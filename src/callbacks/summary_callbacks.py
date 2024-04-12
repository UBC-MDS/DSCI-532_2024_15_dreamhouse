from dash.dependencies import Input, Output
from data import df

def register_summary_callbacks(app):
    @app.callback(
        Output('median-household-income-display', 'children'),
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value'),
        Input('square-footage-slider', 'value'),
        Input('price-range-slider', 'value'),
        Input('ppsf-range-slider', 'value'),
        Input('hi-range-slider', 'value'),
        Input('beds-min-input', 'value'),
        Input('beds-max-input', 'value'),
        Input('baths-min-input', 'value'),
        Input('baths-max-input', 'value')])
    def update_median_income_display(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds, baths):
        # Filter the DataFrame based on the inputs (similar to the bar graph update function)
        filtered_df = df.copy()
        
        if state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
        
        if city != 'All':
            filtered_df = filtered_df[filtered_df['City'] == city]
        
        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]

        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        min_beds, max_beds = beds
        filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
        
        min_baths, max_baths = baths
        filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]
        
        # Compute the median of the "Median Household Income" column for the filtered DataFrame
        median_income = filtered_df['Median Household Income'].median()
        
        # Return the formatted median value for display
        return f"Median Household Income: ${median_income:.2f}"


    @app.callback(
        Output('median-living-space', 'children'),
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value'),
        Input('square-footage-slider', 'value'),
        Input('price-range-slider', 'value'),
        Input('ppsf-range-slider', 'value'),
        Input('hi-range-slider', 'value'),
        Input('beds-slider', 'value'),
        Input('baths-slider', 'value')]
    )
    def update_median_square_footage(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds, baths):
        # Filter the DataFrame based on the inputs (similar to the bar graph update function)
        filtered_df = df.copy()
        
        if state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
        
        if city != 'All':
            filtered_df = filtered_df[filtered_df['City'] == city]
        
        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]

        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        min_beds, max_beds = beds
        filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
        
        min_baths, max_baths = baths
        filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]
        
        # Compute the median of the "Median Household Income" column for the filtered DataFrame
        median_square_footage = filtered_df['Living Space'].median()
        
        # Return the formatted median value for display
        return f"Median Living Space: {median_square_footage:.2f} SqFt"


    @app.callback(
        Output('avg-num-baths', 'children'),
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value'),
        Input('square-footage-slider', 'value'),
        Input('price-range-slider', 'value'),
        Input('ppsf-range-slider', 'value'),
        Input('hi-range-slider', 'value'),
        Input('beds-slider', 'value'),
        Input('baths-slider', 'value')]
    )
    def update_avg_num_baths(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds, baths):
        # Filter the DataFrame based on the inputs (similar to the bar graph update function)
        filtered_df = df.copy()
        
        if state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
        
        if city != 'All':
            filtered_df = filtered_df[filtered_df['City'] == city]
        
        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]

        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        min_beds, max_beds = beds
        filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
        
        min_baths, max_baths = baths
        filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]
        
        # Compute the median of the "Median Household Income" column for the filtered DataFrame
        avg_num_baths = filtered_df['Baths'].mean()
        
        # Return the formatted median value for display
        return f"Average Number of Baths: {avg_num_baths:.2f}"

    # statistical summary 'median house price'
    @app.callback(
        Output('median-price-display', 'children'),  
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value'),
        Input('square-footage-slider', 'value'),
        Input('price-range-slider', 'value'),
        Input('ppsf-range-slider', 'value'),
        Input('hi-range-slider', 'value'),
        Input('beds-slider', 'value'),
        Input('baths-slider', 'value')])
    def update_median_price(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds, baths):
        filtered_df = df.copy()
        
        if state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
        
        if city != 'All':
            filtered_df = filtered_df[filtered_df['City'] == city]
        
        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]

        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        min_beds, max_beds = beds
        filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
        
        min_baths, max_baths = baths
        filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]
        
        median_price = filtered_df['Price'].median()
        
        return f"Median Price: ${median_price:,.2f}"


    # +
    # statistical summary 'median price per SqFt'

    @app.callback(
        Output('median-price-per-sqft-display', 'children'),
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value'),
        Input('square-footage-slider', 'value'),
        Input('price-range-slider', 'value'),
        Input('ppsf-range-slider', 'value'),
        Input('hi-range-slider', 'value'),
        Input('beds-slider', 'value'),
        Input('baths-slider', 'value')])
    def update_median_price_per_sqft(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds, baths):
        filtered_df = df.copy()
        if state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
        
        if city != 'All':
            filtered_df = filtered_df[filtered_df['City'] == city]
        
        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]

        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        min_beds, max_beds = beds
        filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
        
        min_baths, max_baths = baths
        filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]
        
        median_price_per_sqft = filtered_df['Price per SqFt'].median()
        
        return f"Median Price per SqFt: ${median_price_per_sqft:,.2f}"


    # -

    # statistical summary 'avergae beds'
    @app.callback(
        Output('average-beds-display', 'children'),
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value'),
        Input('square-footage-slider', 'value'),
        Input('price-range-slider', 'value'),
        Input('ppsf-range-slider', 'value'),
        Input('hi-range-slider', 'value'),
        Input('beds-slider', 'value'),
        Input('baths-slider', 'value')])
    def update_average_beds(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds, baths):
        filtered_df = df.copy()
        if state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
        
        if city != 'All':
            filtered_df = filtered_df[filtered_df['City'] == city]
        
        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]

        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        min_beds, max_beds = beds
        filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
        
        min_baths, max_baths = baths
        filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]
        
        average_beds = filtered_df['Beds'].mean()
        
        return f"Average Beds: {average_beds:.2f}"  