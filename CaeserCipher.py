alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Encrypt or Decrypt?").lower()
text=input("Enter the text to be encrypted/decrypted: ").lower()
shift=int(input("Enter the shift value: "))

def encrypt(text, shift):
    encoded_text = ""
    for letter in text:
        shifted_position = alphabets.index(letter) + shift
        shifted_position=shifted_position % len(alphabets)
        encoded_text += alphabets[shifted_position]
    print(f"The encrypted text is: {encoded_text}")

def decrypt(text, shift):
    decoded_text = ""
    for letter in text:
        shifted_position = alphabets.index(letter) - shift
        shifted_position=shifted_position % len(alphabets)
        decoded_text += alphabets[shifted_position]
    print(f"The encrypted text is: {decoded_text}")

decrypt(text,shift)
encrypt(text, shift)

