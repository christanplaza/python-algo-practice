def decrypt(ciphertext, k1, k2):
  """
  Decrypts an encrypted string without splitting it using a space character.

  Args:
    ciphertext: The encrypted string.
    k1: The amount to shift the first letter.
    k2: The amount to shift the second letter.

  Returns:
    The decrypted string.
  """

  # Get the length of the ciphertext.
  ciphertext_length = len(ciphertext)

  # Declare a variable to store the plaintext.
  plaintext = ""

  # Iterate over the ciphertext in pairs of characters.
  for i in range(0, ciphertext_length, 2):

    # Decrypt the first character in the pair.
    plaintext += chr(ord(ciphertext[i]) - k1)

    # Decrypt the second character in the pair.
    plaintext += chr(ord(ciphertext[i + 1]) - k2)

  # Return the decrypted string.
  return plaintext

if __name__ == "__main__":
    ciphertext = "wajwnsglkajoglrwaxwnjoin"
    k1 = 12
    k2 = 17

    plaintext = decrypt(ciphertext, k1, k2)

    print(plaintext)