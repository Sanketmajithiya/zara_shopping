"""
Exception handling in Python is a mechanism to deal with errors that occur during program execution. It allows you to handle both expected and unexpected errors gracefully, preventing your program from crashing.

try: This is the block of code where you anticipate an error might occur. You place the code that you want to monitor inside the try block.

except: This block is executed if an exception occurs within the corresponding try block. You can specify the type of exception to catch, or you can catch all exceptions by using a generic except block.

else: This block is executed if no exceptions occur in the try block. It is optional.

finally: This block is always executed, regardless of whether an exception occurred or not. It is useful for cleaning up resources, such as closing files or releasing locks. It is also optional.
"""