import pytest
from unittest.mock import patch
from parser.product_manipulation import increase_price

# Mock product data for testing
mock_products = [{'category': 'Electronics', 'name': 'Laptop', 'price': 1000.0, 'rating': 4.5}]

def test_increase_price(monkeypatch):
    inputs = iter(['Electronics', '10'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    updated_products = increase_price(mock_products)

    assert updated_products[0]['price'] == 1100.0
