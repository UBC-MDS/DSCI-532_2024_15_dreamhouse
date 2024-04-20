# Reflection

## Implementations since last milestone

Since milestone 3, we have made significant improvements to our dashboard's usability and visual appeal. One of the key changes was altering the color scheme of our bar plot to match the map plot, enhancing the visual consistency across the dashboard. Additionally, we increased the map plot's size to make it more user-friendly and removed the legend from the bar plot since the city names directly on the plot already provide sufficient information.

We also refined the display of statistical summaries by removing decimals for a cleaner look and centering the text in their respective boxes. To improve user interaction, we moved the bar plot underneath the main map plot and addressed performance issues, resulting in a faster, more responsive dashboard. Furthermore, we implemented a message alert feature that informs users when their filter selections return no matching data.
A new confirm button was added to the filter section, allowing users to finalize their selections on desired bed and bath counts, thus preventing unintentional filter applications and enhancing user control.

## Differences from the Proposal

We continued to adhere to our project proposal while making necessary adjustments for practical implementation. For example, the integration of statistical summaries without decimals and the enhancement of the dashboard's layout were not originally outlined but proved essential for optimizing user experience.

## Acknowledgment of Current Dashboard Limitations

Our efforts have successfully addressed previous limitations, notably the functionality issues with California. However, a new challenge has emerged with the map's ability to accurately display all counties when selecting major cities like Chicago. This issue is traced back to inconsistencies in our dataset's 'fips' codes, which are crucial for mapping. We plan to enrich our dataset with additional data in the future, hoping to resolve these discrepancies and improve the map's accuracy.

## Deviations from Visualization Best Practices

In our design, we chose a color gradient that deviates from the best practices learned in class. The gradient ranges from yellow to purple, representing a spectrum of pricing that, while intuitive, does not include a neutral middle range color. This choice was intentional to create a more striking visual impact and aid in user interpretation of data.

## Reflection on Dashboard Strengths, Limitations, and Future Improvements
Our dashboard excels in providing an interactive and visually appealing experience, allowing users to navigate real estate data effortlessly. The current limitation with the 'fips' codes affects the display accuracy of counties on the map, which we aim to address by enhancing our dataset. Future improvements will focus on incorporating comprehensive geoJSON data for more detailed mapping and continuing to enhance the dashboard's performance and user interface. This will ensure our tool not only meets but exceeds user expectations for effective real estate analysis.
