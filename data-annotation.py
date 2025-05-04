# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "html5lib",
#     "pandas",
# ]
# ///

import pandas as pd


def print_letter(frame: pd.DataFrame) -> None:
    xcoord = frame["x-coordinate"]
    ycoord = frame["y-coordinate"]
    char = frame["Character"]

    for i in range(0, len(ycoord)):
        if (i != 0) and (xcoord[i] - xcoord[i - 1] > 1):
            # empty spaces
            print(" " * int((xcoord[i]) - (xcoord[i - 1]) - 1), end="")
        if (i != 0) and (ycoord[i] != (ycoord[i - 1])):
            # new line
            print("\r")
        print(char[i], end="")
    print("\n")


def solve(url: str) -> None:
    tables = pd.read_html(url, header=0, flavor="bs4")
    frame = tables[0].sort_values(
        by=["y-coordinate", "x-coordinate"], ignore_index=True, ascending=[False, True]
    )

    print_letter(frame)


if __name__ == "__main__":
    # solve(
    #     "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    # )
    solve(
        "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    )
