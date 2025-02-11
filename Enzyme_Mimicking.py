import hashlib


# ------------------------
# Algorithm 1: Enzyme-Mimicking Cryptographic System
# ------------------------

def enzyme_encrypt(plaintext, key):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted += char  # Non-alphabetic characters remain unchanged
    return encrypted


def enzyme_decrypt(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted += char
    return decrypted


# ------------------------
# Algorithm 2: Protein Folding as a Cryptographic Hash Function
# ------------------------

# Convert plaintext to "residues" mapped from characters
def to_residues(message):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    residues = [amino_acids[ord(char) % 20] for char in message]
    return residues


# Simulate folding process based on simple rules
def fold_protein(residues):
    folded_structure = []
    for i, residue in enumerate(residues):
        # Alternate residues between 'core' and 'surface'
        if i % 2 == 0:
            folded_structure.append(f"{residue}(core)")
        else:
            folded_structure.append(f"{residue}(surface)")
    return folded_structure


# Generate SHA-256 hash from folded structure
def protein_hash(message):
    residues = to_residues(message)
    folded_structure = fold_protein(residues)
    folded_string = "".join(folded_structure)

    # Compute SHA-256 hash
    hash_object = hashlib.sha256(folded_string.encode())
    return hash_object.hexdigest()


# ------------------------
# Demonstration
# ------------------------

def main():
    # Input message and key for enzyme encryption

    plaintext = "HELLOCRYPTOWORLD"
    key = 3  # Enzyme (key) for encryption

    # Step 1: Encrypt the plaintext using enzyme-like encryption
    print("----- Enzyme-Mimicking Cryptography -----")
    ciphertext = enzyme_encrypt(plaintext, key)
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext (Encrypted): {ciphertext}")

    # Step 2: Decrypt the ciphertext
    decrypted_text = enzyme_decrypt(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}")

    # Step 3: Generate hash using protein-folding-inspired method
    print("\n----- Protein Folding Cryptographic Hash -----")
    hash_value = protein_hash(plaintext)
    print(f"Protein Hash of '{plaintext}': {hash_value}")

    # Optional: Display folded structure
    residues = to_residues(plaintext)
    folded_structure = fold_protein(residues)
    print("\nFolded Structure:")
    print(" → ".join(folded_structure))


if __name__ == "__main__":
    main()
