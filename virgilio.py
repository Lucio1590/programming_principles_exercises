import math
import os

programming_principles_exercises_path = "/Users/luciandiaconu/Documents/Repos/Lucio/programming_principles_exercises/canti/"
print(programming_principles_exercises_path)
class Virgilio:
    def __init__(self, directory):
        self.directory = directory

    def read_canto_lines(self, canto_number):
        try:
            file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
            with open(file_path) as f:
                return f.readlines()
        except FileNotFoundError as e:
            print(f'File not found')
            return None
        except Exception as e:
            print(e)
            return None

    def count_verses(self, canto_number):
        try:
            canto = self.read_canto_lines(canto_number)
            if canto is None:
                return Exception("404: Canto not found")
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
            if canto is None:
                return Exception("404: Canto not found")
        except Exception as e:
            print(e)
            return None
        else:
            word_count = 0
            for line in canto:
                word_count += line.count(word)
            return word_count


virgilio = Virgilio(programming_principles_exercises_path)

# print(virgilio.read_canto_lines(1))
# print(virgilio.count_verses(1))
# print(virgilio.count_tercets(1))
print(virgilio.count_word(1, "paura"))
