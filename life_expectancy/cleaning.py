import os
import argparse
import pandas as pd

def clean_data(country='PT'):

    data_path = os.path.join(os.path.dirname(__file__), 'data', 'eu_life_expectancy_raw.tsv')
    df = pd.read_csv(data_path, sep='\t')
    print("Data loaded successfully.")
    df_long = df.melt(id_vars=df.columns[0], var_name='year', value_name='value')
    df_long[['unit', 'sex', 'age', 'region']] = df_long[df.columns[0]].str.split(',', expand=True)
    df_long = df_long.drop(columns=[df.columns[0]])
    df_long['year'] = df_long['year'].astype(int)
    df_long['value'] = pd.to_numeric(df_long['value'], errors='coerce')
    df_long = df_long.dropna(subset=['value'])
    df_country = df_long[df_long['region'] == country]
    output_path = os.path.join(os.path.dirname(__file__), 'data',
                               f'{country.lower()}_life_expectancy.csv')
    df_country.to_csv(output_path, index=False)
    print(f"Data saved to '{country.lower()}_life_expectancy.csv' successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
                                     "Clean life expectancy data for a specific country.")
    parser.add_argument('--country', type=str, default='PT',
                        help='Country code to filter the data (default: PT)')
    args = parser.parse_args()

    clean_data(country=args.country)
