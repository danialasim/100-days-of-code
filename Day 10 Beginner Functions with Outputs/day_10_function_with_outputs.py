# Day 10 - Functions with Outputs
# This file demonstrates different ways functions can handle outputs

#--------------------
# Print-based Output
#--------------------

def format_name(f_name, l_name):
    """
    Format and print a full name without returning any value.
    
    Args:
        f_name (str): First name
        l_name (str): Last name
    """
    formated_f_name = f_name.title()  # Convert to title case
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

# Example usage of print-based function
format_name("angela", "JAKE")

#--------------------
# Return-based Output
#--------------------

def new_format_name(f_name, l_name):
    """
    Format a full name and return it as a string.
    
    Args:
        f_name (str): First name
        l_name (str): Last name
        
    Returns:
        str: Formatted full name or error message
    """
    # Input validation with early return
    if f_name == "" or l_name == "":
        return "You didn't provide any valid input."
    
    # Process the names
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    # Return the formatted string
    return f"{formated_f_name} {formated_l_name}"

# Example usage of return-based function
print(new_format_name(
    input("What is your first name? "), 
    input("What is your last name? ")
))