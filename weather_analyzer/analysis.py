import matplotlib.pyplot as plt

def analyze_data(df, column=None):
    print("\n📊 WEATHER ANALYSIS REPORT")
    print("=" * 40)

    print("\n📁 Available columns:")
    print(list(df.columns))

    # Detect column
    if column and column in df.columns:
        temp_col = column
    else:
        temp_col = df.select_dtypes(include='number').columns[0]

    print(f"\n🌡️ Using column: {temp_col}")

    avg_temp = df[temp_col].mean()
    max_temp = df[temp_col].max()
    min_temp = df[temp_col].min()

    print("\n📈 Statistics:")
    print(f"➡ Average Temperature : {avg_temp:.2f}")
    print(f"⬆ Max Temperature     : {max_temp}")
    print(f"⬇ Min Temperature     : {min_temp}")

    # Trend detection
    trend = df[temp_col].diff().mean()

    print("\n📉 Trend:")
    if trend > 0:
        print("📈 Increasing trend")
    elif trend < 0:
        print("📉 Decreasing trend")
    else:
        print("➡ Stable")

    # Plot
    try:
        plt.figure()
        plt.plot(df[temp_col])
        plt.title("Temperature Trend")
        plt.xlabel("Records")
        plt.ylabel(temp_col)
        plt.grid()
        plt.show()
    except Exception as e:
        print("❌ Plotting failed:", e)