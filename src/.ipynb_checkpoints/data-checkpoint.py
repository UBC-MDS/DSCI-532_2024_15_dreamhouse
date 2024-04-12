import pandas as pd

def load_data():
    return pd.read_csv('../data/processed/processed_df.csv')

# Item associated with mouse clicking function
state_abbreviations = {
    'Arizona': 'AZ', 'California': 'CA', 'Colorado': 'CO', 'District of Columbia': 'DC',
    'Florida': 'FL', 'Georgia': 'GA', 'Illinois': 'IL', 'Indiana': 'IN',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maryland': 'MD',
    'Michigan': 'MI', 'Minnesota': 'MN', 'Missouri': 'MO', 'Nebraska': 'NE',
    'Nevada': 'NV', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Tennessee': 'TN', 'Texas': 'TX', 'Virginia': 'VA', 'Washington': 'WA',
    'Wisconsin': 'WI'
}

# Item associated with mouse clicking function
state_mapping = {abbr: state for state, abbr in state_abbreviations.items()}

df = load_data()

state_avg_prices = df.groupby('code')['Price per SqFt'].mean().reset_index()
