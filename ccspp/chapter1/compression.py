#!/usr/bin/env python3

from sys import getsizeof

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for n in gene.upper():
            self.bit_string <<= 2
            if n == 'A':
                self.bit_string |= 0b00
            elif n == 'C':
                self.bit_string |= 0b01
            elif n == 'G':
                self.bit_string |= 0b10
            elif n == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid nucleotide: {}".format(n))

    def _decompress(self) -> str:
        gene: str = ''
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            b: int = self.bit_string >> i & 0b11
            if b == 0b00:
                gene += 'A'
            elif b == 0b01:
                gene += 'C'
            elif b == 0b10:
                gene += 'G'
            elif b == 0b11:
                gene += 'T'
            else:
                raise ValueError("Invalid bits: {}".format(b))
        return gene[::-1]

    def __str__(self) -> str:
        return self._decompress()

if __name__ == "__main__":
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("Original string is {} bytes".format(getsizeof(original)))

    compressed: CompressedGene = CompressedGene(original)
    print("Compressed string is {} bytes".format(getsizeof(compressed)))

    print(compressed)
    print("Original and (de)compressed are the same: {}".format(original == compressed._decompress()))


