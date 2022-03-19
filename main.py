import csv
import json
from pathlib import Path
from typing import List

import typer

app = typer.Typer()


def parse_csv_file(file: Path) -> List:
    result = []
    with file.open(mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            result.append(row)
    return result


def generate_json_file(content, output_dir, output_file_name):

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    json_file = output_path / output_file_name
    json_file.write_text(
        json.dumps(content, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )


@app.command()
def cvs_to_json(
    file: Path,
    output_dir: str = ".",
    output_file_name: str = "",
):
    """
    Create a json file from a csv file

    provide the name/path to the csv file

    path to the outfile , optional with --output-dir

    name of the output file, optional with --output-file-name

    """
    content = parse_csv_file(file)

    file_name = (
        file.name.replace(".csv", ".json") if not output_file_name else output_file_name
    )

    generate_json_file(content, output_dir, file_name)


if __name__ == "__main__":
    app()
