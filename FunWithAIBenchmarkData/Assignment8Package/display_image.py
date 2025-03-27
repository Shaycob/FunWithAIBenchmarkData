# File Name : display_image.py
# Student Name: Jacob Farrell
# email:  farrelcj@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment was a colborative assignment
# that used functions to demonstrate a visual image and a function that visualed
# data. 

# Brief Description of what this module does: This builds the function display_team_image
# locates the gloom.png file, resizes it, and displays it upon execution.
# Citations: Chatgpt
# Anything else that's relevant:

from PIL import Image

def display_team_image(image_path="gloom.png"):
    """
    Display a 200x200 image representing the team.
    """
    try:
        img = Image.open(image_path)
        img = img.resize((200, 200))
        img.show()
    except Exception as e:
        print(f"Error displaying image: {e}")