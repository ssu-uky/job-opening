import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Company

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


@pytest.mark.django_db
def test_new_company_view(create_company):
    """회사 생성 테스트"""
    url = reverse("new_company")
    data = {
        "company_name": "new_test_company",
        "address": "new_test_address",
        "country": "new_test_country",
        "city": "new_test_city",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Company.objects.count() == 2
    assert (
        Company.objects.get(id=response.data["id"]).company_name == "new_test_company"
    )


@pytest.mark.django_db
def duplicate_company_name_test(create_company):
    """회사 이름 중복 테스트"""
    url = reverse("new_company")
    data = {
        "company_name": "new_test_company",
        "address": "duplicate_test_address",
        "country": "duplicate_test_country",
        "city": "duplicate_test_city",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "이미 등록되어있는 회사 입니다." in str(response.data["company_name"])
    assert Company.objects.count() == 1


@pytest.mark.django_db
def test_company_list_view(create_company):
    """회사 리스트 조회"""
    url = reverse("company_list")
    response = client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert Company.objects.count() == 1
    assert (
        Company.objects.get(id=response.data[0]["id"]).company_name
        == create_company.company_name
    )


@pytest.mark.django_db
def test_company_detail_view(create_company):
    """회사 조회, 수정, 삭제 테스트"""
    url = reverse("company_detail", kwargs={"pk": create_company.id})

    # GET
    response = client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    company = Company.objects.get(id=response.data["id"])

    # assert company.company_name == create_company.company_name
    # assert company.address == create_company.address
    # assert company.country == create_company.country
    # assert company.city == create_company.city

    for company, item in response.data.items():
        assert getattr(create_company, company) == item

    # PUT
    updated_data = {
        "company_name": "update_test_company",
        "address": "update_test_address",
        "country": "update_test_country",
        "city": "update_test_city",
    }
    response = client.put(url, updated_data, format="json")
    assert response.status_code == status.HTTP_200_OK

    # db update
    create_company.refresh_from_db()

    # assert create_company.company_name == updated_data["company_name"]
    # assert create_company.address == updated_data["address"]
    # assert create_company.country == updated_data["country"]
    # assert create_company.city == updated_data["city"]

    for company, updated_data in updated_data.items():
        assert getattr(create_company, company) == updated_data

    # DELETE
    response = client.delete(url, format="json")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Company.objects.count() == 0
