import matplotlib.pyplot as plt

# Data
gm_id = [10, 12, 15]  # gm/Id values
overall_area = [13.3979, 19.781, 35.769]  # Overall area in μm^2

# Plot
plt.figure(figsize=(8, 6))
plt.plot(gm_id, overall_area, marker='o', linestyle='-', linewidth=2, markersize=8)

# Labels and title
plt.title('Overall Area vs gm/Id', fontsize=16)
plt.xlabel('gm/Id', fontsize=14)
plt.ylabel('Overall Area (μm²)', fontsize=14)

# Grid and display
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
