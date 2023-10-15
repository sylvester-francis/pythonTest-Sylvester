'''
A basic XML parser tool which parses an XML file containing product data, manipulates the data 
and saves the results back to the xml file and generates reports from the xml file

Author: Sylvester Ranjith Francis
Date created : 10/13/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/13/2023
'''
#imports 
import argparse
import os,sys
import xml.etree.ElementTree as ET
try:
    from prettytable import PrettyTable
except ImportError as e:
    print("Please install 'prettytable' module using pip")


# Global variables for parsing arguments
parser = argparse.ArgumentParser(description="XML Product Data parser")
parser.add_argument('filepath', type=str, help="Please provide the path to the file containing the xml product data")
args = parser.parse_args()

# Configurable parameters
min_rating = 0.0
max_rating = 5.0

def read_file(filepath):
    try:
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"The specified file is not found: {filepath}")
        return filepath
    except Exception as e:
        print(f"An exception occured while trying to find the file: {type(e).__name__} : Error message - {e}")
        return None
    
def parse_XML(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        products = []
        for product in root.findall('product'):
            products.append({
                'category' : product.get('category'),
                'name': product.find('name').text,
                'price':float(product.find('price').text),
                'rating':float(product.find('rating').text)
            })
        return products
    except Exception as e:
        print(f"Error parsing the provided XML file: {type(e).__name__} : Error message - {e}")
        return []


def increase_price(products):
    try:
        existing_categories = list(set(existing_category['category'] for existing_category in products))
        print("The following are the categories of products in the inventory")
        for index,category in enumerate(existing_categories):
            print(f'{index+1}:{category}')    
        user_category = input("Enter the category of the products to increase the price of: ")
        if user_category not in existing_categories:
            print("Category does not exist")
            return
        percentage = float(input("Enter the percentage to increase the price by: "))
        for product in products:
            if product['category'] == user_category:
                product['price'] = round(product['price']+ (product['price'] * percentage / 100),2)
        return products
    except Exception as e:
        print(f"An exception occured while trying to increase the price: {type(e).__name__} : Error message - {e}")
        return []    

def rename_category(products):
    try:
        existing_categories = list(set(existing_category['category'] for existing_category in products))
        print("The following are the categories of products in the inventory")
        for index,category in enumerate(existing_categories):
            print(f'{index+1}:{category}')    
        user_category = input("Enter the category to be renamed: ")
        if user_category not in existing_categories:
            print("Category does not exist")
            return
        new_user_category= input("Enter the name you want to give this category:")
        if not new_user_category:
            raise ValueError("New Category cannot be empty string")
        for product in products:
            if product['category'] == user_category:
                product['category'] = new_user_category
        return products
    except Exception as e:
        print(f"An exception occured while trying to rename the category: {type(e).__name__} : Error message - {e}")    
        return []

def remove_products(products):
    try:
        rating = float(input("Enter the rating below which all the products need to be removed:"))
        if ((rating <= min_rating) or (rating >= max_rating)):
            raise ValueError(f"Value should be between {min_rating} and {max_rating}")
        for product in products:
            if product['rating'] < rating:
                products.remove(product)
        return products
    except ValueError as e:
        print(f"An exception occured while trying to remove the category: {type(e).__name__} : Error message - The value must be a number")    
        return []


def save_changes(products):
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


def generate_reports(products):
    try:
        if not products:
            print("No products found in inventory")
            return
        total_products_by_category = {}
        total_price_by_category = {}
        for product in products:
            category = product['category']
            if category not in total_products_by_category:
                total_products_by_category[category] = 0
                total_price_by_category[category] = 0
            total_products_by_category[category] += 1
            total_price_by_category[category] += product['price']
        table = PrettyTable()
        table.field_names = ["Category", "Total Products by Category", "Total Price by Category"]
        for category in total_products_by_category:
            table.add_row([category, total_products_by_category[category], total_price_by_category[category]])
        print(table)
    except Exception as e:
        print(f"An exception occured while trying to generate reports: {type(e).__name__} : Error message - {e}")

    
def quit(products):
    save_changes(products)
    sys.exit(1)
    

def menu():
    xml_file = read_file(args.filepath)
    if not xml_file:
        print("The specified file path is not found")
        return
    products = parse_XML(xml_file)
    menu_options = {
        "1":"Increase prices",
        "2":"Rename categories" ,
        "3":"Remove products" , 
        "4":"Generate report",
        "5":"Save the file",
        "6":"Exit"
    }
    print("**********************************************************************************")
    print("Welcome user")
    print("**********************************************************************************")
    print("Please select an option (Enter a number 1-6)")
    for key,value in menu_options.items():
        print(f"{key}:{value}")
    choice = input(">  ")   
    if choice not in menu_options:
        print("Invalid input. Please select a valid option ")
        return
    if choice == "1":
        print("Increasing prices")
        updated_products = increase_price(products)
        if updated_products:
            save_changes(updated_products)
        else:
            save_changes(products)
    elif choice == "2":
        print("Renaming categories")
        renamed_products =rename_category(products)
        if renamed_products:
            save_changes(renamed_products)
        else:
            save_changes(products)
    elif choice == "3":
        print("Removing products based on rating")
        products_after_removal = remove_products(products)
        if products_after_removal:
            save_changes(products_after_removal)
        else:
            save_changes(products)
    elif choice == "4":
        print("Generating reports")
        generate_reports(products)
    elif choice == "5":
        print("Saving the file")
        save_changes(products)    
    elif choice == "6":
        print("Exiting... Goodbye")
        quit(products)
    menu()    

if __name__ == '__main__':
    menu()