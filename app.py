from flask import Flask, render_template, request
from huffman_backend import generate_huffman_tree, encode_text, calculate_storage_size, plot_frequency
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    encoded_text = ""
    storage_size = 0
    plot_path = ""
    if request.method == "POST":
        text = request.form["text"]
        
        # Generate Huffman tree and code
        freq_dict, huffman_code = generate_huffman_tree(text)
        encoded_text = encode_text(text, huffman_code)
        storage_size = calculate_storage_size(encoded_text)
        
        # Plot frequency
        plot_path = plot_frequency(freq_dict)
    
    return render_template("index.html", encoded_text=encoded_text, storage_size=storage_size, plot_path=plot_path)

if __name__ == "__main__":
    app.run(debug=True)
