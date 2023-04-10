import math
p = 3
q = 7
n = p*q
print("n =", n)
phi = (p-1)*(q-1)
e = 2
while(e<phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1
print("e =", e)
d = y = pow(e, -1, phi)
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
msg = 11
print(f'Original message:{msg}')
C = pow(msg, e,n)
print(f'Encrypted message: {C}')
print(pow(C,d,n))
