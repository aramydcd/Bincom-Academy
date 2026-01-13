from model import get_data, ScoreAnalyzer


url = "https://docs.google.com/spreadsheets/d/1_Qh_v-AaoxoxK2nylHFKCTFduGWR2sQiXbeG11YqI5k/edit?usp=drivesdk"
df = get_data(url, "student_score.csv")
analyzer = ScoreAnalyzer(df)
analyzer.perform_regression()
print(f"Predict score for 9.25 hours: {analyzer.predict_score(9.25)}")