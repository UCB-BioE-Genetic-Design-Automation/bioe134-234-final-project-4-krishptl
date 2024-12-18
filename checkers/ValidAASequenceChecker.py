import re

class ValidAASequenceChecker:
    """
    Description: 
    This class checks if the amino acid sequence contains only valid amino acids (A-Z, excluding special characters).
    """

    def run(self, aa_sequence: str) -> bool:
        """
        Check if the sequence contains only valid amino acids.
        :param aa_sequence: The amino acid sequence string to be validated.
        :return: Boolean indicating whether the sequence is valid.
        """
        # Define valid amino acids
        valid_aa = "ACDEFGHIKLMNPQRSTVWY"  
        return all(aa in valid_aa for aa in aa_sequence)
