import csv

from pathlib import Path

from constant import FILE_PATH

base_path = Path(__file__).parent
file_path = (base_path / FILE_PATH).resolve()


def get_logic():
    with open(file_path) as csvfile:
        rdr = csv.DictReader(csvfile, skipinitialspace=True)
        result = []
        for row in rdr:
            temp = []
            for k, v in row.items():
                if k is not None and v:
                    temp.append({k: int(v) if v else 0})
            result.append(temp)

    return result
    # a = [{k: int(v) for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
    # print(a)


# if __name__ == '__main__':
#     get_logic()
