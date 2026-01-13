from model import get_data, ScoreAnalyzer


def main():
    url = "https://docs.google.com/spreadsheets/d/1_Qh_v-AaoxoxK2nylHFKCTFduGWR2sQiXbeG11YqI5k/edit?usp=drivesdk"
    df = get_data(url, "student_scores.csv")
    analyzer = ScoreAnalyzer(df)
    analyzer.perform_regression()
    print()
    
    try:
        hours = float(input("Hours >> "))
        print(f"Predict score for {hours} hours: {analyzer.predict_score(hours)}\n")   
    except ValueError:
        print("Hours can onle be number!")
        
    
    
    
if __name__ == "__main__":
    main()