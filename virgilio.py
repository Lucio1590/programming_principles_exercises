import math
import os
import json


class Virgilio:
    """Class that reads the canti of Dante's Inferno
    and performs various operations on them as re by the pdf of exercises"""

    def __init__(self, directory: str):
        """Constructor of the class Virgilio
        -------------------------
        Attributes:

            directory: str
                the directory where the canti are stored,
                it is expected to be the absolute path where canti are stored
        """

        self.directory = directory

    class CantoNotFoundError(Exception):
        """Custom exception to be raised when the canto number is not found
        Inherited from "Exception" base class
        """

        def __init__(self):
            super().__init__("canto_number must be between 1 and 34.")

    def read_canto_lines(self, canto_number: int, strip_lines: bool = False, num_lines: int = None):
        """Method that reads the lines of a canto from a file based on the canto number
        -------------------------
        Params:
                canto_number: int
                    the number of the canto to be read
                strip_lines: bool
                    if True the lines will be stripped of leading and trailing whitespaces
                num_lines: int
                    if not None, only the first num_lines will be read

        Returns:
            str[]:
                the lines of the canto as strings

        Raises:
            TypeError
                if canto_number is not an integer
                if strip_lines is not a boolean
                if num_lines is not an integer
            CantoNotFoundError
                if the canto number is not found

        """

        if type(canto_number) is not int:
            raise TypeError("canto_number must be an integer")

        # this other error checks are not part of the exercises but are useful to me
        if type(strip_lines) is not bool:
            raise TypeError("strip_lines must be a boolean")
        if num_lines is not None and type(num_lines) is not int:
            raise TypeError("num_lines must be an integer")

        if canto_number < 1 or canto_number > 34:
            raise self.CantoNotFoundError()

        try:

            file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")

            with open(file_path) as f:
                lines = f.readlines()
                if num_lines:
                    lines = lines[:num_lines]
                if strip_lines:
                    return [line.strip() for line in lines]
                else:
                    return lines
        except Exception:
            print(f"error while opening{self.directory}/Canto_{canto_number}.txt")
            return f"error while opening{self.directory}/Canto_{canto_number}.txt"

    def count_verses(self, canto_number):
        """Method that counts the number of verses in a canto
        -------------------------
        Params:
                canto_number: int
                    the number of the canto to be read

        Returns:
            int:
                the number of verses in the canto

        """

        try:
            canto = self.read_canto_lines(canto_number)
            if canto is None:
                raise Exception("404: Canto not found")
            canto_length = len(canto)
        except Exception as e:
            print(e)
            return None

        else:
            return canto_length

    def count_tercets(self, canto_number):
        """Method that counts the number of tercets in a canto
        -------------------------
        Params:
                canto_number: int
                    the number of the canto to be read
        Returns:
            int:
                the number of tercets in the canto
        """

        try:
            tercets = self.count_verses(canto_number) / 3
            return math.floor(tercets)
        except Exception as e:
            print(e)
            return None

    def count_word(self, canto_number, word):
        """Method that counts the number of occurrences of a word in a canto
        -------------------------
        Params:
                canto_number: int
                    the number of the canto to be read
                word: str
                    the word to be counted
        Returns:
            int:
                the number of occurrences of the word in the canto
        """

        try:
            canto = self.read_canto_lines(canto_number)

            word_count = 0
            for line in canto:
                # using string count method that returns the number of occurrences of a substring in the given string
                word_count += line.count(word)

            return word_count

        except Exception as e:
            print(e)
            return None

    def get_verse_with_word(self, canto_number, word):
        """Method that returns the first verse that contains a word in a canto
        -------------------------
        Params:
                canto_number: int
                    the number of the canto to be read
                word: str
                    the word to be searched
        Returns:
            str:
                the first verse that contains the word
        """

        try:
            canto = self.read_canto_lines(canto_number)

            for line in canto:
                # using string.find: that returns -1 if the substring is not found otherwise the index of the first
                # occurrence
                if line.find(word) != -1:
                    return line

        except Exception as e:
            print(e)
            return None

    def get_verses_with_word(self, canto_number, word):
        """Method that returns all the verses that contain a word in a canto
        -------------------------
        Params:
                canto_number: int
                    the number of the canto to be read
                word: str
                    the word to be searched
        Returns:
            str[]:
                the verses that contain the word
        """

        try:
            canto = self.read_canto_lines(canto_number)
            lines = []

            for line in canto:
                if line.find(word) != -1:
                    lines.append(line)

            return lines

        except Exception as e:
            print(e)
            return None

    def get_longest_verse(self, canto_number):
        """Method that returns the longest verse in a canto
        -------------------------
        Params:
                canto_number: int
                    the number of the canto to be read
        Returns:
            str:
                the longest verse in the canto
        """

        try:
            canto = self.read_canto_lines(canto_number)
        except Exception as e:
            print(e)
            return None
        else:
            longest_verse = ''
            len_of_longest_verse = 0
            # using the second variable to make less calls to "len()"

            for line in canto:
                len_of_line = len(line)
                if len_of_line > len_of_longest_verse:
                    # updating the longest verse and its length
                    longest_verse = line
                    len_of_longest_verse = len_of_line
            return longest_verse

    def get_longest_canto(self):
        """Method that returns the longest canto
        -------------------------
        Returns:
            dict: {'canto_number': int, 'canto_len': int}
                a dictionary with the number of the longest canto and its length
            """

        # canto_count = len(os.listdir(self.directory))
        # this would be usefull if we would wnato to use this method for multiple directories
        # anyway for simplicity I will use the "magic number" 34 being common knowledge that the number of canti is 34
        canto_count = 34

        longest_canto = {'canto_number': 0, 'canto_len': 0}

        for canto_number in range(1, canto_count + 1):
            canto_len = self.count_verses(canto_number)
            if canto_len > longest_canto['canto_len']:
                longest_canto['canto_number'] = canto_number
                longest_canto['canto_len'] = canto_len

        return longest_canto

    def count_words(self, canto_number, words):
        """Method that counts the number of occurrences of multiple words in a canto
        -------------------------
        Params:
                canto_number: int
                    the number of the canto to be read
                words: str[]
                    the words to be counted
        Returns:
            dict: {str: int}
                a dictionary with the words as keys and their occurrences as values
        """

        try:
            response_words_count = {}
            for word in words:
                word_count = self.count_word(canto_number, word)
                response_words_count[word] = word_count

            word_counts_file_path = os.path.join(self.directory, "word_counts.json")

            with open(word_counts_file_path, 'w') as fp:
                json.dump(response_words_count, fp, indent=4)

        except Exception as e:
            print(e)
            return None

        else:
            return response_words_count

    def get_hell_verses(self):
        """Method that returns all the verses in the Inferno
        -------------------------
        Returns:
            str[]:
                all the verses in the Inferno
        """

        # canto_count = len(os.listdir(self.directory)), explained in the get_longest_canto method
        canto_count = 34

        longest_canto = {'canto_number': 0, 'canto_len': 0}
        all_verses = []
        for canto_number in range(1, canto_count + 1):
            canto = self.read_canto_lines(canto_number)
            for verse in canto:
                all_verses.append(verse)
        return all_verses

    def count_hell_verses(self):
        """Method that counts the number of verses in the Inferno
        -------------------------
        Returns:
            int:
                the number of verses in the Inferno
        """

        return len(self.get_hell_verses())

    def get_hell_verses_mean_len(self):
        """Method that calculates the mean length of the verses in the Inferno
        -------------------------
        Returns:
            float:
                the mean length of the verses in the Inferno
        """

        verses = self.get_hell_verses()
        verses_length = len(verses)
        all_verses_len = 0
        for verse in verses:
            all_verses_len += len(verse.strip())
        return all_verses_len / verses_length
