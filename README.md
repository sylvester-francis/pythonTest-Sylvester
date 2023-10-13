# pythonTestSolution-Sylvester

## Objective:
Create a Python tool that can parse an XML file containing product data, manipulate the data, save the results back into XML format, and generate reports.

## Instructions:

### Data Parsing:
- Load and parse the provided XML file.
- Extract relevant product data.

### Data Manipulation:
- Increase the price of products in a specific category by a user-defined percentage.
- Rename a specific category.
- Remove products below a user-defined rating.

### Saving the Changes:
- After making changes, save the updated data back to an XML file.

### User Interface:
- Design a simple CLI (Command Line Interface) for the user to input their choices and provide necessary information.

## Requirements:
- Implement basic error handling for invalid requests.
- Write unit tests covering the main functionality.
- Generate a report to display the total products by category and total price by category.


## Sample XML Data:
```xml
<products>
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
</products>
```
