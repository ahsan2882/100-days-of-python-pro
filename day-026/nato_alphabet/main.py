from pathlib import Path
import pandas as pd

file_loc = Path(Path(__file__).parent.resolve(),
                'nato_phonetic_alphabet.csv').resolve()

df = pd.read_csv(file_loc)
nato_list = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("Enter a word: ").upper()
result = [nato_list[letter] for letter in user_input]
print(result)
