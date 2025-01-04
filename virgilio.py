import math
import os
import json


class Virgilio:
    def __init__(self, directory):
        self.directory = directory

    class CantoNotFoundError(Exception):
        def __init__(self):
            super().__init__("canto_number must be between 1 and 34.")

    def read_canto_lines(self, canto_number, strip_lines=False, num_lines=None):
        if type(canto_number) is not int:
            raise TypeError("canto_number must be an integer")

        # this other checks are not part of the exercises but are useful to me
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
        try:
            tercets = self.count_verses(canto_number) / 3
            return math.floor(tercets)
        except Exception as e:
            print(e)
            return None

    def count_word(self, canto_number, word):
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
        # canto_count = len(os.listdir(self.directory))
        canto_count = 34

        longest_canto = {'canto_number': 0, 'canto_len': 0}
        all_verses = []
        for canto_number in range(1, canto_count + 1):
            canto = self.read_canto_lines(canto_number)
            for verse in canto:
                all_verses.append(verse)
        return all_verses

    def count_hell_verses(self):
        return len(self.get_hell_verses())

    def get_hell_verses_mean_len(self):
        verses = self.get_hell_verses()
        verses_length = len(verses)
        all_verses_len = 0
        for verse in verses:
            all_verses_len += len(verse.strip())
        return all_verses_len / verses_length


# CODE USED FOR TESTS

# programming_principles_exercises_path = (
#     "/Users/luciandiaconu/Documents/Repos/Lucio/programming_principles_exercises/canti")
#
# virgilio = Virgilio(programming_principles_exercises_path)
#
# print(virgilio.read_canto_lines(1)) # --> ["...","...", ...]
# print(virgilio.count_verses(1))  # --> 136
# print(virgilio.count_tercets(1))  # --> 45
# print(virgilio.count_word(1, "paura"))  # --> "paura" --> 5
# print(virgilio.get_verses_with_word(1, "paura"))  # --> "paura" --> ["...","...", ...]
# print(virgilio.get_longest_verse(1))  # --> che ’n tutti suoi pensier piange e s’attrista;
# print(virgilio.get_longest_canto())  # --> {'canto_number': 33, 'canto_len': 157}
# print(virgilio.count_words(1, ["paura", "amore", "che"]))  # --> {'paura': 5, 'amore': 2, 'che': 42}
# print(virgilio.get_hell_verses())  # --> ["...","...", ...]
# print(virgilio.count_hell_verses())  # --> 4720
# print(virgilio.get_hell_verses_mean_len())  # --> 36.22351694915254
# print(virgilio.read_canto_lines(canto_number=1, strip_lines=True, num_lines=5))  # --> ["...","...", ...]
