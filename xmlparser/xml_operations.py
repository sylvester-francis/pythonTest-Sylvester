import xml.etree.ElementTree as ET

def parse_XML(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        products = []
        for product in root.findall('product'):
            products.append({
                'category': product.get('category'),
                'name': product.find('name').text,
                'price': float(product.find('price').text),
                'rating': float(product.find('rating').text)
            })
        return products
    except Exception as e:
        print(f"Error parsing the provided XML file: {type(e).__name__} : Error message - {e}")
        raise