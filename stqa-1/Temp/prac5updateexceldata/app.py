from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load the data from the Excel file into a Pandas DataFrame
    df = pd.read_excel("prac5.xlsx")
    
    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict('records')
    
    # Render the HTML template and pass the data to it
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
