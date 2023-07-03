import sys
import os

# Get the path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path of the project directory (assuming the module is in the project root)
project_dir = os.path.dirname(current_dir)

# Add the project directory to sys.path
sys.path.append(project_dir)
