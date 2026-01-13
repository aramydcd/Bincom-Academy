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
        # x = Hours (Independent ==> CAUSE), y = Scores (Dependent ==> EFFECT)
        x = self.df['hours']
        y = self.df['scores']
        
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
        # Attempt to fetch from Web
        export_url = url.replace('/edit?usp=drivesdk', '/export?format=csv')
        print("Fetched data from Google Sheets.")
        # return pd.read_csv(export_url)
        print(pd.read_csv(export_url))
    except Exception:
        # Fallback to Local CSV
        if os.path.exists(local_path):
            print("Web fetch failed. Loaded from local CSV.")
            return pd.read_csv(local_path)
        else:
            raise FileNotFoundError("Neither the URL nor the local file worked!")