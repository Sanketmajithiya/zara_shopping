"""
In Python, an identifier is a name used to identify a variable, function, class, module, or any other object. It is essentially a user-defined name for a program entity. Identifiers follow certain rules and conventions in Python:

Identifiers cannot be a keyword.
Example : for = 40 - False, price = 40 - True

Identifiers are case-sensitive.
Example : Name, name, NAME

It can have a sequence of letters[a-z,A-Z] and digits[0-9]. However, it must begin with a letter or _. 
Example : 1_level - False, level_1 -True

The first letter of an identifier cannot be a digit.

It's a convention to start an identifier with a letter rather _.
Example _level_1 = 1 - True

Whitespaces are not allowed.
Example First name - False, first_name, FirstName, Firstname

We cannot use special symbols like !, @, #, $, and so on.
@tops, #tops - False

Valid Examples:
---------------
variable_name
_internal_variable
myFunction
Class_Name
module_name


Invalid Examples:
-----------------
3variable (starts with a digit)
my-variable (contains a hyphen)
if (uses a reserved keyword)
class (uses a reserved keyword)

Conventions:

Pascal Case:

Typically used for naming classes and, in some cases, modules.
Example: MyClass, MyModule, MyFunction
Camel Case:

Commonly used for naming variables, functions, and sometimes methods.
Example: myVariable, myFunction, calculateTotal
Snake Case:

Frequently used for naming variables and functions in languages where underscores are preferred over camel case.
Example: my_variable, calculate_total, function_name

snake_case : first_name
camelCase :  firstName
PascalCase : FirstName

"""

