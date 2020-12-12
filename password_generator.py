import random
import string

class PasswordGenerator:
    def __init__(self, number_of_chars, has_digits, has_uppercase, has_lowercase, has_special_chars):
        self.number_of_chars = number_of_chars
        self.has_digits = has_digits
        self.has_uppercase = has_uppercase
        self.has_lowercase = has_lowercase
        self.has_special_chars = has_special_chars

    def list_password_features(self):
        chosen_features_by_user = []

        if self.has_digits:
            digits = string.digits
            chosen_features_by_user.append(digits)

        if self.has_uppercase:
            uppercase_letters = string.ascii_uppercase
            chosen_features_by_user.append(uppercase_letters)

        if self.has_lowercase:
            lowercase_letters = string.ascii_lowercase
            chosen_features_by_user.append(lowercase_letters)

        if self.has_special_chars:
            special_chars = string.punctuation
            chosen_features_by_user.append(special_chars)

        return chosen_features_by_user

    def generate_password(self):
        chosen_features_by_user = self.list_password_features()
        
        if len(chosen_features_by_user) == 0:
            return "Choose at least one feature!"

        if self.number_of_chars <= 0:
            return "Choose a valid length!"

        if self.number_of_chars > 100:
            return "Choose a smaller length!"

        # Keeps generating passwords until it has all the wanted features
        
        while True:
            random_generated_password = ""
            features_used_in_password_generation = []

            for i in range(self.number_of_chars):
                random_chosen_feature = random.choice(chosen_features_by_user)
                random_chosen_char = random.choice(random_chosen_feature)
                random_generated_password += random_chosen_char

                if random_chosen_feature not in features_used_in_password_generation:
                    features_used_in_password_generation.append(random_chosen_feature)

            if len(chosen_features_by_user) == len(features_used_in_password_generation):
                break
            
        return random_generated_password