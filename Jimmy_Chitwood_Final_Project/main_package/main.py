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

from Utilities.location_decryption import LocationDecryptor
from Utilities.movie_decryption import MovieDecryptor
from Utilities.image import ImageDisplayer

class FinalProjectRunner:
    def __init__(self, team_name):
        self.team_name = team_name
        self.hints_path = "Data/EncryptedGroupHints Spring 2025.json"
        self.english_path = "Data/UCEnglish.txt"
        self.encrypted_movie_path = "Data/TeamsAndEncryptedMessagesForDistribution.json"
        self.image_path = "Data/group_photo.jpg"  # Make sure this exists
        self.fernet_key = None  # Set this when available

    def run_location_decryption(self):
        decryptor = LocationDecryptor(self.team_name, self.hints_path, self.english_path)
        location = decryptor.decrypt()
        print(f"Decrypted Location:\n{location}\n")

    def run_movie_decryption(self):
        if not self.fernet_key:
            print("Fernet key not provided. Skipping movie decryption.")
            return
        decryptor = MovieDecryptor(self.team_name, self.encrypted_movie_path, self.fernet_key)
        movie = decryptor.decrypt()
        print(f"Decrypted Movie Title:\n{movie}\n")

    def show_group_photo(self):
        displayer = ImageDisplayer(self.image_path)
        displayer.display()

    def run_all(self):
        self.run_location_decryption()
        # Uncomment these when ready
        # self.run_movie_decryption()
        # self.show_group_photo()


if __name__ == "__main__":
    runner = FinalProjectRunner(team_name="Jimmy Chitwood")
    # runner.fernet_key = b"YOUR_KEY_HERE"  # Set this when you have the key
    runner.run_all()
