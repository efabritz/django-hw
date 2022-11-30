import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_course_retrieve(client, course_factory):
    #Arrange
    courses = course_factory(_quantity=1)

    #Act
    response = client.get(f"/api/v1/courses/{courses[0].id}/")

    #Assert
    data = response.json()
    assert data['name'] == courses[0].name


@pytest.mark.django_db
def test_course_list(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get("/api/v1/courses/")

    # Assert
    data = response.json()
    assert len(data) == len(courses)

    for index, course in enumerate(data):
        assert course['name'] == courses[index].name


@pytest.mark.django_db
def test_course_filter_id(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    f_id = courses[0].id
    f_url = f"/api/v1/courses/?id={f_id}"

    # Act
    response = client.get(f_url)
    data = response.json()

    # Assert
    assert courses[0].name == data[0]['name']


@pytest.mark.django_db
def test_course_filter_name(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    f_name = courses[1].name
    f_url = f"/api/v1/courses/?name={f_name}"

    # Act
    response = client.get(f_url)
    data = response.json()

    # Assert
    assert courses[1].name == data[0]['name']


@pytest.mark.django_db
def test_course_create(client, course_factory):
    # Arrange
    count = Course.objects.count()

    # Act
    response = client.post("/api/v1/courses/", data={'name': 'Übersetzerbau',})

    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_course_update(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=1)

    # Act
    f_id = courses[0].id
    response_update = client.patch(f"/api/v1/courses/{f_id}/", data={'name': 'updated_name'})
    assert response_update.status_code == 200
    response_get = client.get(f"/api/v1/courses/{f_id}/")
    data = response_get.json()

    # Assert
    assert data['name'] == 'updated_name'

@pytest.mark.django_db
def test_course_delete(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=1)

    # Act
    f_id = courses[0].id
    response_delete = client.delete(f"/api/v1/courses/{f_id}/")
    assert response_delete.status_code == 204
    response_get = client.get(f"/api/v1/courses/{f_id}/")
    data = response_get.json()

    # Assert
    assert data['detail'] == 'Not found.'
