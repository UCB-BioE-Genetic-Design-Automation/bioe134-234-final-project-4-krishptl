class EmptyAASequenceChecker:
    """
    Description: 
    This class checks if the amino acid sequence is empty.
    """

    def run(self, aa_sequence: str) -> bool:
        """
        Check if the sequence is empty.
        :param aa_sequence: The amino acid sequence string to be validated.
        :return: Boolean indicating whether the sequence is empty.
        """
        return len(aa_sequence) == 0
