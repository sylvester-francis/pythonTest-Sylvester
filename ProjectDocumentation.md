# XML Product Data Parser

## Overview

The XML Product Data Parser is a tool designed to parse an XML file containing product data, manipulate the data, save the results back to the XML file, and generate reports from the XML file. It allows users to perform various operations such as increasing product prices, renaming categories, removing products based on ratings, generating reports on total products and prices by category, saving changes to the file, and exiting the program.

## Author

- **Author:** Sylvester Ranjith Francis
- **Date Created:** 10/13/2023
- **Last Modified By:** Sylvester Ranjith Francis
- **Last Modified Date:** 10/13/2023

## Requirements

- Python 3.x
- `prettytable` module (install using `pip install prettytable`)

## Usage

### Command-line Arguments

The tool requires a command-line argument specifying the path to the XML file containing product data. Example:

```bash
python xml_parser.py path/to/product_data.xml
```

### Menu Options

1. **Increase Prices**
   - Allows users to increase the prices of products in a specified category by a given percentage.

2. **Rename Categories**
   - Enables users to rename a category of products.

3. **Remove Products**
   - Removes products with a rating below a specified value.

4. **Generate Report**
   - Generates a report showing the total number of products and the total price of products in each category.

5. **Save the File**
   - Saves the changes made to the XML file.

6. **Exit**
   - Exits the program.

## Functions

### `read_file(filepath)`

- Checks if the specified file exists.
- Returns the file path if it exists; otherwise, prints an error message and returns `None`.

### `parse_XML(xml_file)`

- Parses the provided XML file and extracts product data.
- Returns a list of dictionaries containing product information.

### `increase_price(products)`

- Increases the prices of products in a specified category by a given percentage.
- Returns the modified list of products.

### `rename_category(products)`

- Renames a category of products.
- Returns the modified list of products.

### `remove_products(products)`

- Removes products with a rating below a specified value.
- Returns the modified list of products.

### `save_changes(products)`

- Saves the changes made to the product data back to the XML file.

### `generate_reports(products)`

- Generates a report showing the total number of products and the total price of products in each category.

### `quit(products)`

- Saves changes and exits the program.

### `menu()`

- Displays a menu of options for the user to choose from.
- Calls the corresponding function based on the user's choice.

## Error Handling

- The tool handles FileNotFoundError when the specified XML file is not found.
- It catches exceptions during XML parsing and provides error messages.
- ValueErrors are caught when invalid input is provided by the user.

## Dependencies

- `argparse`: Handles command-line arguments.
- `os`: Provides a way of using operating system-dependent functionality.
- `sys`: Provides access to some variables used or maintained by the interpreter.
- `xml.etree.ElementTree`: Parses XML files.
- `prettytable`: Used for generating formatted tables.

## Limitations

- The tool assumes a well-formed XML structure.
- Error messages are displayed to the console; a more user-friendly interface could be implemented.
- The tool might not handle all possible edge cases.

## Conclusion

The XML Product Data Parser provides a simple yet powerful interface for users to manipulate product data stored in XML files. It offers a range of functionalities to modify and analyze product information efficiently. Users are encouraged to review and modify the tool based on specific requirements and edge cases.
