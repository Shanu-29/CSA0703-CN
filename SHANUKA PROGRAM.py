import random

def to_binary(msg):
    return ''.join(format(ord(c), '08b') for c in msg)

def parity_bit(bits):
    return '0' if bits.count('1') % 2 == 0 else '1'

def checksum(msg):
    return sum(ord(c) for c in msg)

def flip_bit(bits):
    bits = list(bits)
    i = random.randint(0, len(bits) - 1)
    bits[i] = '1' if bits[i] == '0' else '0'
    return ''.join(bits)

def to_text(bits):
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

random.seed(1)
messages = ["HELLO", "NETWORK", "PYTHON3", "DATA101", "PACKET!"]

for msg in messages:
    original_bits = to_binary(msg)
    corrupted_bits = flip_bit(original_bits)
    corrupted_msg = to_text(corrupted_bits)

    parity_ok = parity_bit(original_bits) == parity_bit(corrupted_bits)
    checksum_ok = checksum(msg) == checksum(corrupted_msg)

    print(f"\nOriginal: {msg}")
    print(f"Received: {corrupted_msg!r}")
    print(f"Parity check   : {'OK' if parity_ok else 'ERROR DETECTED'}")
    print(f"Checksum check : {'OK' if checksum_ok else 'ERROR DETECTED'}")
