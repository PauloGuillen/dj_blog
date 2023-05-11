from django.urls import reverse
from djsite.django_assertions import assert_contains
import pytest
from model_bakery import baker

from djsite.blog.models import Post
from djsite.blog.forms import EmailPostForm


@pytest.fixture
def post(db):
    return baker.make(Post, status='published')


@pytest.fixture
def resp(client, post):
    resp = client.get(reverse("blog:post_share", args=[post.id]))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_form_fields(resp):
    form = EmailPostForm()
    list_field = []
    for field in form:
        assert_contains(resp, f'name="{field.name}"')
        list_field.append(field.name)
    assert {'name', 'email', 'to', 'comments'}.issubset(set(list_field))


def test_form_submit(resp):
    assert_contains(resp, '<input type="submit" value="Send E-mail">')


def test_form_title(resp, post):
    assert_contains(resp, f'<h1>Share "{post.title}" by e-mail</h1>')
