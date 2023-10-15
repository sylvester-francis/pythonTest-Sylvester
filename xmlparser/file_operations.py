import os
import xml.etree.ElementTree as ET
from helper import return_args



def read_file(filepath):
    try:
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"The specified file is not found: {filepath}")
        return filepath
    except Exception as e:
        print(f"An exception occurred while trying to find the file: {type(e).__name__} : Error message - {e}")
        raise

def save_changes(products):
    args = return_args()
    root = ET.Element('products')
    for product in products:    
        product_elem = ET.Element('product', category=product['category'])
        name_elem = ET.Element('name')
        name_elem.text = product['name']
        price_elem = ET.Element('price')
        price_elem.text = str(product['price'])
        rating_elem = ET.Element('rating')
        rating_elem.text = str(product['rating'])
        product_elem.append(name_elem)
        product_elem.append(price_elem)
        product_elem.append(rating_elem)
        root.append(product_elem)
    tree = ET.ElementTree(root)
    try:
        tree.write(args.filepath)
    except ET.ParseError as e:
        print(f"An exception occured while trying to save the file: {type(e).__name__} : Error message - {e}")
        raise
