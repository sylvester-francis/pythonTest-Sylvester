# imports 
import os
import pytest
from xmlparser.xmlParser import read_file

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

# Testing the read_file functionality
def test_read_file(filepath):
    # This test scenario is used to validate the functionality of the read_file function by providing a valid filepath
    result = read_file(filepath)
    assert result == filepath

def test_read_file_returns_none():
    # This test scenario is used to validate the functionality of the read_file function by providing a empty filepath
    filepath = ""
    result = read_file(filepath)
    assert result is None








