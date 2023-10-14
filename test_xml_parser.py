# imports 
import pytest
from xmlParser import read_file, parse_XML, increase_price, rename_category, remove_products, save_changes, generate_reports, quit

# Fixture to hold sample XML data
@pytest.fixture
def xml_data():
    return """<products>
            <product category="Electronics">
                <name>Iphone 12 Pro</name> 
                <price>599.99</price> 
                <rating>4.5</rating>
            </product>
            <product category="Books">
                <name>Python for Beginners</name> 
                <price>29.99</price> 
                <rating>4.0</rating>
            </product>
            <product category="Electronics">
                <name>Ipod</name> 
                <price>49.99</price>
                <rating>3.9</rating>
            </product>
        </products>"""

# Fixture for file path
@pytest.fixture
def filepath(xml_data, tmp_path):
    file_path = tmp_path / "test.xml"
    with open(file_path, 'w') as f:
        f.write(xml_data)
    return file_path

def test_read_file(filepath):
    result = read_file(filepath)
    assert result == filepath

# parse_XML tests
def test_parse_xml(filepath):
    result= parse_XML(filepath)
    expectedResult = [{'category': 'Electronics', 'name': 'Iphone 12 Pro', 'price': 599.99, 'rating': 4.5}, {'category': 'Books', 'name': 'Python for Beginners', 'price': 29.99, 'rating': 4.0}, {'category': 'Electronics', 'name': 'Ipod', 'price': 49.99, 'rating': 3.9}]
    assert expectedResult == result



def test_increase_price(monkeypatch):
    products = [
        {'category': 'Electronics', 'name': 'Laptop', 'price': 999.99, 'rating': 4.2},
        {'category': 'Books', 'name': 'Python Basics', 'price': 29.99, 'rating': 4.5},
        {'category': 'Electronics', 'name': 'Smartphone', 'price': 499.99, 'rating': 4.0},
    ]
    inputs = iter(['Electronics', '5'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    increase_price(products)
    assert products[0]['price'] == pytest.approx(1049.99, rel=1e-2) 
    assert products[1]['price'] == 29.99  
    assert products[2]['price'] == pytest.approx(524.99, rel=1e-2)  





