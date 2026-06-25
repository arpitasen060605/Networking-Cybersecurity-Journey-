password= input("Enter a password to analyze:")
COMMON_PASSWORDS = {"password", "password123", "123456", "12345678", "qwerty",
    "abc123", "letmein", "welcome", "admin", "iloveyou",
    "monkey", "dragon", "football", "111111", "123123",
    "sunshine", "princess", "trustno1", "qwerty123", "1q2w3e4r"}
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
is_common = password.lower() in COMMON_PASSWORDS 
score=0
if length>=8:
    score+=1
if length>=12:
    score+=1
if has_upper:
    score+=1
if has_lower:
    score+=1
if has_digit:
    score+=1
if has_symbol:
    score+=1

if is_common:
    score=0

if score<=2:
    strength= "WEAK"
elif score<=4:
    strength= "MEDIUM"
else:
    strength= "STRONG"
print(f"\nPassword length- {length}")
print(f"Has uppercase- {has_upper}")
print(f"Has lowercase- {has_lower}")
print(f"Has digit- {has_digit}")
print(f"Has symbol- {has_symbol}")
print(f"\nScore- {score}/6")
print(f"Strength- {strength}")

if is_common:
    print("This is one of the most commonly used, change it immediately!")





