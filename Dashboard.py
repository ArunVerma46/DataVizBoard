import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.arange(1, 6)
sales = [200, 400, 300, 500, 600]
profit = [20, 50, 30, 70, 90]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Business Dashboard', fontsize=16)

# Plot 1: Bar Chart
axs[0, 0].bar(x, sales, color='skyblue')
axs[0, 0].set_title('Sales per Day')
axs[0, 0].set_xlabel('Day')
axs[0, 0].set_ylabel('Sales')

# Plot 2: Line Graph
axs[0, 1].plot(x, profit, marker='o', color='green')
axs[0, 1].set_title('Profit per Day')
axs[0, 1].set_xlabel('Day')
axs[0, 1].set_ylabel('Profit')

# Plot 3: Pie Chart
axs[1, 0].pie(sales, labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], autopct='%1.1f%%')
axs[1, 0].set_title('Sales Distribution')

# Plot 4: Scatter Plot
axs[1, 1].scatter(sales, profit, color='red')
axs[1, 1].set_title('Sales vs Profit')
axs[1, 1].set_xlabel('Sales')
axs[1, 1].set_ylabel('Profit')

plt.tight_layout()
plt.show()
