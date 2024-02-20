import streamlit as st

st.header("Caesar Cipher")

text = st.text_input("Enter the text:")
shift_keys_input = st.text_input("Enter the shift keys separated by spaces:")
if shift_keys_input:
    shift_keys = list(map(int, shift_keys_input.split()))

if st.button("Submit"):
        def encrypt_decrypt(text, shift_keys, ifdecrypt):
            """
            Encrypts or decrypts a text using Caesar Cipher with a list of shift keys.
            Args:
                text: The text to encrypt or decrypt.
                shift_keys: A list of integers representing the shift values for each character.
                ifdecrypt: Flag to indicate whether to decrypt or encrypt.
            Returns:
                A string containing the encrypted text if encrypting, or plain text if decrypting.
            """
            result = ""

            assert 1 < len(shift_keys) <= len(text)

            for i, char in enumerate(text):
                shift_key = shift_keys[i % len(shift_keys)]
                if 32 <= ord(char) <= 125:
                    if ifdecrypt:
                        asc = ord(char) - shift_key
                    else:
                        asc = ord(char) + shift_key
                    while asc > 125:
                        asc -= 94
                    while asc < 32:
                        asc += 94
                    result += chr(asc)
                else:
                    result +=char
                st.write(f"{i} {char} {shift_key} {result[i]}") 

            return result

        enc = encrypt_decrypt(text, shift_keys, False)
        st.write("----------")
        dec = encrypt_decrypt(enc, shift_keys, True)  
        st.write("----------")
        st.write("Text:", text)
        st.write("Shift keys:", *shift_keys)
        st.write("Cipher:", enc)
        st.write("Decrypted text:", dec)
        st.snow()

