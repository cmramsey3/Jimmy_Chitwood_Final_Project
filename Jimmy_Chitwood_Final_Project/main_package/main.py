# File Name : main.py
# Student Name: Colton Ramsey, Lucas Iceman, Matthew Boutros, Dylan Sams
# email: ramseyc6@mail.uc.edu, icemanlc@mail.uc.edu, boutromw@mail.uc.edu, samsds@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 05/01/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Use give JSON files to decrypt hidden messages for our team 
# to take a picture with a message at the location assigned to our team

# Brief Description of what this module does: Main entry point code that will invoke each of the methods that we create
# Citations:
# Anything else that's relevant:

from Utilities.location_decryption import *
from Utilities.movie_decryption import *
from Utilities.image import *

if __name__ == "__main__":

    # Saves path and displays team image at UC Baseball Stadium with our chose movie quote
    team_picture = ImageDisplayer("Data/UC_Baseball_Jimmy_Chitwood.jpeg")
    team_picture.display()
    
    # Decrypts and Prints Location Message
    team_name = "Jimmy Chitwood"
    hints_path = "Data/EncryptedGroupHints Spring 2025.json"
    english_path = "Data/UCEnglish.txt"
    decryptor = LocationDecryptor(team_name, hints_path, english_path)
    location = decryptor.decrypt()
    print(f"Decrypted Location:\n{location}\n")

    # Decrypts and Prints Movie Results
    movieEncryption = movie_decryption()
    encrypted_data = movieEncryption.get_encrypt()
    movieEncryption.decrypt_data(encrypted_data) 