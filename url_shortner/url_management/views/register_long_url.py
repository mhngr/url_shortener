from rest_framework.views import APIView
from ..models import Url
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from ..serializers import UrlSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from ..functions import url_shortener

#
#

class RegisterLongUrl(APIView):
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         Url.objects.create(**data)
#         return Response(data={'message': 'Your url created successfully'}, status=HTTP_201_CREATED)
    def post(self, request, *args, **kwargs):
        data = request.data
        long_url = data.get('long_url')
        short_url = url_shortener(long_url)
        data['short_url'] = short_url
        serializer = UrlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# class RegisterLongUrl(CreateAPIView):
#     serializer_class = UrlSerializer
#     queryset = Url.objects.all()
#
#     def perform_create(self, serializer):
#         short_url = url_shortener(self.request.data.get('long_url'))
#         serializer.save(short_url=short_url)
