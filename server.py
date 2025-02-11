from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS
@app.route('/')
def home():
    return "Server is running! Use /encrypt for POST requests."


@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']

    # Simple encryption simulation (Caesar cipher)
    ciphertext = ''.join([chr(((ord(char) - 65 + key) % 26) + 65) if char.isalpha() else char for char in plaintext])
    decrypted_text = plaintext

    # Simulated 3D protein folding structure
    folded_structure = [
        {"residue": "A", "location": "core", "x": 0, "y": 0, "z": 0},
        {"residue": "B", "location": "surface", "x": 1, "y": 2, "z": 1},
        {"residue": "C", "location": "core", "x": 2, "y": 1, "z": -1},
        {"residue": "D", "location": "core", "x": 3, "y": 0, "z": 2},
        {"residue": "E", "location": "surface", "x": 4, "y": 2, "z": -2},
    ]

    return jsonify({
        "ciphertext": ciphertext,
        "decrypted_text": decrypted_text,
        "folded_structure": folded_structure
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

