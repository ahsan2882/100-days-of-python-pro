import pandas as pd
from pathlib import Path

file_loc = Path(Path(__file__).parent.resolve(), 'squirrel_data.csv').resolve()

data = pd.read_csv(file_loc)
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(f'Gray Squirrels: {gray_squirrels_count}')
print(f'Red Squirrels: {red_squirrels_count}')
print(f'Black Squirrels: {black_squirrels_count}')


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv(
    Path(Path(__file__).parent.resolve(), 'squirrel_count.csv').resolve())
