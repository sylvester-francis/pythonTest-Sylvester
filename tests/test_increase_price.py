# imports 
import os
import pytest
from xmlparser.xmlParser import increase_price

# Testing the increase price functionality
def test_price_increase_valid(monkeypatch):
    products = [
        {'category': 'Electronics', 'name': 'Laptop', 'price': 999.99, 'rating': 4.2},
        {'category': 'Books', 'name': 'Python Basics', 'price': 29.99, 'rating': 4.5},
        {'category': 'Electronics', 'name': 'Smartphone', 'price': 499.99, 'rating': 4.0},
    ]
    inputs = iter(['Electronics', '5'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    updatedproducts=increase_price(products)
    assert updatedproducts[0]['price'] == pytest.approx(1049.99, rel=1e-2) 
    assert updatedproducts[1]['price'] == 29.99  
    assert updatedproducts[2]['price'] == pytest.approx(524.99, rel=1e-2)  


def test_increase_price_output_params(monkeypatch):
    # This test scenario checks if the return values are a list of dictionaries
    products = [{'category':'Electronics','name':'laptop','price':876,'rating':4}]
    inputs = iter(['Electronics', '3'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    updatedproducts =increase_price(products)
    assert isinstance(updatedproducts, list)
    assert isinstance(updatedproducts[0],dict)
    
def test_increase_price_Exception(monkeypatch, capsys):
    # This test scenario checks if provided a non-numeric value for user input "Percentage" - The code correctly raises an Exception
    products = [
        {'category': 'Electronics', 'name': 'Laptop', 'price': 999.99, 'rating': 4.2},
        {'category': 'Books', 'name': 'Python Basics', 'price': 29.99, 'rating': 4.5},
        {'category': 'Electronics', 'name': 'Smartphone', 'price': 499.99, 'rating': 4.0},
    ]
    inputs = iter(['Electronics', 'abc'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    increase_price(products)
    captured = capsys.readouterr()
    assert "An exception occured while trying to increase the price: ValueError : Error message - could not convert string to float: 'abc'" in captured.out   

