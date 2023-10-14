from rest_framework.exceptions import NotFound
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer


class NewCompanyView(APIView):
    """회사 등록"""

    def get(self, request):
        return Response({"message": "company_name, address, country, city 를 입력해주세요."})

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            company_data = serializer.data
            return Response(
                {"message": "회사가 등록되었습니다.", "회사 정보": company_data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyListView(APIView):
    """회사 리스트"""

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)


class CompanyDetailView(APIView):
    """회사 조회 및 수정, 삭제"""

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(
            company,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            company = self.get_object(pk)
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
