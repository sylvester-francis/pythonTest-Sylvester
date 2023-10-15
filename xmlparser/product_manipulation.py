from prettytable import PrettyTable
from helper import return_min_max_rating
min_rating,max_rating =return_min_max_rating()

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
        raise

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
        raise

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
        raise

