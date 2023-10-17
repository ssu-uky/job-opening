import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from companies.models import Company
from companies.serializers import CompanySerializer
from .models import Recruit
from .serializers import RecruitSerializer


client = APIClient()


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


@pytest.fixture()
def create_pagenation_recruit(create_company):
    """페이지네이션 테스트를 위한 공고 데이터 생성"""
    recruits = []
    for i in range(10):
        recruit = Recruit.objects.create(
            company=create_company,
            title=f"test_title_{i}",
            position=f"test_position_{i}",
            reward=1000000,
            skill=f"test_skill_{i}",
            content=f"test_content_{i}",
        )
        recruits.append(recruit)
    return recruits


@pytest.mark.django_db
def test_create_recruit(create_company):
    """공고 생성 테스트"""
    url = reverse("new_recruit")
    data = {
        "company": create_company.company_name,
        "title": "new_test_title",
        "position": "new_test_position",
        "reward": 2000000,
        "skill": "new_test_skill",
        "content": "new_test_content",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Recruit.objects.count() == 1
    assert Recruit.objects.get(id=response.data["id"]).title == "new_test_title"


# 회사가 등록 되어 있지 않은 경우
@pytest.mark.django_db
def test_create_recruit_no_company():
    """공고 생성 테스트 / 회사가 등록되어있지 않을 경우"""
    url = reverse("new_recruit")
    data = {
        "company": "no_exist_company",
        "title": "test_title",
        "position": "test_position",
        "reward": 1000000,
        "skill": "test_skill",
        "content": "test_content",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "등록되지 않은 회사입니다."
    assert Recruit.objects.count() == 0


@pytest.mark.django_db
def test_recruit_list(create_recruit):
    """공고 리스트 조회"""
    url = reverse("recruit_list")
    response = client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK

    assert "results" in response.data

    results = response.data["results"]
    assert isinstance(results, list)

    assert results, "공고가 없습니다."

    for recruit in results:
        assert all(key in recruit for key in RecruitSerializer.Meta.fields)

    assert Recruit.objects.count() == 1


@pytest.mark.django_db
def test_recruit_list_pagination(create_pagenation_recruit):
    """공고 리스트 페이지네이션 테스트"""
    url = reverse("recruit_list")
    response = client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert "results" in response.data
    assert len(response.data["results"]) <= 5


@pytest.mark.django_db
def test_recruit_search(create_recruit):
    """공고 검색 테스트"""
    url = reverse("recruit_list")
    response = client.get(url, {"search": "test"}, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0


@pytest.mark.django_db
def test_recruit_search_no_result(create_recruit):
    """공고 검색 테스트 / 검색 결과가 없는 경우"""
    url = reverse("recruit_list")
    response = client.get(url, {"search": "found"}, format="json")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["message"] == "검색 결과가 없습니다."
    assert len(response.data) == 1
