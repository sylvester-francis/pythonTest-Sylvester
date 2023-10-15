import pytest
from unittest.mock import patch

from parser.user_interface import menu

# Mock product data for testing
mock_products = [{'category': 'Electronics', 'name': 'Laptop', 'price': 1000.0, 'rating': 4.5}]

# Test menu with invalid user choice
def test_menu_invalid_choice(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "7")
    menu(mock_products)
    captured = capsys.readouterr()
    assert "Invalid input. Please select a valid option" in captured.out
    assert "Please select an option (Enter a number 1-6)" in captured.out  # assert that the menu is shown again


# Test menu choice "6" (Exit)
def test_menu_exit(capsys):
    with patch('builtins.input', return_value="6"):
        with pytest.raises(SystemExit):
            menu(mock_products)
