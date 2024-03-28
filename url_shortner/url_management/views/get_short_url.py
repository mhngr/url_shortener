from ..functions import url_shortener
from rest_framework.views import APIView
from ..functions import url_shortener
from ..serializers import UrlSerializer, UrlSerializerV2
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from ..models import Url
from rest_framework.generics import ListAPIView


# class ShortUrlList(APIView):
#
#     def get(self, request, *args, **kwargs):
#         data = request.GET
#         objects = Url.objects.filter(username=data["username"], category=data["category"], name=data["name"])
#         serializer = UrlSerializerV2(objects, many=True)
#         return Response(data=serializer.data, status=HTTP_200_OK)

class ShortUrlList(ListAPIView):
    serializer_class = UrlSerializerV2

    def get_queryset(self):
        data = self.request.GET
        return Url.objects.filter(username=data["username"], category=data["category"])