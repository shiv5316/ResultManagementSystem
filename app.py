from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("student_results.csv")
@app.route('/')
def index():
    return render_template('dashboard.html', tables=[df.to_html(classes='data', header="true")], titles=df.columns.values)
if __name__ == "__main__":
    app.run(debug=True)
