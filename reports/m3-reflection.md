# Reflection

## Implementations since last week

Since milestone 2, we have fixed the overcrowded slider markers on the 'Median Household Income' slider by reducing the number of markers to 4, using the quartiles of the distribution. We felt reducing the number of markers was a good option as the slider also has a tooltip that displays the amount the user sets. We also added a 'Reset Custom Filters' button to make it easy to clear all the selections made by the user if they wish to restart and create a new combination of filter criteria. Another improvement we made this week was to fix the bar graph's legend colours by state so that there are no duplicates.

Since last week we have also implemented city and zip code levels to the map. Users can now click on a state in the map and watch as the map zooms in to that state to display the counties which have listings. They can then click on a county to see the map zoom in and display the various zip codes with house listings. We are working on a method of displaying points to show where the exact listings are within each zip code using latitude and longitude data. We are hoping this will be functional for milestone 4.

Finally, we created a new file structure in the repo with the goal keeping the app.py file clean and easily navigable. We removed all styling and functions and created the layout.py, components.py, and figure.py files to house our app's various features. All styling to these features are done within their own files while the layout.py file controls the app's layout. The app.py file now serves to instantiate the app and nothing more.

## Differences from the Proposal

The 'type of home' feature was not added to our dashboard given that our data set is skewed toward certain home types, making it inefficient to add it as a filter. Consequently, it has been excluded from our numerical summaries. During the development phase, we performed feature engineering to add a new metric - price per square foot - as an additional filter and numerical summary. Moreover, the map is no longer color-coded by average house pricing by region, rather it is colored by our new engineered feature, price per square foot by region. We believed this implementation was a good idea given that it provides a more granular understanding of value across different areas, enhancing comparability for users. Moreover, our map's functionality has evolved; it now zooms into states on mouse clicks, increasing interactivity and user engagement.

Since milestone 2, we have not diverged any further from the initial proposal.

## Acknowledgment of Current Dashboard Limitations

- We are currently dealing with a bug that is not allowing California to display city and zip code levels in the map. All other states work properly, the bug will be fixed for milestone 4.

- A challenge we are facing is when selecting a state and then a city, the dropdown does not reset when another state is chosen, requiring a return to 'all' before reselection.

- Cities sharing names across different states result in a shared bar on the graph, distinguished only by color - this ambiguity is on our radar for potential redesign to mitigate user confusion.

## Deviations from Visualization Best Practices

The map utilizes a color gradient from yellow to purple to represent pricing, which breaks from traditional best practices of having a light/white color in the middle of the range but creates an intuitive spectrum from 'hot' (expensive) -yellow- to 'cool' (cheaper) -purple- regions. Further, as taught in 531, we ensured to group cities of the same state by color in our bar graph. However, some state colors currently share the same colors given the vast number of states and cities - the bar graph could not conform to a fixed color palette without sacrificing clarity. This issue is further addressed in the next paragraph.

## Limitations and Potential Enhancements

The main limitations faced by our team included the time we had to create the dashboard and the nature of our data set - our data does not feature any geoJSON data, which we need to add certain features and layers to the map. Future improvements will focus on fine-tuning aesthetics. For milestone 4, we will be aiming to have the complete map functioning properly so that for any state, you can click and see the counties where there are house listings. You will then be able to click on a county and see the zip codes that have listings. This is all currently functional, except for California. We are also working on showing pins on the map for each house listing in a zip code based on latitude and longitude coordinates from the data. We are aiming to add this feature for milestone 4.