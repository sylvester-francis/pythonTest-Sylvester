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


def read_file(filepath):
    try:
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"The specified file is not found: {filepath}")
        return filepath
    except FileNotFoundError as e:
        print(f"An exception occured while trying to find the file: {type(e).__name__} : Error message - {e}")
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
                product['price'] += product['price'] * percentage / 100
        save_changes(products)
    except ValueError:
        print(f"Error: Percentage must be a number.")
    except Exception as e:
        print(f"An exception occured while trying to increase the price: {type(e).__name__} : Error message - {e}")    

def rename_category():
    pass

def remove_products():
    pass

def save_changes(products):
    pass

def generate_reports():
    pass
def quit(products):
    save_changes(products)
    sys.exit(1)
    

def menu():
    parser = argparse.ArgumentParser(description="XML Product Data parser")
    parser.add_argument('filepath', type=str, help="Please provide the path to the file containing the xml product data")
    args = parser.parse_args()
    xml_file = read_file(args.filepath)
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
        increase_price(products)
    elif choice == "2":
        print("Renaming categories")
        rename_category(products)
    elif choice == "3":
        print("Removing products based on rating")
        remove_products(products)
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