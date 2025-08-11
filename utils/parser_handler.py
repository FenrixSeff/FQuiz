import json

def parse_json(target):
    with open(target, "r") as f:
        isi = json.load(f)
    return isi


if __name__ == "__main__":
    print("haii")
