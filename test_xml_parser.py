import pytest
from xmlParser import read_file, parse_XML, increase_price, rename_category, remove_products, save_changes, generate_reports, quit

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

@pytest.fixture
def filepath(xml_data, tmp_path):
    file_path = tmp_path / "test.xml"
    with open(file_path, 'w') as f:
        f.write(xml_data)
    return file_path

def test_read_file(filepath):
    result = read_file(filepath)
    assert result == filepath

def test_parse_XML(filepath):
    products = parse_XML(filepath)
    assert len(products) == 3

