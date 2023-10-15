# imports 
import os
import pytest
from xmlParser import parse_XML

# Testing the parse_XML functionality
def test_parse_xml_valid(filepath):
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
