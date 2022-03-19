
from cryptography.fernet import Fernet
from tangled_up_in_unicode import uppercase

class Cryptography:
    
    def key_generator(self):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    def read_key(self):
        with open("secret.key", "rb") as key_reader:
            return key_reader.read()

    def encrypt_msg(self,message):

        key = self.read_key()
        encoded_message = message.encode()
        f = Fernet(key = key)
        encrypted_message = f.encrypt(encoded_message)
        return encrypted_message

    def decrypt_msg(self,encrypted_message):
    
        key = self.read_key()
        f = Fernet(key = key)
        decrypted_message = f.decrypt(encrypted_message)
        return decrypted_message


if __name__ == "__main__":
    
    again_run = "yes"
    while again_run == "yes":

        text = input("\nEnter Your Message to encrypt it: ")
        crypto = Cryptography()
        crypto.key_generator()
        encrypted_msg = crypto.encrypt_msg(message= text)
        decrypted_msg = crypto.decrypt_msg(encrypted_message= encrypted_msg)

        print("\n The encrypted message is = ", encrypted_msg,"/n")
        print(" The decrypted messgae is = ", decrypted_msg)

        again_run = input("\n If your want to run again type 'Yes' else any key to exit: ").lower()

print("\nThanks For Using......")