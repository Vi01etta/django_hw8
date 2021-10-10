import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_course_retrieve(api_client, course_factory):
    course = course_factory(_quantity=1)[0]
    url = reverse('courses-detail', args=[course.id])
    response = api_client.get(url)
    response_json = response.json()
    assert response.status_code == 200
    assert course.id == response_json['id']


@pytest.mark.django_db
def test_course_list(api_client, course_factory):
    course = course_factory(_quantity=3)
    url = reverse('courses-list')
    response = api_client.get(url)
    response_json = response.json()
    assert response.status_code == 200
    assert len(course) == len(response_json)

@pytest.mark.django_db
def test_course_filter_id(api_client, course_factory):
    course = course_factory(_quantity=3)[1]
    url = reverse('courses-list')
    response = api_client.get(url, {'id': course.id})
    response_json = response.json()[0]
    assert response.status_code == 200
    assert course.id == response_json['id']


@pytest.mark.django_db
def test_course_filter_name(api_client, course_factory):
    course = course_factory(_quantity=5)[4]
    url = reverse('courses-list')
    response = api_client.get(url, {'name': course.name})
    response_json = response.json()[0]
    assert response.status_code == 200
    assert course.name == response_json['name']


@pytest.mark.django_db
def test_create_course(api_client):
    payload = {
        'name': 'Python-разработчик'
    }
    url = reverse('courses-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 201




@pytest.mark.django_db
def test_course_delete(api_client, course_factory):
    course = course_factory(_quantity=1)[0]
    url = reverse('courses-detail', args=[course.id])
    response = api_client.delete(url)
    assert response.status_code == 204



@pytest.mark.django_db
def test_course_update(api_client, course_factory):
    course = course_factory(_quantity=1)[0]
    url = reverse('courses-detail', args=[course.id])
    payload = {
        'name': 'Python-разработчик'
    }
    response = api_client.patch(url, payload)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['name'] == payload['name']