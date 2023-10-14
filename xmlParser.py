'''
A basic XML parser tool which parses an XML file containing product data, manipulates the data 
and saves the results back to the xml file and generates reports from the xml file

Author: Sylvester Ranjith Francis
Date created : 10/13/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/13/2023
'''
#imports 
import os,sys

def parse_XML():
    print("Parse XML function called")
def increase_price():
    pass

def rename_category():
    pass

def remove_products():
    pass

def save_changes():
    pass

def generate_reports():
    pass
def quit():
    sys.exit(1)
    

def menu():
    menu_options = {
        "1":"Increase prices",
        "2":"Rename categories" ,
        "3":"Remove products" , 
        "4":"Generate report",
        "5":"Exit"
    }
    print("**********************************************************************************")
    print("Welcome user")
    print("**********************************************************************************")
    print("Please select an option (Enter a number 1-5)")
    for key,value in menu_options.items():
        print(f"{key}:{value}")
    choice = input(">  ")   
    if choice not in menu_options:
        print("Invalid input. Please select a valid option ")
        return
    if choice == "1":
        print("Increasing prices")
        increase_price()
    elif choice == "2":
        print("Renaming categories")
        rename_category()
    elif choice == "3":
        print("Removing products based on rating")
        remove_products()
    elif choice == "4":
        print("Generating reports")
        generate_reports()
    elif choice == "5":
        print("Exiting... Goodbye")
        quit()
    menu()    

if __name__ == '__main__':
    menu()