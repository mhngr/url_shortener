
from django.urls import path
from .views import RegisterLongUrl, ShortUrlList, ShortUrlDetail

urlpatterns = [
    path("register_long_url/", RegisterLongUrl.as_view()),
    path("short-urls/", ShortUrlList.as_view()),
    path("<int:url_id>/short-url-detail/", ShortUrlDetail.as_view())
]
