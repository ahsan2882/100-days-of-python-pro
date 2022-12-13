from pathlib import Path

f1_path = Path(Path(__file__).parent.resolve(), 'file1.txt').resolve()
f2_path = Path(Path(__file__).parent.resolve(), 'file2.txt').resolve()

with open(f1_path, 'r') as f1:
    f1_lines = f1.readlines()
    f1_lines = [int(line.strip()) for line in f1_lines]

with open(f2_path, 'r') as f2:
    f2_lines = f2.readlines()
    f2_lines = [int(line.strip()) for line in f2_lines]

result = [line for line in f1_lines if line in f2_lines]

print(result)
