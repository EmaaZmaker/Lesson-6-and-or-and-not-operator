char = input("Enter a character: ")
is_alphabet = False
if 'a' <= char <= 'z':
    is_alphabet = True
if is_alphabet:
    print(f"The character '{char}' is an alphabet.")
else:
    print(f"The character '{char}' is not an alphabet.")

