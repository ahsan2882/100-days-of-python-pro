from pathlib import Path

current_dir = Path(__file__).parent.resolve()
starting_letter__path = Path(
    current_dir, "Input", "Letters", "starting_letter.txt").resolve()
names_path = Path(current_dir, "Input", "Names", "invited_names.txt").resolve()

output_dir = Path(current_dir, "Output", "ReadyToSend").resolve()

with open(starting_letter__path) as file:
    starting_letter = file.read()

with open(names_path) as file:
    names = file.readlines()


for name in names:
    name = name.strip()
    named_letter = starting_letter.replace("[name]", name)
    with open(Path(output_dir, f"{name}.txt").resolve(), "w") as file:
        file.write(named_letter)
