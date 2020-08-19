import random
import string

class PasswordGenerator:
    def __init__(self, number_characters, has_numbers, has_uppercase, has_lowercase):
        self.number_characters = number_characters
        self.has_numbers = has_numbers
        self.has_uppercase = has_uppercase
        self.has_lowercase = has_lowercase

    def list_password_features(self):
        features = []

        if self.has_numbers:
            numbers = [str(number) for number in range(0, 10)]
            features.append(numbers)

        if self.has_uppercase or self.has_lowercase:

            if self.has_uppercase:
                uppercase = string.ascii_uppercase
                features.append(uppercase)

            if self.has_lowercase:
                lowercase = string.ascii_lowercase
                features.append(lowercase)

        return features

    def generate_password(self):
        features = self.list_password_features()
        
        if len(features) == 0:
            return "Choose an option!"

        if self.number_characters <= 0:
            return "Choose a valid length!"

        if self.number_characters > 100:
            return "Choose a smaller length!"

        chose_features = []

        # Keeps generating passwords until it has all the wanted features
        
        while True:
            password = ""

            for i in range(self.number_characters):
                feature = random.choice(features)
                chose_char = random.choice(feature)
                password += chose_char

                if feature not in chose_features:
                    chose_features.append(feature)

            if len(features) == len(chose_features):
                break
            
        return password