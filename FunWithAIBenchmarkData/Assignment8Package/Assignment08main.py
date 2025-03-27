# File Name : Assignment8_main.py
# Student Name: Jacob Farrell & Daquan Daniels 
# email:  farrelcj@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment was a collaborative assignment
# that used functions to demonstrate a visual image and a function that visualizes
# data. 

# Brief Description of what this module does: This module calls the functions
# display_team_image and show_answer_distribution and executes them.
# Citations: Chatgpt
# Anything else that's relevant:

from Assignment8Package.visualization import show_answer_distribution
from Assignment8Package.display_image import display_team_image
from utilitiesPackage.CSV_Utilities import MMLU_CSV_Processor

# Get the data
CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv"])
questions = CSV_Processor.read_data()

# Show team image
display_team_image("gloom.png")

# Show chart
file_path = "dataPackage/MMLU/data/management_test.csv"  #   Explicitly define file_path
print("Type of file_path:", type(file_path))  #   Debugging line 1
print("Value of file_path:", file_path)  #   Debugging line 2
show_answer_distribution(file_path)