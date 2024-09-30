import os
import argparse
import pandas as pd
from cleaning import load_data, clean_data, save_data

# Define paths
input_file_path = os.path.join('data', 'eu_life_expectancy_raw.tsv')
fixture_input_path = os.path.join('tests', 'fixtures', 'eu_life_expectancy_raw.tsv')
expected_output_path = os.path.join('tests', 'fixtures', 'eu_life_expectancy_expected.csv')

def create_input_fixture(country):
    """Creates the input fixture by sampling the raw data."""
    # Load the full dataset
    df = pd.read_csv(input_file_path, sep='\t')

    # Create a sample of the data for the specified country
    sample_df = df[df.iloc[:, 0].str.contains(country)]

    # Save the sample to the fixture path
    sample_df.to_csv(fixture_input_path, sep='\t', index=False)
    print(f"Sample fixture saved to {fixture_input_path}")

def create_expected_fixture(country):
    """Creates the expected output fixture using the input fixture."""
    # Load the sample fixture
    df_sample = load_data(fixture_input_path)

    # Clean the sample data for the specified region
    cleaned_df = clean_data(df_sample, country=country)

    # Save the cleaned data as the expected output fixture
    cleaned_df.to_csv(expected_output_path, index=False)
    print(f"Expected output fixture saved to {expected_output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create fixtures for testing.")
    parser.add_argument('--country', type=str, default='PT', help='Country code to filter data (default: PT)')
    
    args = parser.parse_args()

    create_input_fixture(args.country)
    create_expected_fixture(args.country)
