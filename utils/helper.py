import sys
import json
import tomllib

def parse_json(target):
    try:
        with open(target, "r") as f:
            isi = json.load(f)
        return isi
    except FileNotFoundError:
        print("File tidak ditemukan!")
        sys.exit(0)
    except json.JSONDecodeError as e:
        print(f"Gagal mem-parsing\n{e}")
        sys.exit(0)

def parse_toml(target):
    try:
        with open(target, "rb") as f:
            isi = tomllib.load(f)
        return isi
    except FileNotFoundError:
        return {}
    except tomllib.TOMLDecodeError as e:
        print(f"Gagal mem-parsing\n{e}")
        sys.exit(0)

if __name__ == "__main__":
    print("haii")
