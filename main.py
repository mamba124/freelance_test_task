import os
import json
import re
import pandas as pd
import argparse
from llm import process_text


def main(products_path, features_path, output_path):
    with open(features_path, "r") as f:
        features = [line.strip() for line in f]

    if os.path.exists(output_path):
        df = pd.read_excel(output_path, index_col=0)
    else:
        df = pd.DataFrame(index=features)

    products_list = [f for f in os.listdir(products_path) if os.path.isfile(os.path.join(products_path, f))]

    for product_title in products_list:
        if product_title in df.columns:
            continue

        file_path = os.path.join(products_path, product_title)
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        extracted_features_dict = process_text(features, text).split('json')[1].replace("`", "")
        print(0.03*len(extracted_features_dict)/4000)
        extracted_features = json.loads(extracted_features_dict)

        extracted_features.pop('NOTFOUND', None)

        column_name = product_title
        values = [extracted_features.get(feature, None) for feature in features]
        df[column_name] = values

    df.to_excel(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process product data and extract features.")
    parser.add_argument("--data_folder", help="Path to the folder containing product data files.")
    parser.add_argument("--features_path", help="Path to the features.txt file.")
    parser.add_argument("--output_path", help="Name of the output file (Excel).")

    args = parser.parse_args()

    main(args.data_folder, args.features_path, args.output_path)
