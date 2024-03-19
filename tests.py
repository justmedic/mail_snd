
from fastapi.testclient import TestClient
from decimal import Decimal
import pytest
from api_core import app  # Импорт приложения FastAPI

client = TestClient(app)

def test_receive_order():
    response = client.post("/order/", json={
    "product_info_list": [
        {
            "Товар": "Laptop",
            "Ссылка": "http://testserver/shop/products/detail/laptop/",
            "Количество": 1,
            "Цена за единицу": "1000.00",
            "Характеристики": "15.6 inch, 8GB RAM, 256GB SSD."
        },
        {
            "Товар": "Smartphone",
            "Ссылка": "http://testserver/shop/products/detail/smartphone/",
            "Количество": 2,
            "Цена за единицу": "500.00",
            "Характеристики": "6.5 inch, 128GB storage, 6GB RAM."
        },
        {
            "Товар": "Headphones",
            "Ссылка": "http://testserver/shop/products/detail/headphones/",
            "Количество": 3,
            "Цена за единицу": "150.00",
            "Характеристики": "Noise canceling, Wireless."
        },
        {
            "Товар": "Keyboard",
            "Ссылка": "http://testserver/shop/products/detail/keyboard/",
            "Количество": 1,
            "Цена за единицу": "70.00",
            "Характеристики": "Mechanical, RGB backlighting."
        },
        {
            "Товар": "Mouse",
            "Ссылка": "http://testserver/shop/products/detail/mouse/",
            "Количество": 1,
            "Цена за единицу": "40.00",
            "Характеристики": "Wireless, Gaming, 16000 DPI."
        }
    ],
    "user": "testemail@example.com",
    "user_phone": "89991231234",
    "Order_id": 2
})

    print('вроде все ок')


test_receive_order()