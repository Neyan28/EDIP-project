from etl.extract import extract_all
from etl.validate import validate_all
from etl.transform import transform_all
from etl.load import load_all


def main():
    extracted = extract_all()
    validated = validate_all(extracted)
    transformed = transform_all(validated)
    load_all(transformed)

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    main()
