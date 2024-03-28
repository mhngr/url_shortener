from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, DestroyAPIView
from ..models import Url
from ..serializers import UrlSerializer


# class ShortUrlDetail(APIView):
#     def get(self, request, *args, **kwargs):
#         url_id = kwargs['url_id']
#         objects = Url.objects.get(id=url_id)
#         serializer = UrlSerializer(objects)
#         return Response(data=serializer.data, status=HTTP_200_OK)

class ShortUrlDetail(RetrieveAPIView):
    serializer_class = UrlSerializer

    def get_object(self, *args, **kwargs):
        url_id = self.kwargs['url_id']
        return Url.objects.get(id=url_id)


class DeleteUrl(APIView):
    def delete(self, request, *args, **kwargs):
        url_id = kwargs['url_id']
        Url.objects.get(id=url_id).delete()
        return Response(status=HTTP_204_NO_CONTENT)



class DeleteUrl(DestroyAPIView):
    def get_object(self, *args, **kwargs):
        url_id = self.kwargs['url_id']
        return Url.objects.get(id=url_id)
