import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(df, column=None):
    print("\n WEATHER ANALYSIS REPORT")
    print("=" * 50)

    print(f"\n Total Records: {len(df)}")

    print("\n Available columns:")
    print(list(df.columns))

    # Detect column
    if column and column in df.columns:
        temp_col = column
    else:
        temp_col = df.select_dtypes(include='number').columns[0]

    print(f"\n Using column: {temp_col}")

    # Basic stats
    avg_temp = df[temp_col].mean()
    max_temp = df[temp_col].max()
    min_temp = df[temp_col].min()
    std_dev = df[temp_col].std()
    variance = df[temp_col].var()

    print("\n Statistics:")
    print(f" Average Temperature : {avg_temp:.2f}")
    print(f" Max Temperature     : {max_temp:.2f}")
    print(f" Min Temperature     : {min_temp:.2f}")
    print(f" Standard Deviation : {std_dev:.2f}")
    print(f" Variance           : {variance:.2f}")

    # Moving Average (Trend Replacement)
    window = 50
    df["moving_avg"] = df[temp_col].rolling(window=window).mean()

    print("\n Trend (Moving Average):")
    if df["moving_avg"].iloc[-1] > df["moving_avg"].iloc[window]:
        print(" Increasing trend")
    else:
        print(" Decreasing trend")

    # Correlation
    numeric_cols = df.select_dtypes(include='number')
    correlation = numeric_cols.corr()[temp_col].sort_values(ascending=False)

    print("\n Correlation with other features:")
    print(correlation)

    # Linear Regression (simple)
    df = df.reset_index()
    df["index"] = df.index

    X = df["index"]
    y = df[temp_col]

    # Fit line: y = mx + b
    m, b = pd.Series(X).cov(y) / pd.Series(X).var(), y.mean() - (pd.Series(X).cov(y) / pd.Series(X).var()) * X.mean()

    df["prediction"] = m * X + b

    print("\n Linear Regression Model:")
    print(f"y = {m:.4f}x + {b:.2f}")

    # Predict next value
    next_x = len(df)
    next_prediction = m * next_x + b

    print(f" Next predicted value: {next_prediction:.2f}")

    # Plot
    try:
        plt.figure(figsize=(10, 5))

        # Handle date if available
        if "Formatted Date" in df.columns:
            df["Formatted Date"] = pd.to_datetime(df["Formatted Date"], utc=True).dt.tz_localize(None)
            x_axis = df["Formatted Date"]
            plt.xlabel("Date")
        else:
            x_axis = df["index"]
            plt.xlabel("Records")

        # Actual data
        plt.plot(x_axis, df[temp_col], label="Actual")

        # Moving average
        plt.plot(x_axis, df["moving_avg"], label="Moving Avg", linestyle="--")

        # Prediction line
        plt.plot(x_axis, df["prediction"], label="Prediction", linestyle=":")

        plt.ylabel(temp_col)
        plt.title("Temperature Analysis")
        plt.legend()
        plt.grid()

        plt.xticks(rotation=45)

        plt.savefig("temperature_analysis.png")
        print("\n Graph saved as temperature_analysis.png")

    except Exception as e:
        print(" Plotting failed:", e)
