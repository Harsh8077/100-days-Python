from string import ascii_letters
alphabet = ascii_letters

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 0b,dPPYba,  
a0"     "" ""     `Y0 a0P_____00 I0[    "" ""     `Y0 00P'   "Y0  
0b         ,adPPPPP00 0PP"""""""  `"Y0ba,  ,adPPPPP00 00          
"0a,   ,aa 00,    ,00 "0b,   ,aa aa    ]0I 00,    ,00 00          
 `"Ybbd0"' `"0bbdP"Y0  `"Ybbd0"' `"YbbdP"' `"0bbdP"Y0 00   
            00             00                                 
           ""             00                                 
                          00                                 
 ,adPPYba, 00 0b,dPPYba,  00,dPPYba,   ,adPPYba, 0b,dPPYba,  
a0"     "" 00 00P'    "0a 00P'    "0a a0P_____00 00P'   "Y0 
0b         00 00       d0 00       00 0PP""""""" 00          
"0a,   ,aa 00 00b,   ,a0" 00       00 "0b,   ,aa 00          
 `"Ybbd0"' 00 00`YbbdP"'  00       00  `"Ybbd0"' 00          
              00                                             
              00           
"""
print(logo)

def caesar(text,shift,direction):

  def encrypt(text=text , shift = shift):
    cipher_text = ""
    for i in text:
      position = alphabet.index(i)
      new_position = position + shift
      new_letter = alphabet[new_position]
      cipher_text+= new_letter
    print(f"The encoded text is :{cipher_text}")
  
  
  def decrypt(text = text, shift = shift):
    decoded_text = ""
    for i in text:
      position = alphabet.index(i)
      new_position = position - shift
      new_letter = alphabet[new_position]
      decoded_text+= new_letter
    print(f"The decoded text is :{decoded_text}")
  
  if direction == 'encode':
    encrypt(text,shift)
  elif direction == 'decode':
    decrypt(text,shift)

continious = True
while continious:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(text,shift,direction)
  res = input("Type 'yes' if you want to go again , else type 'no' to terminate the program\n")
  if res == 'no':
    continious = False
    print("GoodBye!")
  
