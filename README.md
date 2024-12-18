
# BioE 134 Final Project Submission

## Project Overview

This project provides bioinformatics utilities for retrieving and processing protein sequences from UniProt:

1. **Query UniProt**: Retrieves the amino acid sequence of a protein by its name or UniProt ID.
2. **Strip FASTA Header**: Removes the header from a FASTA-formatted protein sequence for easier processing.

These functions are implemented in **Python** and aim to automate protein sequence retrieval and processing tasks as part of a bioinformatics toolkit.

---

## Scope of Work

For the final project in BioE 134, I developed a set of functions that automate protein sequence retrieval and processing, this was the first step in building a CodonOptimizer for Yeast:

1. **Query UniProt**: This function takes a protein name or UniProt ID and retrieves the corresponding amino acid sequence in FASTA format from the UniProt database.
   
2. **Strip FASTA Header**: This function processes the FASTA-formatted sequence by removing the header, returning just the amino acid sequence for further analysis.

Both functions include error handling for invalid or missing protein entries, ensuring robust usage.

---

## Function Descriptions

### 1. Query UniProt (`query_uniprot`)

- **Description**: This function queries the UniProt database to retrieve the amino acid sequence of a protein based on either its name or UniProt ID. The sequence is returned in FASTA format.
- **Input**: A string representing the protein name or UniProt ID.
- **Output**: A string representing the protein sequence in FASTA format.

**Example**:
```python
query_uniprot("P12345")
# Returns: ">sp|P12345|ProteinName Protein sequence...
MSTKRTAG..."
```

### 2. Strip FASTA Header (`strip_fasta_header`)

- **Description**: This function takes a FASTA-formatted protein sequence and removes the header, returning only the amino acid sequence.
- **Input**: A string representing the protein sequence in FASTA format.
- **Output**: A string representing the protein sequence without the header.

**Example**:
```python
strip_fasta_header(">sp|P12345|ProteinName Protein sequence...
MSTKRTAG...")
# Returns: "MSTKRTAG..."
```

### 3. Main Function (`main`)

- **Description**: This function acts as a wrapper to both query UniProt for a protein sequence and strip the FASTA header. It returns a clean amino acid sequence without any headers.
- **Input**: A string representing the protein name or UniProt ID.
- **Output**: A string representing the amino acid sequence without the FASTA header.

**Example**:
```python
main("P12345")
# Returns: "MSTKRTAG..."
```

---

## Error Handling

### Query UniProt
- Raises a `ValueError` if no protein sequence is found for the provided name or UniProt ID.

### Strip FASTA Header
- Returns the original data if the FASTA header is not present. If the input is not in valid FASTA format, the function will return the input unchanged.

### Main Function
- Raises a `ValueError` if no valid sequence is found after querying UniProt.

---

## Testing

The functions have been tested with various protein name/ID inputs and valid/invalid sequences to ensure robustness. The tests include:

- Valid protein names/IDs
- Handling of missing or invalid protein entries
- Proper header removal from FASTA sequences

Tests have been implemented using **pytest** to ensure functionality.

- **Test File**: `tests/test_protein_seq_retriever.py`

---

## Usage Instructions

Clone the repository and install the required dependencies listed in `requirements.txt`. The functions can be imported from the `protein_seq_retriever.py` module.

**Example**:

```bash
pip install -r requirements.txt
```

Once installed, you can use the functions as follows:

```python
from protein_seq_retriever import query_uniprot, strip_fasta_header, main

# Example protein name or UniProt ID
protein_name_or_id = "P12345"

# Query UniProt
fasta_sequence = query_uniprot(protein_name_or_id)

# Strip FASTA header
clean_sequence = strip_fasta_header(fasta_sequence)

# Main function to get clean sequence
final_sequence = main(protein_name_or_id)

print(final_sequence)
```

---

## Conclusion

This project provides essential utilities for protein sequence retrieval and processing. The functions are tested, include proper error handling, and are documented to ensure they can be used effectively in bioinformatics workflows. 