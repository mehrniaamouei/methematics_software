import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "پروژه 3.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

print(df.head())

x_column = df.columns[0]
y_columns = df.columns[1:]

plt.figure(figsize=(10, 6))
bar_width = 0.25
x = range(len(df[x_column]))

for i, col in enumerate(y_columns):
    plt.bar([p + i * bar_width for p in x], df[col], width=bar_width, label=col)

plt.xlabel("Data Size (KB)")
plt.ylabel("Execution Time (ms)")
plt.title("Bar Chart: Algorithm Performance Comparison")
plt.xticks([p + bar_width for p in x], df[x_column])
plt.legend()
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

plt.figure(figsize=(10, 6))
for col in y_columns:
    plt.plot(df[x_column], df[col], marker='o', label=col)

plt.xlabel("Data Size (KB)")
plt.ylabel("Execution Time (ms)")
plt.title("Line Chart: Execution Time vs Data Size")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

plt.figure(figsize=(8, 6))
data_to_plot = [df[col] for col in y_columns]
plt.boxplot(data_to_plot, labels=y_columns)

plt.xlabel("Algorithm")
plt.ylabel("Execution Time (ms)")
plt.title("Box Plot: Execution Time Distribution per Algorithm")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("boxplot.png")
plt.show()






file_path = "پروژه 3.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1", engine='openpyxl')

df['Size_KB'] = df.iloc[:, 0].str.extract('(\d+)').astype(int)

filtered_df = df[(df['Size_KB'] >= 100) & (df['Size_KB'] <= 600)]

algorithm_2_filtered = filtered_df["Alg.2"]

average_time = algorithm_2_filtered.mean()

print(f"Average execution time for Algorithm 2 (100KB to 600KB): {average_time:.2f} ms")