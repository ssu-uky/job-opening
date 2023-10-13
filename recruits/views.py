import json
from django.http import JsonResponse, HttpResponse

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from companies.models import Company
from .models import Recruit
from .serializers import RecruitSerializer, RecruitListSerializer


class CreateRecruitView(APIView):
    """공고글 생성"""

    def get(self, request):
        return Response(
            {"message": "company, title, position, reward, skill, content 를 입력해주세요."}
        )

    def post(self, request):
        serializer = RecruitSerializer(data=request.data)

        if serializer.is_valid():
            company_name = request.data.get("company")

            try:
                company = Company.objects.get(company_name=company_name)
            except Company.DoesNotExist:
                return Response(
                    {"message": "회사를 찾을 수 없습니다."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            recruit = serializer.save(company=company)
            recruit_data = serializer.data
            return Response(
                {"message": "공고글이 생성되었습니다.", "공고 내용": recruit_data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecruitListView(APIView):
    """
    채용공고 리스트 / 검색가능
    """

    def get(self, request):
        company_name = request.GET.get("search")

        if company_name:
            company = get_object_or_404(Company, company_name=company_name)
            recruits = Recruit.objects.filter(company=company)
        else:
            recruits = Recruit.objects.all()

        paginator = PageNumberPagination()
        paginated_recruits = paginator.paginate_queryset(recruits, request)
        serializer = RecruitListSerializer(paginated_recruits, many=True)

        return paginator.get_paginated_response(serializer.data)


class RecruitDetailView(APIView):
    def get_object(self, pk):
        try:
            return Recruit.objects.get(pk=pk)
        except Recruit.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        recruit = self.get_object(pk)
        serializer = RecruitSerializer(recruit)
        
        same_company_recruits = Recruit.objects.filter(company=recruit.company).exclude(pk=pk)
        another_recruits = [{"id": recruit.id, "title": recruit.title} for recruit in same_company_recruits]
        # another_recruits = [recruit.id for recruit in same_company_recruits]
        
        serializer = RecruitSerializer(recruit)
        recruit_data = serializer.data
        
        recruit_data["same_company_recruits"] = another_recruits
        
        return Response(recruit_data)

    def put(self, request, pk):
        recruit = self.get_object(pk)
        serializer = RecruitSerializer(
            recruit,
            data=request.data,
            partial=True,
        )
        if "company" in request.data:
            return Response(
                {"message": "회사는 수정할 수 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "공고글이 수정되었습니다.", "공고 내용": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recruit = self.get_object(pk)
        recruit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
