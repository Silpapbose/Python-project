from weather_analyzer.loader import load_data
from weather_analyzer.analysis import analyze_data

def main():
    df = load_data()

    if df is None:
        print("Failed to load dataset.")
        return

    analyze_data(df)

if __name__ == "__main__":
    main()