#!/usr/bin/env python3

from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    ob: bytes = original.encode()
    key1: int = random_key(len(ob))
    key2: int = int.from_bytes(ob, "big")
    encrypted: int = key2 ^ key1
    return key1, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == '__main__':
    dummy, crypt = encrypt("One-time pad!")
    result: str = decrypt(dummy, crypt)
    print(result)
