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
