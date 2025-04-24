# File Name : image.py
# Student Name: Colton Ramsey, Lucas Iceman, Matthew Boutros, Dylan Sams
# email: ramseyc6@mail.uc.edu, icemanlc@mail.uc.edu, boutromw@mail.uc.edu, samsds@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 05/01/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Use give JSON files to decrypt hidden messages for our team 
# to take a picture with a message at the location assigned to our team

# Brief Description of what this module does: This module will hold the methods that will load and display our team
# image in the console window
# Citations:
# Anything else that's relevant:

import matplotlib.pyplot as plt
from PIL import Image 

class ImageDisplayer:
    def __init__(self, image_path):
        self.image_path = image_path

    def display(self):
        img = Image.open(self.image_path)
        plt.imshow(img)
        plt.axis('off')
        plt.title("Group Photo")
        plt.show()