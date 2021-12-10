# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Project libs
from apps.orders.models import Order
from apps.orders.serializers.order import OrderCreateSerializer, OrderRetrieveSerializer
from apps.orders.services.create_order import CreateOrderService

# If type checking, __all__
if TYPE_CHECKING:
    from typing import Any
    from rest_framework.request import Request

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class OrderCreateListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderRetrieveSerializer

    def post(self, request: "Request", *args: "Any", **kwargs: "Any"):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = self.perform_create(serializer)
        serializer = OrderRetrieveSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer: "OrderCreateSerializer"):
        service = CreateOrderService(serializer.validated_data)
        return service.create()


class OrderRetrieveView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderRetrieveSerializer
