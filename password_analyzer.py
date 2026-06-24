password= input("Enter a password to analyze:")
length= len(password)
has_upper= False
has_lower= False
has_digit= False
has_symbol= False
for char in password:
    if char.isupper():
        has_upper= True
    elif char.islower():
        has_lower= True
    elif char.isdigit():
        has_digit= True
    else:
        has_symbol= True
print(f"\nPassword length- {length}")
print(f"Has uppercase- {has_upper}")
print(f"Has lowercase- {has_lower}")
print(f"Has digit- {has_digit}")
print(f"Has symbol- {has_symbol}")