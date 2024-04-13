from dash.dependencies import Input, Output
import plotly.express as px
from src.data import df

def register_bar_callbacks(app):
    @app.callback(
        Output('city-bar-graph', 'figure'),
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
    def update_city_bar_graph(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds_min, beds_max, baths_min, baths_max):
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
        
        Pastel_colors = px.colors.qualitative.Pastel
        alphabet_colors = px.colors.qualitative.Alphabet
        Dark_colors = px.colors.qualitative.Dark24
        Vivid_colors = px.colors.qualitative.Vivid
        combined_palette = Pastel_colors + alphabet_colors + Dark_colors + Vivid_colors # Created our own color palette :)
        
        if not filtered_df.empty:
            avg_prices = filtered_df.groupby(groupby_col, as_index=False)['Price'].agg(['mean', 'count'])
            if use_color:
                fig = px.bar(
                    avg_prices,
                    x='mean',
                    y=groupby_col,
                    color=color_col,
                    title=bar_title,
                    orientation='h',
                    hover_data={'mean': True, 'count': True}, 
                    labels={'mean': 'Average Price', 'City': 'City', 'State': 'State', 'count': 'Count'},
                    color_discrete_sequence=combined_palette #Mixed colors
                )
            else:
                fig = px.bar(
                    avg_prices,
                    x='mean',
                    y=groupby_col,
                    title=bar_title,
                    orientation='h',
                    hover_data={'mean': True, 'count': True}, 
                    labels={'mean': 'Average Price', 'City': 'City', 'State': 'State', 'count': 'Count'}
                )
            fig.update_layout(
                xaxis_title='Average Price',
                yaxis_title=groupby_col,
                yaxis={'categoryorder': 'total descending'},
                legend_title=groupby_col,
            )
            fig.update_yaxes(tickmode='array', tickvals=avg_prices[groupby_col])
            fig.update_layout(legend_font_size=14)

        else:
            fig = go.Figure()
            fig.update_layout(
                title='No Data Available for Selected Filters',
                xaxis={'visible': False},
                yaxis={'visible': False}
            )
        
        fig.update_yaxes(tickfont=dict(size=7.5))
        
        return fig

