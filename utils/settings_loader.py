from pathlib import Path
from .helper import parse_toml

lok = Path(__file__).parent.parent / "settings.toml"

setting = parse_toml(lok)

if __name__ == "__main__":
    print(setting)
