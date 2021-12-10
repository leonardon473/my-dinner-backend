# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.views import APIView

# Project libs
from apps.orders.services.order import get_menu_items_sales_by_type_of_cuisine
from apps.utils.time import parse_date

# If type checking, __all__
if TYPE_CHECKING:
    from typing import Any, Optional
    from datetime import date
    from rest_framework.request import Request

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


def parse_date_query_param(date_string: str, query_param_name: str) -> "Optional[date]":
    if not date_string:
        return None
    try:
        return parse_date(date_string)
    except ValueError:
        raise ValidationError({query_param_name: "Error parsing data"})


# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class CustomSchema(AutoSchema):
    def get_operation(self, path, method):
        operation = super().get_operation(path, method)
        operation["parameters"] += [
            {
                "name": "from_date",
                "required": True,
                "in": "query",
                "description": "Date to start to show results.",
                "schema": {
                    "type": "date",
                },
            },
            {
                "name": "to_date",
                "required": True,
                "in": "query",
                "description": "Date until results will be shown.",
                "schema": {
                    "type": "date",
                },
            },
        ]
        return operation


class MenuItemsSalesByTypeOfCuisineView(APIView):
    schema = CustomSchema()

    def get(self, request: "Request", *args: "Any", **kwargs: "Any"):
        from_date = parse_date_query_param(
            request.query_params.get("from_date"),
            "from_date",
        )
        to_date = parse_date_query_param(
            request.query_params.get("to_date"),
            "to_date",
        )
        if from_date and to_date:
            result = get_menu_items_sales_by_type_of_cuisine(from_date, to_date)
            return Response(
                result,
                status=status.HTTP_200_OK,
            )

        return Response(
            "Query params 'from_date' and 'to_date' must be included",
            status=status.HTTP_400_BAD_REQUEST,
        )
