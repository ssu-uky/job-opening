from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import User
from recruits.models import Recruit
from .serializers import UserSerializer, UserRecruitSerializer


class NewUserView(APIView):
    """회원가입"""

    def get(self, request):
        return Response({"message": "username, password를 입력해주세요."})

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):
    """회원 리스트"""

    def get(self, request):
        users = User.objects.all()
        serializer = UserRecruitSerializer(users, many=True)
        return Response(serializer.data)


class UserRecruitView(APIView):
    """회사 지원"""

    def get_object(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFound()

    def get(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserRecruitSerializer(user)
        return Response(serializer.data)

    def post(self, request, user_id):
        recruit_id = request.data.get("recruit_id")
        
        try:
            user = User.objects.get(pk=user_id)
            recruit = Recruit.objects.get(pk=recruit_id)
        except User.DoesNotExist:
            return Response({"message":"존재하지 않는 회원입니다."}, status=status.HTTP_404_NOT_FOUND)
        except Recruit.DoesNotExist:
            return Response({"message":"존재하지 않는 채용공고입니다."}, status=status.HTTP_404_NOT_FOUND)
        
        
        if user.user_recruit is not None:
            return Response({"message":"이미 지원한 채용공고가 있습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        user.user_recruit = recruit
        user.save()
        
        serializer = UserRecruitSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)