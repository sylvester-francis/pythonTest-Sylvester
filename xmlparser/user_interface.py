import sys
from product_manipulation import increase_price, rename_category, remove_products, generate_reports
from file_operations import save_changes

def quit(products):
    save_changes(products)
    sys.exit(1)
    

def menu(products):
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
    menu(products)    
