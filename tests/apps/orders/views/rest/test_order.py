import pytest
from freezegun import freeze_time
from model_bakery import baker
from rest_framework.test import APIClient

from apps.users.models import Client, ClientAddress
from apps.menu.models import MenuItem, TypeOfCuisine


pytestmark = pytest.mark.django_db

order_in_available_time = freeze_time("2021-12-10 16:00 -06:00")


class TestCreateOrderView:

    endpoint = "/orders/orders/"

    def setup_method(self, method):
        self.api_client = APIClient()
        self.client = baker.make(Client)
        self.client_address = baker.make(ClientAddress, client=self.client)
        self.type_of_cuisine = baker.make(TypeOfCuisine)

    # @order_in_available_time
    # def test_repeated_elements_return_a_error(self):
    #     # Arrange
    #     menu_item_1 = baker.make(MenuItem, price="200.0")
    #     payload = {
    #         "order_menu_items": [
    #             {"menu_item": menu_item.menu_item_id, "quantity": 1},
    #             {"menu_item": menu_item.menu_item_id, "quantity": 1},
    #         ],
    #         "client": self.client.client_id,
    #         "client_address": self.client_address.client_address_id,
    #     }

    #     # Act
    #     response = self.api_client.post(self.endpoint, data=payload, format="json")

    #     # Assert
    #     data = response.json()
    #     assert response.status_code == 400
    #     assert isinstance(data, dict)

    @order_in_available_time
    def test_raise_error_with_less_than_two_order_menu_items(self):
        # Arrange
        menu_item_1 = baker.make(MenuItem, price="300.0")
        payload = {
            "order_menu_items": [
                {"menu_item": menu_item_1.menu_item_id, "quantity": 2},
            ],
            "client": self.client.client_id,
            "client_address": self.client_address.client_address_id,
        }

        # Act
        response = self.api_client.post(self.endpoint, data=payload, format="json")

        # Assert
        data = response.json()
        assert response.status_code == 400
        assert isinstance(data, dict)
        assert "order_menu_items" in data

    @order_in_available_time
    def test_order_amounts(self):
        # Arrange
        menu_item_1 = baker.make(MenuItem, price="300.0")
        menu_item_2 = baker.make(MenuItem, price="400.0")
        payload = {
            "order_menu_items": [
                {"menu_item": menu_item_1.menu_item_id, "quantity": 2},
                {"menu_item": menu_item_2.menu_item_id, "quantity": 1},
            ],
            "client": self.client.client_id,
            "client_address": self.client_address.client_address_id,
        }

        # Act
        response = self.api_client.post(self.endpoint, data=payload, format="json")

        # Assert
        data = response.json()
        assert response.status_code == 201
        assert isinstance(data, dict)
        assert data["total_amount"] == "1000.00"
        assert data["order_menu_items"][0]["subtotal"] == "600.00"
        assert data["order_menu_items"][1]["subtotal"] == "400.00"

    @freeze_time("2021-12-10 15:59 -06:00")
    def test_raise_error_time_less_than_unavailable_time(self):
        # Arrange
        menu_item_1 = baker.make(MenuItem, price="100.0")
        menu_item_2 = baker.make(MenuItem, price="100.0")
        payload = {
            "order_menu_items": [
                {"menu_item": menu_item_1.menu_item_id, "quantity": 1},
                {"menu_item": menu_item_2.menu_item_id, "quantity": 1},
            ],
            "client": self.client.client_id,
            "client_address": self.client_address.client_address_id,
        }

        # Act
        response = self.api_client.post(self.endpoint, data=payload, format="json")

        # Assert
        data = response.json()
        assert response.status_code == 400
        assert isinstance(data, dict)
        assert "non_field_errors" in data

    @freeze_time("2021-12-10 21:01 -06:00")
    def test_raise_error_time_greater_than_unavailable_time(self):
        # Arrange
        menu_item_1 = baker.make(MenuItem, price="100.0")
        menu_item_2 = baker.make(MenuItem, price="100.0")
        payload = {
            "order_menu_items": [
                {"menu_item": menu_item_1.menu_item_id, "quantity": 1},
                {"menu_item": menu_item_2.menu_item_id, "quantity": 1},
            ],
            "client": self.client.client_id,
            "client_address": self.client_address.client_address_id,
        }

        # Act
        response = self.api_client.post(self.endpoint, data=payload, format="json")

        # Assert
        data = response.json()
        assert response.status_code == 400
        assert isinstance(data, dict)
        assert "non_field_errors" in data

    @order_in_available_time
    def test_raise_error_for_incorrect_client_address(self):
        # Arrange
        random_client_address = baker.make(ClientAddress)
        menu_item_1 = baker.make(MenuItem, price="100.0")
        menu_item_2 = baker.make(MenuItem, price="100.0")
        payload = {
            "order_menu_items": [
                {"menu_item": menu_item_1.menu_item_id, "quantity": 1},
                {"menu_item": menu_item_2.menu_item_id, "quantity": 1},
            ],
            "client": self.client.client_id,
            "client_address": random_client_address.client_address_id,
        }

        # Act
        response = self.api_client.post(self.endpoint, data=payload, format="json")

        # Assert
        data = response.json()
        assert response.status_code == 400
        assert isinstance(data, dict)
        assert "client_address" in data
