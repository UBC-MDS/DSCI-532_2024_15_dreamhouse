import pandas as pd

def load_data(url):
    return pd.read_csv(url)

def load_feather(url):
    return pd.read_feather(url)


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

df1_url = 'data/processed/data.feather'
df2_url = 'https://query.data.world/s/npaool4liamcv2ltc6jeji3pq7gptl?dws=00000'

df = load_feather(df1_url)
df2 = load_data(df2_url)

df['Zip Code'] = df['Zip Code'].astype(str)
df2['ZIP'] = df2['ZIP'].astype(str)


# State Average Price Level
# This object is used to render the default map
state_avg_prices = df.groupby('code')['Price per SqFt'].mean().reset_index()

# The following process adds the Federal Information Processing Standards information to dataframe
# Fibs information imported from data.world
df = pd.merge(df, df2[['ZIP', 'STCOUNTYFP']], left_on='Zip Code', right_on='ZIP', how='left')
df.rename(columns={'STCOUNTYFP': 'fips'}, inplace=True)
df.drop(columns='ZIP', inplace=True)

# Pad counties that have a 4 digit fips code to make them 5 digits
df['fips_str'] = df['fips'].astype(str).str.zfill(5)