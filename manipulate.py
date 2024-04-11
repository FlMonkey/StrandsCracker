class Manipulate:
    @staticmethod
    def makeset():
        def filter_words(word):
            # Check if the word has any non-alphabetic character
            if any(not char.isalpha() for char in word):
                return False
            # Check if the word is shorter than 4 characters
            if len(word) < 4:
                return False
            return True

        # Read the words from the file
        with open('WordList.txt', 'r') as file:
            words = file.readlines()

        # Filter the words based on the defined criteria
        filtered_words = [word for word in words if filter_words(word.strip())]

        # Write the filtered words back to a new file or the same file
        with open('WordListSet.txt', 'w') as file:
            file.writelines(filtered_words)