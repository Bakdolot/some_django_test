from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Logging
from .serializers import MainResponseSerializer, SomeSerializer
from .utils import get_client_ip


class MainView(GenericAPIView):
    serializer_class = SomeSerializer
    response_serializer = MainResponseSerializer

    @extend_schema(responses={status.HTTP_200_OK: response_serializer})
    def post(self, request):
        is_valid = self.get_serializer_class()(request.data).is_valid_string()
        response_data = self.response_serializer({"is_valid": is_valid}).data
        Logging.objects.create(
            source_ip=get_client_ip(request), request_data=request.data, response_data=response_data
        )
        return Response(response_data, status=status.HTTP_200_OK)
