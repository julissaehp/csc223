import heapq
import os
from collections import defaultdict, Counter

class Node: # Creates the node with a character and a frequency.
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):# This compares two different nodes by their freequencies to put it in the list
        return self.freq < other.freq

def build_huffman_tree(text):# takes in the text 
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]# builds the list of nodes
    heapq.heapify(heap) # makes it a heap 

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, code="", codes={}):
    if node:# makes the codes recursivley and stores it in a dictionary
        if node.char:
            codes[node.char] = code
        generate_codes(node.left, code + "0", codes)
        generate_codes(node.right, code + "1", codes)
    return codes

def huffman_encoding(text):
    if not text:
        return "", {}

    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = ''.join(codes[char] for char in text)

    return encoded_text, codes

def huffman_decoding(encoded_text, codes):
    if not encoded_text:
        return ""

    reverse_codes = {code: char for char, code in codes.items()}
    decoded_text = ""
    code = ""
    for bit in encoded_text:
        code += bit
        if code in reverse_codes:
            decoded_text += reverse_codes[code]
            code = ""

    return decoded_text



input_file = "Alice_Wonderland.txt"
text = open(input_file, 'r').read().rstrip()
encoded_text, codes = huffman_encoding(text)
print("Encoded text:", encoded_text)
print("Codes:", codes)

decoded_text = huffman_decoding(encoded_text, codes)
print("Decoded text:", decoded_text)





