# File Name : movie_decryption.py
# Student Name: Colton Ramsey, Lucas Iceman, Matthew Boutros, Dylan Sams
# email: ramseyc6@mail.uc.edu, icemanlc@mail.uc.edu, boutromw@mail.uc.edu, samsds@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 05/01/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Use give JSON files to decrypt hidden messages for our team 
# to take a picture with a message at the location assigned to our team
# Brief Description of what this module does: Uses the TeamsAndEncryptedMessagesForDistribution file to decrypt the hidden message for our
# team and find out our assigned movie
# Citations: cryptography.fernet library Chatgpt
# Anything else that's relevant:

import json
from cryptography.fernet import *


class movie_decryption():
    """
    decrypts the hidden message assigned to out team
    """
    def __init__(self, input_file = "Data/TeamsAndEncryptedMessagesForDistribution.json"):
        """
        Storing a path to the encrypted message file
        @Param:None
        @Return:None
        """
        self.file = input_file
        self.team_name = "Jimmy Chitwood"
        self.key = Fernet("GusN5ceicQjGeKNr0gedUkjZ6h4I8xXm6Thx_issRko=")

    def get_encrypt(self):
        """
        retrieves the first encrypted message associated with a specific team from a JSON file
        @Param:None
        @Return:encrypted_data
        """
        with open(self.file, "r") as f:
            encrypted_list = json.load(f)[self.team_name]
            encrypted_data = encrypted_list[0]
        return encrypted_data
    def decrypt_data(self, encrypted_data):
        """
        decrypt an encrypted message using the Fernet encryption key stored in the object.
        @Param:None
        @Return:None
        """
        token = encrypted_data.encode()
        decrypt = self.key.decrypt(token)
        decrypted_movie = decrypt.decode()
        print(decrypted_movie)
        

