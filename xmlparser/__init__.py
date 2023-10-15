# xml_parser/__init__.py
import os,sys 
# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))
# Add the relative path to the xmlparser directory to sys.path
project_path = os.path.join(script_dir, 'xmlparser')
sys.path.append(project_path)
