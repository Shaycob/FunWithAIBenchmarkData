# File Name: visualization.py
# Student Name: Daquan Daniels 
# email: Danieldu@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This module visualizes the answer distribution
# from a CSV file related to the MMLU management test.

# Brief Description of what this module does: It reads a CSV file, extracts the answers,
# counts their occurrences, and generates a bar chart to display the distribution.
# Citations: www.chatgpt.com & gemini.google.com
# Anything else that's relevant:

import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

def show_answer_distribution(csv_file_path):
    """
    Reads a CSV file, extracts answer choices, and generates a bar chart.

    Args:
        csv_file_path (str): The path to the CSV file.
    """
    try:
        # Load the CSV file without headers
        df = pd.read_csv(csv_file_path, header=None)

        # Extract answers from the last column, removing NaN values
        answers = df.iloc[:, -1].dropna().tolist()

        # Count occurrences of each answer choice
        answer_counts = Counter(answers)

        # Check if there are any answers
        if not answer_counts:
            print("No answers found in the dataset.")
            return

        # Prepare data for visualization
        labels, values = zip(*answer_counts.items())

        # Plot the bar chart
        plt.figure(figsize=(10, 6)) # Increased figure size for better readability
        plt.bar(labels, values, color='skyblue', alpha=0.8) # Changed color and alpha
        plt.xlabel('Answer Choices', fontsize=12) # Increased font size
        plt.ylabel('Frequency', fontsize=12)
        plt.title('Answer Distribution in Management Test', fontsize=14)
        plt.xticks(rotation=45, ha='right') # Rotated x-axis labels for better fit
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout() # Adjusts plot parameters for a tight layout
        plt.show()

    except FileNotFoundError:
        print(f"Error: File not found at {csv_file_path}")
    except pd.errors.EmptyDataError:
        print(f"Error: The CSV file at {csv_file_path} is empty.")
    except Exception as e:
        print(f"Error generating visualization: {e}")