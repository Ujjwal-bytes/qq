
p = 23 
g = 5   

a = 8
b = 15
A = (g**a) % p 
B = (g**b) % p  

print("Alice Public Key:", A)
print("Bob Public Key:", B)

alice_secret = (B**a) % p
bob_secret = (A**b) % p

print("Alice Secret Key:", alice_secret)
print("Bob Secret Key:", bob_secret)

if alice_secret == bob_secret:
    print("Key Exchange Successful!")
    print("Shared Secret Key =", alice_secret)
else:
    print("Key Exchange Failed")
