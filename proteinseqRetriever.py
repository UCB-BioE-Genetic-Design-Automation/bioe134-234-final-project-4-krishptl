import requests

def query_uniprot(protein_name_or_id):
    """
    Query UniProt to retrieve amino acid sequence by protein name or ID.

    Args:
        protein_name_or_id (str): Name or UniProt ID of the protein to query.

    Returns:
        str: Amino acid sequence in FASTA format.
    """
    base_url = "https://rest.uniprot.org/uniprotkb/search"
    params = {
        "query": protein_name_or_id,  # Name or UniProt ID
        "format": "fasta",            # Retrieve in FASTA format
        "size": 1                     # Return the top match
    }
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise HTTPError for bad responses
    
    if response.text.strip():
        return response.text.strip()  # Return FASTA sequence
    else:
        raise ValueError(f"No protein found for '{protein_name_or_id}'.")

def strip_fasta_header(fasta_data):
    """
    Remove the FASTA header from the sequence data.

    Args:
        fasta_data (str): Amino acid sequence in FASTA format.

    Returns:
        str: Amino acid sequence without the FASTA header.
    """
    lines = fasta_data.splitlines()
    if lines and lines[0].startswith(">"):
        return ''.join(lines[1:])  # Remove the header line and join the sequence lines
    return fasta_data  # Return original data if no header is present

def main(protein_name_or_id):
    """
    Retrieve and return the amino acid sequence of a protein.
    
    Args:
        protein_name_or_id (str): Name or UniProt ID of the protein.

    Returns:
        str: Plain amino acid sequence.
    """
    fasta_sequence = query_uniprot(protein_name_or_id)
    if fasta_sequence.startswith(">"):
        return strip_fasta_header(fasta_sequence)
    else:
        raise ValueError("No valid sequence found.")

if __name__ == "__main__":
    protein_name_or_id = input("Enter a protein name or UniProt ID: ").strip()
    aa_sequence = main(protein_name_or_id)
    print(aa_sequence)