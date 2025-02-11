import React, { useState } from 'react';
import axios from 'axios';
import Protein3DView from './Protein3DView';

const ProteinCryptoAnimation = () => {
    const [plaintext, setPlaintext] = useState("HELLOCRYPTOWORLD");
    const [key, setKey] = useState(3);
    const [ciphertext, setCiphertext] = useState("");
    const [decryptedText, setDecryptedText] = useState("");
    const [pdbId, setPdbId] = useState("");
    const [fetchedPdb, setFetchedPdb] = useState("");

    const handleEncryption = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:5002/encrypt', {
                plaintext: plaintext,
                key: key,
            });

            setCiphertext(response.data.ciphertext);
            setDecryptedText(response.data.decrypted_text);
        } catch (error) {
            console.error("Error connecting to the backend:", error);
        }
    };

    const fetchPdbFromAlphafold = async () => {
        try {
            const response = await axios.get(`https://www.alphafold.ebi.ac.uk/api/prediction/${pdbId}`);
            if (response.data && response.data.length > 0) {
                const pdbFileUrl = response.data[0].pdbUrl;
                setFetchedPdb(pdbFileUrl);
                console.log("Fetched PDB file from AlphaFold:", pdbFileUrl);
            } else {
                alert("No PDB structure found for this UniProt ID.");
            }
        } catch (error) {
            console.error("Error fetching PDB file from AlphaFold:", error);
        }
    };

    return (
        <div className="flex flex-col items-center gap-4 p-6">
            <h1 className="text-2xl font-bold">Protein-Inspired Cryptography</h1>
            <input
                type="text"
                value={plaintext}
                onChange={(e) => setPlaintext(e.target.value)}
                className="border p-2 rounded w-full"
                placeholder="Enter plaintext"
            />
            <input
                type="number"
                value={key}
                onChange={(e) => setKey(Number(e.target.value))}
                className="border p-2 rounded w-full mt-2"
                placeholder="Encryption Key"
            />
            <input
                type="text"
                value={pdbId}
                onChange={(e) => setPdbId(e.target.value)}
                className="border p-2 rounded w-full mt-2"
                placeholder="Enter UniProt ID (e.g., P69905)"
            />
            <div className="mt-4">
                <button onClick={handleEncryption} className="bg-blue-500 text-white p-2 rounded mr-2">
                    Encrypt Text
                </button>
                <button onClick={fetchPdbFromAlphafold} className="bg-green-500 text-white p-2 rounded">
                    Fetch PDB Structure
                </button>
            </div>

            <p className="mt-4">Ciphertext: <strong>{ciphertext}</strong></p>
            <p>Decrypted Text: <strong>{decryptedText}</strong></p>

            {fetchedPdb && (
                <div className="mt-6">
                    <h2 className="text-lg font-semibold">3D Protein Structure</h2>
                    <Protein3DView pdbFileUrl={fetchedPdb} />
                </div>
            )}
        </div>
    );
};

export default ProteinCryptoAnimation;
