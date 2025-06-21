"""

"""

import csv, json

def main():
    parse_file("data.csv", "data.json")

NONE_NAMES = { "", "(无嗣)" }
def is_not_name(name):
    return (name in NONE_NAMES)
def is_some_name(name):
    return not is_not_name(name)

def build_tree(table, i, j):
    root = table[i][j]
    children = []
    height = len(table)
    width = len(table[0])
    if j + 1 < width and is_some_name(table[i][j+1]):
        # try to add children
        children.append(build_tree(table, i, j+1))
        for ic in range(i+1, height):
            if is_some_name(table[ic][j+1]):
                if is_not_name(table[ic][j]):
                    children.append(build_tree(table, ic, j+1))
                else:
                    break
    return (root, children)

def parse_file(input_csv, output_json):
    table = []
    with open(input_csv, "r", encoding="utf-8") as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            table.append(row)
    tree = build_tree(table, 1, 0)
    with open(output_json, "w", encoding="utf-8") as f:
        f.write(json.dumps(tree, ensure_ascii=False))

if __name__ == "__main__":
    main()
