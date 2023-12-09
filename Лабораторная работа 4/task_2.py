from json import dump
from csv import DictReader


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as file:
        reader = DictReader(file)
        data_csv = list()
        for row in reader:
            data_csv.append(row)

    with open(OUTPUT_FILENAME, "w") as file:
        dump(data_csv, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
