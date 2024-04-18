from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
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
                bar_title = 'Median House Pricing by Zip Code'
                use_color = False 
            else:
                groupby_col = 'City'
                bar_title = 'Median House Pricing by City'
                use_color = True
                color_col = 'City'
        else:
            groupby_col = 'State'
            bar_title = 'Median House Pricing by State'
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
        
        if not filtered_df.empty:
            avg_prices = filtered_df.groupby(groupby_col, as_index=False)['Price'].agg(['median', 'count'])
            if use_color:
                fig = px.bar(
                    avg_prices,
                    x='median',
                    y=groupby_col,
                    color='median',
                    title=bar_title,
                    orientation='h',
                    hover_data={'median': True, 'count': True}, 
                    labels={'median': 'Median Price', 'City': 'City', 'State': 'State', 'count': 'Count'},
                    color_continuous_scale='Plasma',
                )
                fig.update_layout(coloraxis_showscale=False)  
            else:
                fig = px.bar(
                    avg_prices,
                    x='median',
                    y=groupby_col,
                    title=bar_title,
                    orientation='h',
                    hover_data={'median': True, 'count': True}, 
                    labels={'median': 'Median Price', 'City': 'City', 'State': 'State', 'count': 'Count'}
                )
            fig.update_layout(
                xaxis_title='Median Price',
                yaxis_title=None,
                yaxis={'categoryorder': 'total descending'},
            )
            fig.update_yaxes(tickmode='array', tickvals=avg_prices[groupby_col])
            fig.update(layout_showlegend=False)

        else:
            fig = go.Figure()
            fig.update_layout(
                title='No Data Available for Selected Filters',
                xaxis={'visible': False},
                yaxis={'visible': False}
            )
        
        fig.update_yaxes(tickfont=dict(size=7.5))
        
        return fig

