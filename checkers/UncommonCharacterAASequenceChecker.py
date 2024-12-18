class UncommonCharacterAASequenceChecker:
    """
    Description: 
    This class checks if the amino acid sequence contains uncommon characters.
    """

    uncommon_characters = set("0123456789!@#$%^&*()_+={}[]|:;'<>,.?/`~")  # Add any uncommon characters

    def run(self, aa_sequence: str) -> bool:
        """
        Check if the sequence contains uncommon characters.
        :param aa_sequence: The amino acid sequence string to be validated.
        :return: Boolean indicating whether the sequence contains uncommon characters.
        """
        return any(char in self.uncommon_characters for char in aa_sequence)
