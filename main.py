from art import logo
from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(text,shift):
  final_text=""
  for ch in text:
    if ch in alphabet:
      position = alphabet.index(ch)
      if direction == "decode":
        new_position = position - shift
      elif direction=="encode":
        new_position = position + shift
      final_text += alphabet[new_position]
    else:
      final_text += ch
  print(f"The {direction}d text is {final_text}")

k="yes"
while k!="no":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26 #the shift value will always be between 0-25
  caesar(text,shift)
  k = input("\nPlease enter 'yes' to continue or 'no' to stop: ")
  clear()

print("Goodbye")