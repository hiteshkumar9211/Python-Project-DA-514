import heapq
from collections import Counter
import matplotlib.pyplot as plt
import os

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # Ensure nodes are comparable by frequency for heapq
    def __lt__(self, other):
        return self.freq < other.freq

def generate_huffman_tree(text):
    # Remove spaces from the text
    text = text.replace(" ", "")
    freq_dict = Counter(text)
    
    # Initialize a min-heap with nodes for each character
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    # Generate Huffman codes
    huffman_code = {}
    build_huffman_code(heap[0], "", huffman_code)
    return freq_dict, huffman_code

def build_huffman_code(node, current_code, huffman_code):
    if node.char is not None:
        huffman_code[node.char] = current_code
    else:
        build_huffman_code(node.left, current_code + "0", huffman_code)
        build_huffman_code(node.right, current_code + "1", huffman_code)

def encode_text(text, huffman_code):
    text = text.replace(" ", "")
    return ''.join(huffman_code[char] for char in text)

def calculate_storage_size(encoded_text):
    return len(encoded_text) / 8  # Each bit is 1/8 byte

def plot_frequency(freq_dict):
    plt.figure(figsize=(10, 5))
    plt.bar(freq_dict.keys(), freq_dict.values(), color="skyblue")
    plt.xlabel('Characters')
    plt.ylabel('Frequency')
    plt.title('Character Frequency')
    plot_path = 'static/frequency_plot.png'
    plt.savefig(plot_path)
    plt.close()
    return plot_path
