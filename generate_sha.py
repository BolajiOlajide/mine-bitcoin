from hashlib import sha256

text = 'ABC'
print(sha256(text.encode('ascii')).hexdigest())