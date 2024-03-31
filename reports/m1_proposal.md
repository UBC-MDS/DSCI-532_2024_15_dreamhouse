## Milestone 1 Proposal - Group 15 - Dreamhouse

##### By: Jake Barnabe, Zeily Garcia, Ruocong Sun, Chun Li

### Section 1 - Motivation and Purpose

Our role: Real Estate Consultancy / Realty Firm (Similar to Realtor.ca)
Target audience: Uninformed buyers/sellers who are new to the housing market
Millions of people buy their first home every year, and likely lack the market knowledge or experience to know how to find what they’re looking for. We want to help new-comers to the real-estate market by creating a data visualization app to help explore house listings in the United States’ 50 most populated cities. Our app will display listings in each city and will give users the ability to filter by state or city, price, number of bedrooms and bathrooms, and other metrics. It will also display the factors that are most heavily associated with price so that uninformed sellers get a good sense of what similar homes are being sold for and help them get the right value in their market.

### Section 2 - Description of the Data

- This dataset comprises various variables around housing and demographics for the top 50 American cities by population.
- There are 39981 rows and 14 columns. 
- Since there are latitude and longitude, we can show a map on the dashboard with real estate information such as average price for certain areas or median household etc. Other variables such as price, beds, bath, city, and state will be the filter conditions if users are interested in specific house types or price ranges. Zip code, zip code population and zip code density could be shown on heatmap to give users preference when they want to purchase a dream house. 
- New variable we are planning to derive is ‘property type’. This variable will be a categorical variable including ‘townhouse’, ‘condo’, ‘house’. And this new variable will be predicted by other variables such as price, Beds, Baths, Living Space. We believe this new variable will help users to filter out the right type of their dream houses.  
- For visualization, we would have bar plots for average house price, and median household income for different cities. Some statistical summary for how many bedrooms, bathrooms, price ranges or other variables on the dashboard as well. The variables we are visualizing are all continuous float variables. Only latitude and longitude will be used as demographics visualization. 

#### Variables:

- Zip Code: Zip code within which the listing is present.
- Price: Listed price for the property.
- Beds: Number of beds mentioned in the listing.
- Baths: Number of baths mentioned in the listing.
- Living Space: The total size of the living space, in square feet, mentioned in the listing.
- Address: Street address of the listing.
- City: City name where the listing is located.
- State: State name where the listing is located.
- Zip Code Population: The estimated number of individuals within the zip code. Data from Simplemaps.com.
- Zip Code Density: The estimated number of individuals per square mile within the zip code. Data from Simplemaps.com.
- County: County where the listing is located.
- Median Household income: Estimated median household income. Data from the U.S. Census Bureau.
- Latitude: Latitude of the zip code. ** Data from Simplemaps.com.**
- Longitude: Longitude of the zip code. Data from Simplemaps.com.

### Section 3 - Research Questions and Usage Scenarios

Persona Description:
Name: Sofía Ramirez
Age: 29
Occupation: Software Developer
Interests: Homeownership, community engagement, outdoor activities
Background: Sofia is in the market for her first home. She is a single mother with 4 children. She's worked remotely for the past two years and her contract gives her the ability to continue working remotely on a permanent basis, which has given her the flexibility to consider living in various cities. Sofia is looking for a city that not only offers affordable housing options but also a vibrant community and a good quality of life.

#### User Story:
Sofia is using the "DreamHouse" dashboard to find the perfect city and neighborhood for her first home purchase. Her goals include:

- [Explore] the housing market in different cities to find areas that fit her budget and lifestyle.
- [Compare] living spaces, prices, and amenities across various zip codes within her selected cities.
- [Evaluate] community factors like population density, median household income, and access to outdoor spaces.
- [Decide] on a city and neighborhood that best aligns with her personal and financial criteria.


#### Usage Scenario:

When Sofia logs onto the "DreamHouse" dashboard, she's greeted by a user-friendly interface that prompts her to select her preferences, such as desired state, city, price range, and home features like beds and baths.

The dashboard then presents Sofia with a curated list of cities that match her criteria. She starts by exploring the overall housing market features in each city, including average prices and living space sizes. The app provides interactive maps and charts that help Sofia visualize the data, making it easier for her to grasp the information.

Sofia utilizes the filtering feature on the "DreamHouse" dashboard to sequentially review the cities that fit her criteria. She focuses on analyzing the median household income and zip code density within each city to understand the community's lifestyle and economic status. Instead of amenities like parks and recreational areas, the dashboard offers insights into living space sizes and the balance between price and quality of housing, which are crucial for Sofia to determine the value and comfort of potential homes.

After narrowing down her choices to a few cities, Sofia dives deeper into specific neighborhoods within those cities. She examines detailed listings, including photos and descriptions of available properties, and reads about local schools, community events, and other relevant local information provided by the app.

Armed with comprehensive data and insights from the "DreamHouse" dashboard, Sofia feels confident in her decision-making process. She shortlists a few properties and neighborhoods and plans visits to see her potential dream homes in person. The dashboard has empowered her to make an informed decision based on a wide range of factors, bringing her one step closer to purchasing her dream home.

### Section 4 - App Sketch and Brief Description

The app's landing page features interactive widgets that present housing market analytics for major US cities. It includes a color-coded map showing average pricing by region. This map, alongside a bar graph - arranged in descending order of average home city prices and color-coded by state - and detailed numerical summaries of median prices, household income, and square footage, ranking of most common home type, and counts of bedrooms and bathrooms, updates to only consider homes that fit the user-selected filters. The filters include square footage and price range sliders, numerical range inputs for household income, discrete selectors for bedroom and bathroom counts, and dropdowns for state and city selections. Selecting a state zooms into the map to display color intensities based on city average prices, narrows the bar graph to that state's cities, and customizes the numerical summaries to reflect state-specific data. Further filtering by city refines the display to city zip codes, presents a single bar for the selected city, and adjusts summaries to be city-specific. Users can further explore the market by hovering their cursor over a desired bar or map region, where they'll find additional details through informative tooltips.

**[Link to Image](https://github.com/UBC-MDS/DSCI-532_2024_15_dreamhouse/blob/main/img/sketch.png)**
