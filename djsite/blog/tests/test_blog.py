from django.urls import reverse
from djsite.django_assertions import assert_contains
import pytest
from model_bakery import baker

from djsite.blog.models import Post


@pytest.fixture
def posts(db):
    return baker.make(Post, 3, status='published')


@pytest.fixture
def resp(client, posts):
    resp = client.get(reverse('blog:post_list'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>My blog</title>')


def test_posts_titulo(resp, posts):
    for post in posts:
        assert_contains(resp, post.title)


def test_posts_links(resp, posts):
    for post in posts:
        assert_contains(resp, post.get_absolute_url())


def test_posts_author(resp, posts):
    for post in posts:
        assert_contains(resp, post.author)


def test_posts_body(resp, posts):
    for post in posts:
        assert_contains(resp, post.body[:20])
