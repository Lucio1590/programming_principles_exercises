# CODE USED FOR TESTS
from virgilio import Virgilio

programming_principles_exercises_path = (
    "/Users/luciandiaconu/Documents/Repos/Lucio/programming_principles_exercises/canti")

virgilio = Virgilio(programming_principles_exercises_path)

print(virgilio.read_canto_lines(1)) # --> ["...","...", ...]
print(virgilio.count_verses(1))  # --> 136
print(virgilio.count_tercets(1))  # --> 45
print(virgilio.count_word(1, "paura"))  # --> "paura" --> 5
print(virgilio.get_verses_with_word(1, "paura"))  # --> "paura" --> ["...","...", ...]
print(virgilio.get_longest_verse(1))  # --> che ’n tutti suoi pensier piange e s’attrista;
print(virgilio.get_longest_canto())  # --> {'canto_number': 33, 'canto_len': 157}
print(virgilio.count_words(1, ["paura", "amore", "che"]))  # --> {'paura': 5, 'amore': 2, 'che': 42}
print(virgilio.get_hell_verses())  # --> ["...","...", ...]
print(virgilio.count_hell_verses())  # --> 4720
print(virgilio.get_hell_verses_mean_len())  # --> 36.22351694915254
print(virgilio.read_canto_lines(canto_number=1, strip_lines=True, num_lines=5))  # --> ["...","...", ...]
