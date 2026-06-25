import math
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
pool_size=0
if has_lower:
    pool_size+=26
if has_upper:
    pool_size+=26
if has_digit:
    pool_size+=10
if has_symbol:
    pool_size+=32
combinations= pool_size**length
guesses_per_second= 1_000_000_000
seconds_to_crack= combinations/guesses_per_second
def format_crack_time(seconds):
    if seconds<1:
        return "Instantly"
    elif seconds<60:
        return f"{seconds:.1f} seconds"
    elif seconds<3600:
        return f"{seconds/60:.1f} minutes"
    elif seconds< 86400:
        return f"{seconds/3600:.1f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.1f} days"
    else:
        years = seconds/31536000
        if years > 1e6:
            return f"{years:.2e} years"
        return f"{years:.1f} years"
crack_time = format_crack_time(seconds_to_crack)
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
print(f"Estimated crack time: {crack_time}")
if is_common:
    print("This is one of the most commonly used, change it immediately!")





