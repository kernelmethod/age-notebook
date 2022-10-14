#!/usr/bin/env python3

import argparse
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog=str(Path(__file__).name),
        description="Extract the payload from an age file as a byte string"
    )
    parser.add_argument(
        "file",
        help="The age file to read",
    )

    args = parser.parse_args()

    with open(args.file, "rb") as f:
        while not (line := f.readline()).startswith(b"---"):
            ...

        print(f.read())
