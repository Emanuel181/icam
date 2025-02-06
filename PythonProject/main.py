def decrypt(encf, key):
    decf = b""
    i = 0
    for c in encf:
        if i >= len(key):
            i = 0
        x = (c - key[i]) % 256
        decf += x.to_bytes(1, 'big')
        i += 1
    return decf

def derive_key(encf, plaintext):
    key = []
    for i, c in enumerate(plaintext):
        key_byte = (encf[i] - c) % 256
        key.append(key_byte)
    return key

# Provided encrypted flag and known plaintext
encrypted_flag = b'\x9e\xb5\xd4\xa8\x9c\xef\x98\x8c\x9d\xac\xb7\xabVz\xcf\xbe\xa1\x92\x7f\x86\xd7\x9aj\xac\xddY\x97\xad\x88\xa3mo\xb3\xb1\x88i\xae\xb4\xa6\x9bm\xb2\xae\x8aj\xb1\x85\xa8\x99\x9b\xb1\xddXh\x82\xb1\xd4\x9b\x9b\xaf\xab\x89h\x84\xb6\xa2\x9b\x98\xab\xdbYf\x82\x89\xaafm\xb2\xaaVf\xc8'
known_plaintext = b"Secret flag"

# Derive the key from the known plaintext
key = derive_key(encrypted_flag[:len(known_plaintext)], known_plaintext)

# Decrypt the entire flag using the derived key
decrypted_flag = decrypt(encrypted_flag, key)

print("Key:", key)
print("Decrypted flag:", decrypted_flag.decode())
