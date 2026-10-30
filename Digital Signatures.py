import hashlib
import hmac

def create_hash(message):
    hash_value = hashlib.sha256(message.encode()).hexdigest()
    return hash_value
def hash_to_integer(message, n):
    hash_hex = create_hash(message)
    hash_int = int(hash_hex, 16)
    return hash_int % n

def generate_signature(message, private_key, n):
    message_hash = hash_to_integer(message, n)
    signature = pow(message_hash, private_key, n)
    return signature
def verify_signature(message, signature, public_key, n):
    message_hash = hash_to_integer(message, n)
    verified_hash = pow(signature, public_key, n)
    if hmac.compare_digest(str(message_hash), str(verified_hash)):
        return True
    else:
        return False

p = 61 
q = 53  
n = p * q 
phi = (p - 1) * (q - 1) 
d = 2753

print("Public Key  :", e, n)
print("Private Key :", d, n)

message = input("Enter the message: ")
signature = generate_signature(message, d, n)
print("\nDigital Signature:")
print(signature)
print("\n---- Signature Verification ----")
received_message = input("Enter received message: ")
received_signature = int(input("Enter received signature: "))

if verify_signature(received_message, received_signature, e, n):
    print("Signature Verified Successfully.")
    print("Message integrity and authenticity are confirmed.")
else:
    print("Signature Verification Failed.")
    print("Message may be modified or signature is invalid.")
