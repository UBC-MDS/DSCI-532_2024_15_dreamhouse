from dash.dependencies import Input, Output, State
from src.data import df

def register_summary_callbacks(app):
    @app.callback(
        Output('median-household-income-display', 'children'),
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value'),
        Input('square-footage-slider', 'value'),
        Input('price-range-slider', 'value'),
        Input('ppsf-range-slider', 'value'),
        Input('hi-range-slider', 'value'),
        Input('beds-last-update', 'children'),  
        Input('baths-last-update', 'children'),  
        ],
            State('beds-min-input', 'value'),
            State('beds-max-input', 'value'),
            State('baths-min-input', 'value'),
            State('baths-max-input', 'value')
        )
    def update_median_income_display(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds_update, baths_update, beds_min, beds_max, baths_min, baths_max):
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

        filtered_df = filtered_df[(filtered_df['Beds'] >= beds_min) & (filtered_df['Beds'] <= beds_max)]
        filtered_df = filtered_df[(filtered_df['Baths'] >= baths_min) & (filtered_df['Baths'] <= baths_max)]

        # Compute the median of the "Median Household Income" column for the filtered DataFrame
        median_income = filtered_df['Median Household Income']. median()

        # Return the formatted median value for display
        return f"Median Household Income: ${median_income:,.0f}"

    @app.callback(
        Output('median-living-space', 'children'),
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value'),
        Input('square-footage-slider', 'value'),
        Input('price-range-slider', 'value'),
        Input('ppsf-range-slider', 'value'),
        Input('hi-range-slider', 'value'),
        Input('beds-last-update', 'children'),  
        Input('baths-last-update', 'children'),  
        ],
            State('beds-min-input', 'value'),
            State('beds-max-input', 'value'),
            State('baths-min-input', 'value'),
            State('baths-max-input', 'value')
        )
    def update_median_square_footage(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds_update, baths_update, beds_min, beds_max, baths_min, baths_max):
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

        filtered_df = filtered_df[(filtered_df['Beds'] >= beds_min) & (filtered_df['Beds'] <= beds_max)]
        filtered_df = filtered_df[(filtered_df['Baths'] >= baths_min) & (filtered_df['Baths'] <= baths_max)]

        # Compute the median of the "Living Space" column for the filtered DataFrame
        median_square_footage = filtered_df['Living Space'].median()

        # Return the formatted median value for display
        return f"Median Living Space: {median_square_footage:,.0f} SqFt"


    @app.callback(
        Output('avg-num-baths', 'children'),
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value'),
        Input('square-footage-slider', 'value'),
        Input('price-range-slider', 'value'),
        Input('ppsf-range-slider', 'value'),
        Input('hi-range-slider', 'value'),
        Input('beds-last-update', 'children'),  
        Input('baths-last-update', 'children'),  
        ],
            State('beds-min-input', 'value'),
            State('beds-max-input', 'value'),
            State('baths-min-input', 'value'),
            State('baths-max-input', 'value')
        )
    def update_avg_num_baths(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds_update, baths_update, beds_min, beds_max, baths_min, baths_max):
        # Filter the DataFrame based on the inputs (similar to the bar graph update function)
        filtered_df = df.copy()
        
        if state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
            if city != 'All':
                filtered_df = filtered_df[filtered_df['City'] == city]
                groupby_col = 'Zip Code'
                bar_title = 'Average House Pricing by Zip Code'
                use_color = False 
            else:
                groupby_col = 'City'
                bar_title = 'Average House Pricing by City'
                use_color = True
                color_col = 'City'
        else:
            groupby_col = 'State'
            bar_title = 'Average House Pricing by State'
            use_color = True
            color_col = 'State'
        
        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
        
        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        filtered_df = filtered_df[(filtered_df['Beds'] >= beds_min) & (filtered_df['Beds'] <= beds_max)]
        
        filtered_df = filtered_df[(filtered_df['Baths'] >= baths_min) & (filtered_df['Baths'] <= baths_max)]
        
        # Compute the median of the "Median Household Income" column for the filtered DataFrame
        avg_num_baths = filtered_df['Baths'].median()
        
        # Return the formatted median value for display
        return f"Median Number of Baths: {avg_num_baths:,.0f}"

    # statistical summary 'median house price'
    @app.callback(
        Output('median-price-display', 'children'),  
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value'),
        Input('square-footage-slider', 'value'),
        Input('price-range-slider', 'value'),
        Input('ppsf-range-slider', 'value'),
        Input('hi-range-slider', 'value'),
        Input('beds-last-update', 'children'),  
        Input('baths-last-update', 'children'),  
        ],
            State('beds-min-input', 'value'),
            State('beds-max-input', 'value'),
            State('baths-min-input', 'value'),
            State('baths-max-input', 'value')
        )
    def update_median_price(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds_update, baths_update, beds_min, beds_max, baths_min, baths_max):
        filtered_df = df.copy()
        
        if state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
            if city != 'All':
                filtered_df = filtered_df[filtered_df['City'] == city]
                groupby_col = 'Zip Code'
                bar_title = 'Average House Pricing by Zip Code'
                use_color = False 
            else:
                groupby_col = 'City'
                bar_title = 'Average House Pricing by City'
                use_color = True
                color_col = 'City'
        else:
            groupby_col = 'State'
            bar_title = 'Average House Pricing by State'
            use_color = True
            color_col = 'State'
        
        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
        
        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        filtered_df = filtered_df[(filtered_df['Beds'] >= beds_min) & (filtered_df['Beds'] <= beds_max)]
        
        filtered_df = filtered_df[(filtered_df['Baths'] >= baths_min) & (filtered_df['Baths'] <= baths_max)]
        
        median_price = filtered_df['Price'].median()
        
        return f"Median Price: ${median_price:,.0f}"


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
        Input('beds-last-update', 'children'),  
        Input('baths-last-update', 'children'),  
        ],
            State('beds-min-input', 'value'),
            State('beds-max-input', 'value'),
            State('baths-min-input', 'value'),
            State('baths-max-input', 'value')
        )
    def update_median_price_per_sqft(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds_update, baths_update, beds_min, beds_max, baths_min, baths_max):
        filtered_df = df.copy()
        if state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
            if city != 'All':
                filtered_df = filtered_df[filtered_df['City'] == city]
                groupby_col = 'Zip Code'
                bar_title = 'Average House Pricing by Zip Code'
                use_color = False 
            else:
                groupby_col = 'City'
                bar_title = 'Average House Pricing by City'
                use_color = True
                color_col = 'City'
        else:
            groupby_col = 'State'
            bar_title = 'Average House Pricing by State'
            use_color = True
            color_col = 'State'
        
        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
        
        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        filtered_df = filtered_df[(filtered_df['Beds'] >= beds_min) & (filtered_df['Beds'] <= beds_max)]
        
        filtered_df = filtered_df[(filtered_df['Baths'] >= baths_min) & (filtered_df['Baths'] <= baths_max)]
        
        median_price_per_sqft = filtered_df['Price per SqFt'].median()
        
        return f"Median Price per SqFt: ${median_price_per_sqft:,.0f}"


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
        Input('beds-last-update', 'children'),  
        Input('baths-last-update', 'children'),  
        ],
            State('beds-min-input', 'value'),
            State('beds-max-input', 'value'),
            State('baths-min-input', 'value'),
            State('baths-max-input', 'value')
        )
    def update_average_beds(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds_update, baths_update, beds_min, beds_max, baths_min, baths_max):
        filtered_df = df.copy()
        if state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
            if city != 'All':
                filtered_df = filtered_df[filtered_df['City'] == city]
                groupby_col = 'Zip Code'
                bar_title = 'Average House Pricing by Zip Code'
                use_color = False 
            else:
                groupby_col = 'City'
                bar_title = 'Average House Pricing by City'
                use_color = True
                color_col = 'City'
        else:
            groupby_col = 'State'
            bar_title = 'Average House Pricing by State'
            use_color = True
            color_col = 'State'
        
        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
        
        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        filtered_df = filtered_df[(filtered_df['Beds'] >= beds_min) & (filtered_df['Beds'] <= beds_max)]
        
        filtered_df = filtered_df[(filtered_df['Baths'] >= baths_min) & (filtered_df['Baths'] <= baths_max)]
        
        average_beds = filtered_df['Beds'].median()
        
        return f"Median number of Beds: {average_beds:,.0f}"  
