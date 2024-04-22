def forgot_():
    email = input("Enter your email: ")
    import random
    otp = random.randint(1111,9999)
    return email, otp, "Password Changed."