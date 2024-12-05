import csv
import matplotlib.pyplot as plt
import numpy as np

# File path to the CSV file
csv_file_path = "Plots\\LDO_45nm_int_90_LG_h.txt"

# Initialize lists for storing frequency, magnitude, and phase
frequency = []
magnitude = []
phase = []

# Read the CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter='\t')  # Assuming tab-separated values
    next(csv_reader)  # Skip header row
    
    for row in csv_reader:
        # Extract data
        freq = float(row[0])
        mag_phase = row[1].strip("()").split(",")  # Remove parentheses and split
        mag = float(mag_phase[0].replace("dB", ""))
        ph = float(mag_phase[1].replace("°", ""))
        
        # Append data to lists
        frequency.append(freq)
        magnitude.append(mag)
        phase.append(ph)

# User-specified pole frequencies and their labels
pole_frequencies = [318.31, 318310, 2633000]  # Example pole frequencies (can be updated)
pole_labels = ['Wp1', 'Wugb', 'Wp2']  # Labels for the poles

# Find and annotate poles
pole_indices = [np.argmin(np.abs(np.array(frequency) - pole)) for pole in pole_frequencies]
pole_points = [(frequency[i], magnitude[i]) for i in pole_indices]

# Create the plot
fig, ax1 = plt.subplots()

# Plot magnitude
color = 'tab:blue'
ax1.set_xlabel('Frequency (Hz)')
ax1.set_ylabel('Magnitude (dB)', color=color)
ax1.plot(frequency, magnitude, color=color, linestyle='--', label="Magnitude (dB)")
ax1.set_xscale('log')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(which='both', linestyle='--', linewidth=0.5)
ax1.legend(loc='lower left')

# Annotate poles with a cross (X) and customized offsets
for (freq, mag), label in zip(pole_points, pole_labels):
    ax1.scatter(freq, mag, color='black', marker='x', s=100)
    if label == 'Wp1':
        # Custom placement for Wp1
        x_offset = -0.1 * freq  # Horizontal offset for Wp1
        y_offset = -10  # Vertical offset for Wp1
    else:
        # Default placement for other poles
        x_offset = 0.05 * freq
        y_offset = 7
    ax1.text(freq + x_offset, mag + y_offset, f'{label}\n({freq:.2f} Hz)', 
             fontsize=8, color='black', ha='left', va='bottom')

# Create a twin y-axis for the phase plot
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Phase (°)', color=color)
ax2.plot(frequency, phase, linestyle='-.', color=color, label="Phase (°)")
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

# Final adjustments
plt.title('Loop Gain Bode Plot for externally compensated LDO with heavy load current (10 mA)')
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
