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
    file_path = tmp_path / "./testFile.xml"
    with open(file_path, 'w') as f:
        f.write(xml_data)
    return file_path

def test_read_file(filepath):
    result = read_file(filepath)
    assert result == filepath


# Testing the parse_XML functionality
def test_parse_xml(filepath):
    # This test scenario is used to validate the functionality of the parse_XML by providing a valid xml string
    result= parse_XML(filepath)
    expectedResult = [{'category': 'Electronics', 'name': 'Iphone 12 Pro', 'price': 599.99, 'rating': 4.5}, {'category': 'Books', 'name': 'Python for Beginners', 'price': 29.99, 'rating': 4.0}, {'category': 'Electronics', 'name': 'Ipod', 'price': 49.99, 'rating': 3.9}]
    assert expectedResult == result

def test_parse_empty_xml():
    # This test scenario is used to validate how the parse_XML function behaves by providing an empty xml string
    xml_str = "<products></products>"
    with open('./testFile.xml','w') as fp:
        fp.write(xml_str)
    result = parse_XML('./testFile.xml')
    assert result == []

def test_parse_invalid_xml():
    # This test scenario is used to validate how the parse_XML function behaves by providing an invalid xml string
    invalidXMLstr = "Test string"
    with open('./testFile.xml', 'w') as fp:
        fp.write(invalidXMLstr)
    result = parse_XML('./testFile.xml')
    assert result == []    

def test_parse_missing_elements():
    # This test scenario is used to validate how the parse_XML function behaves by providing an xml with missing tags
    missingElementsStr = """<products>
        <product category="Electronics">
            <name>Laptop</name>
        </product>
    </products>
    """
    with open('./testFile.xml', 'w') as fp:
        fp.write(missingElementsStr)
    result = parse_XML('./testFile.xml')
    assert result == []

def test_parse_non_numeric_rating():
    # This test scenario is used to validate how the parse_XML function behaves by providing an xml with non-numeric rating
    nonNumericRatingStr = """
    <products>
        <product category="Electronics">
            <name>Laptop</name>
            <price>999.99</price>
            <rating>invalidRating</rating>
        </product>
    </products>
    """
    with open('./testFile.xml', 'w') as fp:
        fp.write(nonNumericRatingStr)
    result = parse_XML('./testFile.xml')
    assert result == []
def test_parse_non_numeric_price():
    # This test scenario is used to validate how the parse_XML function behaves by providing an xml with non-numeric price
    xml_content = """
    <products>
        <product category="Electronics">
            <name>Laptop</name>
            <price>Invalidprice</price>
            <rating>4.2</rating>
        </product>
    </products>
    """
    with open('./testFile.xml', 'w') as fp:
        fp.write(xml_content)
    result = parse_XML('./testFile.xml')
    assert result == []


# Testing the increase price functionality
def test_price_increase(monkeypatch):
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





