# :us: :house_with_garden: Find Your Dream House  :house_with_garden: :us:

## Project Overview

This dashboard presents an interactive visualization of housing prices across the top 50 most populous cities in the United States of America. The data is sourced from a comprehensive dataset available on Kaggle, which includes demographics and house prices of the top cities in the United States. Our dashboard is built using the Dash package, enabling users to filter and explore the housing market data across various dimensions, such as state, city, house type, square footage, number of bedrooms and bathrooms, and more.

## Our Motivation

Millions of people buy their first home every year, and likely lack the market knowledge or experience to know how to find what they’re looking for. We want to help new-comers to the real-estate market by creating a data visualization app to help explore house listings in the United States’ 50 most populous cities. Our app will display listings in each city and will give users the ability to filter by state or city, price, number of bedrooms and bathrooms, and other metrics. It will also display the factors that are most heavily associated with price so that uninformed sellers get a good sense of what similar homes are being sold for and help them get the right value in their local market.

## Preview

![](https://github.com/UBC-MDS/DSCI-532_2024_15_dreamhouse/blob/main/img/demo.gif)

## Features

- Interactive map visualizing average housing prices by region.
- Filterable options for state and city selection.
- Detailed pricing across top cities and a comparative list by states.
- Visual representation of median house price, median square footage, and common home types.
- Dynamic charts and graphs updating with user input.

## Data Source

The dataset used in this project is available on Kaggle: [American House Prices and Demographics of Top Cities](https://www.kaggle.com/datasets/jeremylarcher/american-house-prices-and-demographics-of-top-cities).

## Installation

1. Clone the repository to your local PC
Click "code" on the repository page and copy the URL. In your local PC, open the terminal and enter:
```
git clone https://github.com/UBC-MDS/DSCI-532_2024_15_dreamhouse.git
```

2. activate a virtual environment using conda
```
conda env create -f environment.yml
conda activate environment
```

3. Open src folder and run app.py by Jupiter Notebook.
   Then you will see the dashboard!

## Usage

[Find your dream house!](dsci-532-2024-15-dreamhouse-odas.onrender.com/)

The dashboard is designed to help display the key statistics of the real-estate market as well as a map of the selected area and a bar graph outlining the average price of listings in the selected area. The dashboard makes it easy to filter the data by state, city, square footage, price range, price per square foot, median household income of the zip code, number of bedrooms, and number of bathrooms. Once you have selected the criteria of your dream home, the dashboard will update to display the price of corresponding homes, their locations, and the summary statistics of all those homes that fit your selection.

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Acknowledgements

- Dataset provided by [Jeremy Larcher on Kaggle](https://www.kaggle.com/jeremylarcher).
- Dash, Plotly, and Pandas for providing the tools to build this interactive dashboard.
- Our dedicated team who worked tirelessly to bring this project to fruition.

## Contact

For any queries regarding this project, please open an issue in the GitHub repository or reach out to us directly through our contact information provided in the repository.


