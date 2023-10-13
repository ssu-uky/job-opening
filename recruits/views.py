from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Recruit
from .serializers import RecruitSerializer


class CreateRecruitView(APIView):
    """공고글 생성"""

    def get(self, request):
        return Response(
            {"message": "company, title, position, reward, skill, content 를 입력해주세요."}
        )

    def post(self, request):
        serializer = RecruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            recruit_data = serializer.data
            return Response(
                {"message": "공고글이 생성되었습니다.", "공고 내용": recruit_data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecruitListView(APIView):
    """공고글 리스트"""

    def get(self, request):
        recruits = Recruit.objects.all()
        serializer = RecruitSerializer(recruits, many=True)
        return Response(serializer.data)