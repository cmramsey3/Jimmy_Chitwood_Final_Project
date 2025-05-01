# File Name : location_decryption.py
# Student Name: Colton Ramsey, Lucas Iceman, Matthew Boutros, Dylan Sams
# email: ramseyc6@mail.uc.edu, icemanlc@mail.uc.edu, boutromw@mail.uc.edu, samsds@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 05/01/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Use give JSON files to decrypt hidden messages for our team 
# to take a picture with a message at the location assigned to our team
# Brief Description of what this module does: Uses the files give to decrypt the location where our team should take our picture
# Uses the UCEnglish text file and the EncryptedGroupHints JSON File
# Citations:ChatGpt
# Anything else that's relevant: 
# Our team name is a key in the dictionary and we use it to match the numbers to words in the txt file to come up with our location

import json

class LocationDecryptor:
    """
    A utility class to decrypt campus location data for a project team.
    It uses 0-based indexing into the English word list provided.

    Attributes:
        team_name (str): The name of the team whose location is to be decrypted.
        hints_path (str): Path to the EncryptedGroupHints JSON file.
        english_path (str): Path to the UCEnglish.txt file.
    """
    def __init__(self, team_name, hints_path, english_path):
        self.team_name = team_name
        self.hints_path = hints_path
        self.english_path = english_path

    def decrypt(self):
        """Returns the decrypted location string."""
        with open(self.hints_path, "r") as f:
            encrypted_data = json.load(f)[self.team_name]

        with open(self.english_path, "r") as f:
            words = f.readlines()

        # Use 0-based indexing (DO NOT subtract 1)
        decrypted_words = [words[int(index)].strip() for index in encrypted_data]
        return " ".join(decrypted_words)
