import argparse
from weather_analyzer.loader import load_data
from weather_analyzer.analysis import analyze_data

def main():
    print(" Starting Weather Analyzer...\n")

    parser = argparse.ArgumentParser(description="Weather Analyzer CLI")

    parser.add_argument(
        "--file",
        type=str,
        default="data/weather.csv",
        help="Path to CSV file"
    )

    parser.add_argument(
        "--column",
        type=str,
        default=None,
        help="Column to analyze"
    )

    args = parser.parse_args()

    df = load_data(args.file)

    if df is None:
        print(" Failed to load dataset.")
        return

    analyze_data(df, args.column)


if __name__ == "__main__":
    main()
