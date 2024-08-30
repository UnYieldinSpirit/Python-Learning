def is_leap_year(year):
    """Function that takes in years and tests to see 
    whether they are leap years or not."""
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
    
year = int(input("What year would you like to test? "))

print(f"Result for the year {year}: {is_leap_year(year)}")