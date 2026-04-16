import csv
from pathlib import Path

DATA_DIR = Path("./data")
OUTPUT_PATH = Path("./formatted_data.csv")

def process_files():
    with OUTPUT_PATH.open(mode="w", newline="") as out_file:
        csv_writer = csv.writer(out_file)
        
        # write header
        csv_writer.writerow(["sales", "date", "region"])

        # loop through all CSV files in directory
        for file_path in DATA_DIR.iterdir():
            if file_path.is_file():
                handle_file(file_path, csv_writer)

def handle_file(file_path, writer):
    with file_path.open(mode="r") as in_file:
        csv_reader = csv.reader(in_file)
        
        # skip header row
        next(csv_reader, None)

        for row in csv_reader:
            process_row(row, writer)

def process_row(row, writer):
    product, raw_price, quantity, date, region = row

    if product != "pink morsel":
        return

    # calculate sale value
    price = float(raw_price.replace("$", ""))
    total_sale = price * int(quantity)

    writer.writerow([total_sale, date, region])


if __name__ == "__main__":
    process_files()