from json import load


INPUT_FILENAME = "input.json"


def task() -> float:
    with open(INPUT_FILENAME, "r") as file:
        data_json = load(file)
    values = [val["score"]*val["weight"] for val in data_json]
    return round(sum(values), 3)


print(task())
