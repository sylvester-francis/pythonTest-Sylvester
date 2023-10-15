from helper import return_args
from file_operations import read_file
from xml_operations import parse_XML
from user_interface import menu


if __name__ == '__main__':
    args = return_args()
    xml_file = read_file(args.filepath)
    if not xml_file:
        print("The specified file path is not found")
    else:
        products = parse_XML(xml_file)
        menu(products)