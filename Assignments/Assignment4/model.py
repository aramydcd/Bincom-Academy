import pandas as pd
import os
from scipy import stats

        
class ScoreAnalyzer:
    def __init__(self, data_frame):
        self.df = data_frame
        self.slope = None
        self.intercept = None
        self.r_value = None


    def perform_regression(self):
        # Data Cleaning: Force columns to be numeric, turning text/errors into 'NaN'
        self.df['Hours'] = pd.to_numeric(self.df['Hours'], errors='coerce')
        self.df['Scores'] = pd.to_numeric(self.df['Scores'], errors='coerce')

        # Drop any rows that now have 'NaN' (missing or bad data)
        self.df = self.df.dropna(subset=['Hours', 'Scores'])

        # x = Hours (Independent ==> CAUSE), y = Scores (Dependent ==> EFFECT)
        x = self.df['Hours']
        y = self.df['Scores']
        
        # The Math: y = mx + b ------> linear_reg = (slope * hours) + intercept
        res = stats.linregress(x, y)
        
        self.slope = res.slope
        self.intercept = res.intercept
        self.r_value = res.rvalue
        
        print(f"Regression Complete!")
        print(f"Slope: {self.slope:.2f}")
        print(f"Intercept: {self.intercept:.2f}")
        print(f"R-Squared: {self.r_value**2:.4f}")

    def predict_score(self, hours):
        # Using the formula y = mx + b
        prediction = (self.slope * hours) + self.intercept
        return prediction


def get_data(url, local_path):
    try:
        # Convert Google Edit link to Export link
        export_url = url.replace('/edit?usp=drivesdk', '/export?format=csv')
        df = pd.read_csv(export_url)
        print("Successfully fetched from Google Sheets.")
        return df        
    except Exception as e:
        # Fallback to Local CSV
        print(f"Network fetch failed ({e}). Checking local file...")
        if os.path.exists(local_path):
            print(f"Loading local file: {local_path}")
            return pd.read_csv(local_path)
        else:
            print(f"ERROR: Local file '{local_path}' not found in {os.getcwd()}")
            raise FileNotFoundError("Both Web and Local sources are unavailable.")
        
        
 