from django.urls import path
from .views import post_detail, post_list, post_share

app_name = 'blog'
urlpatterns = [
    # views de postagens
    path('', post_list, name='post_list'),
    # path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name='post_detail'),
    path("<int:post_id>/share/", post_share, name='post_share'),
]
