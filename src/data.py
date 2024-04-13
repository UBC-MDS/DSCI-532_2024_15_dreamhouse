import pandas as pd

def load_data(url):
    return pd.read_csv(url)


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

df1_url = 'data/processed/processed_df.csv'
df2_url = 'https://query.data.world/s/npaool4liamcv2ltc6jeji3pq7gptl?dws=00000'

df = load_data(df1_url)
df2 = load_data(df2_url)

df['Zip Code'] = df['Zip Code'].astype(str)
df2['ZIP'] = df2['ZIP'].astype(str)

# State Average Price Level
state_avg_prices = df.groupby('code')['Price per SqFt'].mean().reset_index()

# The following process adds the Federal Information Processing Standards information to dataframe
# Fibs information imported from data.world
df = pd.merge(df, df2[['ZIP', 'STCOUNTYFP']], left_on='Zip Code', right_on='ZIP', how='left')
df.rename(columns={'STCOUNTYFP': 'fips'}, inplace=True)
df.drop(columns='ZIP', inplace=True)
