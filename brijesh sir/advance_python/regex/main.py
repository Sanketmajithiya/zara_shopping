import re


# print("brijesh gondaliya")
# print(r"brijesh go\ndaliya")

# txt = "The rain in Spain"

# x = re.findall('ai', txt)


# data = "map mat mob moon master mam m mm mmm mmmm fat"

# # x = re.findall(r'\bm\w+\b', data)
# x = re.findall(r'\bm\w{3}\b', data)
# print(x)


# dob = "23-12-1996 1-12-1996"
# x = re.findall(r'\b\d{1,2}-\d{1,2}-\d{4}\b', dob)
# print(x)

# email = "brijesh.gondaliya07@gmail.com"
# x = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
# print(x.group())

# email = "brijesh.gondaliya07@gmail.com"
# x = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
# print(x.group())

# data = "this is a php language."
# x = re.sub("php", "python", data)
# print(x)



import re

def is_valid_email(email):
    """
    Check if the given email address is valid.
    
    Args:
    email (str): The email address to be checked.
    
    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(pattern, email))

# Test the function
email = "brijesh."
print(is_valid_email(email))  # Output: True
