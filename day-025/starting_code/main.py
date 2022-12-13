import pandas as pd
from pathlib import Path

file_loc = Path(Path(__file__).parent.resolve(), 'weather_data.csv').resolve()

with open(file_loc) as data_file:
    data = pd.read_csv(data_file)
    print(data)
