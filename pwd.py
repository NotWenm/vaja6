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
          upper = True
          
