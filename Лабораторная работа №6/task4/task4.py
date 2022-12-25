import json

INPUT_FILE = "input.csv"


def csv_to_list_dict() -> list[dict]:
    with open(INPUT_FILE, 'r') as i_f:
        lines_list = i_f.read().split('\n')
        cells_list = [line.split(',') for line in lines_list]
        list_dict = [dict(zip(cells_list[0], cells_list[i])) for i in range(1, len(lines_list)-1)]
    return list_dict  # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(), indent=4))
