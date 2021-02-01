from hashlib import sha256
import time


MAX_NONCE = 100

def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros

    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)

        if new_hash.startswith(prefix_str):
            print(f'Yay! Successfully mined bitcoins with nonce value:{nonce}')
            return new_hash

    raise BaseException('Omo! E be things.')


if __name__ == '__main__':
    transactions = '''
    Dhaval->Bhavin->20,
    Mando->Cara->45
'''

    prev_hash = '000000000000000000041f844be9e58bde6069a52d80eba5821e3e02d5742488'
    difficulty = 20
    start = time.time()
    print('start mining')
    new_hash = mine(5, transactions, prev_hash, difficulty)
    total_time = str((time.time() - start))
    print(f'End mining. Mining took: {total_time} seconds.')
    print(SHA256('ABC'))