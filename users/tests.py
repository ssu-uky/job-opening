import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User

from companies.models import Company
from recruits.models import Recruit

client = APIClient()


@pytest.fixture()
def create_user():
    """유저 데이터 생성"""
    return User.objects.create(
        username="test_user",
        password="test_password",
    )


@pytest.fixture()
def create_company():
    """회사 데이터 생성"""
    return Company.objects.create(
        company_name="test_company",
        address="test_address",
        country="test_country",
        city="test_city",
    )


@pytest.fixture()
def create_recruit(create_company):
    """공고 데이터 생성"""
    return Recruit.objects.create(
        company=create_company,
        title="test_title",
        position="test_position",
        reward=1000000,
        skill="test_skill",
        content="test_content",
    )


@pytest.mark.django_db
def test_new_user(create_user):
    """유저 생성 테스트"""
    url = reverse("new_user")
    data = {
        "username": "new_test_user",
        "password": "new_test_password",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 2
    assert User.objects.get(id=response.data["id"]).username == "new_test_user"


@pytest.mark.django_db
def test_user_list(create_user):
    """유저 리스트 조회 테스트"""
    url = reverse("user_list")
    response = client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == User.objects.count()


@pytest.mark.django_db
def test_user_recruit(create_user, create_recruit):
    """회사 지원 테스트"""
    url = reverse("user_recruit", kwargs={"user_id": create_user.id})
    data = {"recruit_id": create_recruit.id}
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    user = User.objects.get(id=create_user.id)
    assert user.user_recruit.id == create_recruit.id


@pytest.mark.django_db
def test_user_already_recruit(create_user, create_recruit):
    """이미 지원한 공고가 있는 경우"""
    url = reverse("user_recruit", kwargs={"user_id": create_user.id})
    user = create_user
    recruit = create_recruit
    user.user_recruit = recruit
    user.save()
    data = {"recruit_id": recruit.id}
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
