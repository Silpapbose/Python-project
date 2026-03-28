import matplotlib.pyplot as plt

def analyze_data(df):
    print("\n--- Weather Analysis ---\n")

    print("Columns:", df.columns)

    # Adjust column names if needed
    temp_col = "temperature" if "temperature" in df.columns else df.columns[0]

    avg_temp = df[temp_col].mean()
    max_temp = df[temp_col].max()
    min_temp = df[temp_col].min()

    print(f"Average Temperature: {avg_temp:.2f}")
    print(f"Max Temperature: {max_temp}")
    print(f"Min Temperature: {min_temp}")

    # Plot
    try:
        plt.plot(df[temp_col])
        plt.title("Temperature Trend")
        plt.xlabel("Records")
        plt.ylabel("Temperature")
        plt.show()
    except Exception as e:
        print("Plotting failed:", e)