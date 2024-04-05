# Reflection

## Implementations

Adhering to our design, the dashboard includes state and city selection dropdowns, square footage, and price range sliders, complemented by sliders for household income and bedroom and bathroom counts - these were consciously modified from input and discrete selectors for improved user experience given that sliders offer a more intuitive and continuous range of selections, allowing users to more accurately define their search criteria. Per our sketch, our dashboard has a descending order bar graph, presenting the average city home prices and color-coded by state alongside detailed numerical summaries of mean price, living space, average number of beds and baths, and household incomes, which dynamically respond and match the user-selected filters. Moreover, the dashboard shows a color-coded map.

Detailed subtitles for the numerical summaries, including range indicators, are yet to be implemented (E.g., Adding max and min values to the median household income numerical summary). Planned refinements include adjusting filter ranges to more accurately represent our user persona, as our target audience could perceive the current ranges as overwhelming.

The map's functionality remains in development. Currently, the map updates when a state is selected from the dropdown; however, we aim to have it respond to other filters and be capable of zooming in to show zip code-level data. We also plan to enhance the map with detailed tooltips, similar to the one in our bar chart.

## Differences from the Proposal & Justifications for Changes

The 'type of home' feature was not added to our dashboard given that our data set is skewed toward certain home types, making it inefficient to add it as a filter. Consequently, it has been excluded from our numerical summaries. During the development phase, we performed feature engineering to add a new metric - price per square foot - as an additional filter and numerical summary. Moreover, the map is no longer color-coded by average house pricing by region, rather it is colored by our new engineered feature, price per square foot by region. We believed this implementation was a good idea given that it provides a more granular understanding of value across different areas, enhancing comparability for users. Moreover, our map's functionality has evolved; it now zooms into states on mouse clicks, increasing interactivity and user engagement. 

## Acknowledgment of Current Dashboard Limitations

-   We recognize our filters' sliders currently display markers that may seem overcrowded. We are deliberating on the optimal marker representation that aligns with our user persona. 

-   A challenge we are facing is when selecting a state and then a city, the dropdown does not reset when another state is chosen, requiring a return to 'all' before reselection.

-   Cities sharing names across different states result in a shared bar on the graph, distinguished only by color - this ambiguity is on our radar for potential redesign to mitigate user confusion. 

## Explanation of Deviations from Visualization Best Practices

The map utilizes a color gradient from yellow to purple to represent pricing, which breaks from traditional best practices of having a light/white color in the middle of the range but creates an intuitive spectrum from 'hot' (expensive) -yellow- to 'cool' (cheaper) -purple- regions. Further, as taught in 531, we ensured to group cities of the same state by color in our bar graph. However, some state colors currently share the same colors given the vast number of states and cities - the bar graph could not conform to a fixed color palette without sacrificing clarity. This issue is further addressed in the next paragraph. 

## Reflection on Limitations and Potential Enhancements

The main limitations faced by our team included the time we had to create the dashboard and the nature of our data set - our data spans over only one month and has incomplete state coverage. Future improvements will focus on fine-tuning aesthetics. Mainly, we will experiment with aligning color schemes across the map and bar graph for visual consistency or find a color pallet that allows for good differentiation between states in the bar graph.
