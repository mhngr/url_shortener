
from django.urls import path
from .views import RegisterLongUrl

urlpatterns = [
    path("register_long_url/", RegisterLongUrl.as_view())
]
