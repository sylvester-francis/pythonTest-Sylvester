# tests/__init__.py
import os
import sys

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))
project_path = os.path.join(script_dir, '..')  
sys.path.append(project_path)
print(sys.path)