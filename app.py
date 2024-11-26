from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load sales data
data = pd.read_csv('data/sales_data.csv')

@app.route('/')
def dashboard():
    # Generate bar chart
    bar_chart = px.bar(data, x='Region', y='Sales', color='Region', title="Sales by Region")
    
    # Generate line chart
    line_chart = px.line(data, x='Date', y='Profit', title="Profit Over Time")
    
    # Generate pie chart
    pie_chart = px.pie(data, names='Product', values='Discount', title="Discount Distribution")
    
    # Render dashboard with charts
    return render_template('dashboard.html', bar_chart=bar_chart.to_html(),
                           line_chart=line_chart.to_html(),
                           pie_chart=pie_chart.to_html())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)