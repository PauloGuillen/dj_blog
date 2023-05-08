import pytest
from model_bakery import baker

from djsite.blog.models import Post


@pytest.fixture
def posts(db):
    return baker.make(Post, 2, status='published')


@pytest.fixture
def posts_not_published(db):
    return baker.make(Post, 2, status='draft')


def test_published(posts):
    posts_published = Post.published.all()

    assert len(posts_published) > 0
    for post in posts_published:
        assert 'published' == post.status


def test_not_published(posts_not_published):
    posts_published = Post.published.all()

    assert len(posts_published) == 0
