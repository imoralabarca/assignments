import pandas as pd

def load_data(file_path):
    """Loads the data from a TSV file and returns a DataFrame."""
    try:
        df = pd.read_csv(file_path, sep='\t')
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

def save_data(df, output_path):
    """Saves the cleaned data to a CSV file."""
    try:
        df.to_csv(output_path, index=False)
        print(f"Data saved to '{output_path}' successfully.")
    except Exception as e:
        print(f"An error occurred while saving the data: {e}")
