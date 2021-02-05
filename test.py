hash = '0000000000000000000'
hash2 = '000000000000000000041f844be9e58bde6069a52d80eba5821e3e02d5742488'
print(len(hash2))

total = 0

for char in hash2:
    if char == '0':
        total += 1
    else:
        break
print(total, 'zertos in hash')
