import matplotlib.pyplot as plt
import numpy as np

# Create subplots with complex layouts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [2, 1]})

# Plot 1: Customized line plot
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), color='#FF5733', linestyle='--', linewidth=2, marker='o', markersize=5, label='sin(x)')
ax1.set_title("Customized Line Plot", fontsize=14, pad=20)
ax1.set_xlabel("X-axis", fontweight='bold')
ax1.legend(loc='upper right', framealpha=0.5)
ax1.grid(True, linestyle=':', alpha=0.7)

# Plot 2: Annotated scatter plot
np.random.seed(42)
x_rand = np.random.rand(50)
y_rand = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)
scatter = ax2.scatter(x_rand, y_rand, c=colors, s=sizes, alpha=0.6, cmap='viridis')
ax2.annotate('Outlier', xy=(x_rand[10], y_rand[10]), xytext=(0.2, 0.8),
             arrowprops=dict(facecolor='black', shrink=0.05))
fig.colorbar(scatter, ax=ax2, label='Color Intensity')

plt.tight_layout()
plt.show()