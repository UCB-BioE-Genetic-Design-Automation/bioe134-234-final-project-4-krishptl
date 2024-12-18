class LowercaseAASequenceChecker:
    """
    Description: 
    This class checks if the amino acid sequence contains any lowercase letters.
    """

    def run(self, aa_sequence: str) -> bool:
        """
        Check if the sequence contains lowercase letters.
        :param aa_sequence: The amino acid sequence string to be validated.
        :return: Boolean indicating whether the sequence contains lowercase letters.
        """
        return not aa_sequence.isupper()