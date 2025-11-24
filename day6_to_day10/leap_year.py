"""Write a program that returns True or False 
whether if a given year is a leap year."""
"""Use docstring to explain yout code"""



def is_leap_year(year):
    """Take a year and it return 'True' for Leap Years and 'False'
    for not Leap Years"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

leapyear = is_leap_year(2000)
print(leapyear)
