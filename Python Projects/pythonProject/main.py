import matplotlib.pyplot as plt
import numpy as np

# Data of Yellow Warblers weights
weights = [9.21, 9.05, 9.73, 9.43, 10.3, 9.68, 9.82, 9.73, 9.52, 9.53]

# Define the bin edges for intervals that are 0.2 wide with whole numbers on interval endpoints
bin_edges = np.arange(start=np.floor(min(weights)), stop=np.ceil(max(weights)), step=0.2)

# Calculate histogram data (frequency)
hist, bins = np.histogram(weights, bins=bin_edges)

# Probability densities for the right-hand axis (frequency divided by total observations and by bin width)
prob_density = hist / (sum(hist) * 0.2)

# Create the histogram plot
fig, ax1 = plt.subplots()

# Plot the frequencies
ax1.hist(weights, bins=bin_edges, alpha=0.7, color='blue', edgecolor='black')
ax1.set_xlabel('Weight (grams)')
ax1.set_ylabel('Frequency')
ax1.set_xticks(bin_edges)

# Create the second axis for estimated probability density
ax2 = ax1.twinx()
ax2.set_ylim(ax1.get_ylim())
ax2.set_yticks(hist)
ax2.set_yticklabels(np.round(prob_density, 2))
ax2.set_ylabel('Estimated Probability Density')

# Add grid lines for readability
ax1.grid(True)

# Show the plot
plt.show()
