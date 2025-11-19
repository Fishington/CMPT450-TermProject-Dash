from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

# Incorporate data
df = pd.read_excel(r"C:\Uni_Macewan\_Fall 2025\CMPT450\games_excel.xlsx")

# Initialize the app
app = Dash()

app.layout = [
    html.Div(children='My First App with Data'),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field": i} for i in df.columns]
    )
]

if __name__ == '__main__':
    app.run(debug=True)
