from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load sales data
data = pd.read_csv('data/sales_data.csv')

@app.route('/')
def dashboard():
    # Generate bar chart for sales by region
    bar_chart = px.bar(data, x='Region', y='Sales', color='Region', 
                       title="Sales by Region", text='Sales')

    # Generate line chart for profit trends over time
    data['Date'] = pd.to_datetime(data['Date'])  # Convert Date to datetime
    line_chart = px.line(data, x='Date', y='Profit', color='Region', 
                         title="Profit Trends Over Time", markers=True)

    # Generate pie chart for discount distribution by product
    pie_chart = px.pie(data, names='Product', values='Discount', 
                       title="Discount Distribution by Product")

    # Generate scatter plot for sales vs. profit
    scatter_chart = px.scatter(data, x='Sales', y='Profit', color='Region', size='Units Sold',
                                hover_data=['Product'], title="Sales vs. Profit Analysis")

    # Render dashboard with charts
    return render_template(
        'dashboard.html',
        bar_chart=bar_chart.to_html(),
        line_chart=line_chart.to_html(),
        pie_chart=pie_chart.to_html(),
        scatter_chart=scatter_chart.to_html()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
    