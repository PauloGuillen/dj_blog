from django.urls import reverse
# from pypro.django_assertions import assert_contains
import pytest


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('blog:post_list'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200