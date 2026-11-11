print("=== PASSWORD VALIDATOR ===")

while True:
  password = input("\nEnter a password: ")

  upper = False
  lower = False
  number = False
  
  for char in password:
      if char >= "A" and char <= "Z":
          upper = True
      if char >= "a" and char <= "z":
          lower = True
      if char >= "0" and char <= "9":
          number = True
  valid = True

  if len(password) < 8:
    print("Password must contain at least 8 charecters.")
    valid = False 
