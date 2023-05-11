from django.urls import reverse
from django.utils import timezone
from djsite.django_assertions import assert_contains
import pytest
from model_bakery import baker

from djsite.blog.models import Post


@pytest.fixture
def post(db):
    return baker.make(Post, status='published', publish=timezone.now())


@pytest.fixture
def resp(client, post):
    return client.get(reverse('blog:post_detail',
                              kwargs={'year': post.publish.year,
                                      'month': post.publish.month,
                                      'day': post.publish.day,
                                      'post': post.slug}))


@pytest.fixture
def resp_nao_encotrado(client, post):
    return client.get(reverse('blog:post_detail',
                              kwargs={'year': post.publish.year,
                                      'month': post.publish.month,
                                      'day': post.publish.day,
                                      'post': post.slug+'post_nao_encotrado'}))


def test_status_code(resp):
    assert resp.status_code == 200


def test_post_nao_encontrado(resp_nao_encotrado):
    assert resp_nao_encotrado.status_code == 404


def test_detail_titulo(resp, post):
    assert_contains(resp, post.title)


def test_detail_author(resp, post):
    assert_contains(resp, post.author)


def test_detail_body(resp, post):
    assert_contains(resp, post.body)


def test_detail_share(resp, post):
    assert_contains(resp, 'Share this post')


def test_detail_share_link(resp, post):
    assert_contains(resp, f'href="{reverse("blog:post_share", args=[post.id])}"')
