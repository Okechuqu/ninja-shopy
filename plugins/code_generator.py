import random
import string

# from users.models.users import CustomUser


def generate_unique_ID():
    # Generate 6 random numbers
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(6))
    # Generate 3 random capital alphabets
    random_alphabets = ''.join(random.choice(
        string.ascii_uppercase) for _ in range(3))
    # Combine numbers and alphabets with a hyphen
    unique_id = f"{random_numbers}-{random_alphabets}"
    return unique_id

    # if not CustomUser.objects.filter(code=unique_id).exists():
    #         return unique_id
    # else:
    #     return generateUniqueId()
