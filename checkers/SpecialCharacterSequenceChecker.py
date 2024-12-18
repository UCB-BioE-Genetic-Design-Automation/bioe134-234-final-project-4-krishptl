class SpecialCharacterAASequenceChecker:
    """
    Description: 
    This class checks if the amino acid sequence contains any special characters.
    """

    def run(self, aa_sequence: str) -> bool:
        """
        Check if the sequence contains any special characters.
        :param aa_sequence: The amino acid sequence string to be validated.
        :return: Boolean indicating whether the sequence contains special characters.
        """
        # Define the regex pattern for special characters
        pattern = re.compile(r'[^ACDEFGHIKLMNPQRSTVWY]')
        return bool(pattern.search(aa_sequence))
