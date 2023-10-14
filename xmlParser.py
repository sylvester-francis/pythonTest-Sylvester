'''
A basic XML parser tool which parses an XML file containing product data, manipulates the data 
and saves the results back to the xml file and generates reports from the xml file

Author: Sylvester Ranjith Francis
Date created : 10/13/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/13/2023
'''


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
    pass

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
    print("Please select an option")
    for key,value in menu_options.items():
        print(f"{key}:{value}")
    # choice = input(" > ")    



if __name__ == '__main__':
    menu()