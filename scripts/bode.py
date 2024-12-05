import csv
import matplotlib.pyplot as plt
import numpy as np

# File path to the CSV file
csv_file_path = "Plots\LDO_45nm_ext_90_CL_h.txt"

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

# Find the index of the frequency closest to 1 Hz
closest_index = np.argmin(np.abs(np.array(frequency) - 1))
freq_closest = frequency[closest_index]
mag_closest = magnitude[closest_index]

# Convert frequency to log scale for plotting
frequency_log = np.log10(frequency)

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

# Add text annotation for the initial value of magnitude
ax1.text(freq_closest, mag_closest + 2, f'{mag_closest:.2f} dB', 
         fontsize=10, color='blue', ha='center')

# Create a twin y-axis for the phase plot
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Phase (°)', color=color)
ax2.plot(frequency, phase, linestyle='-.', color=color, label="Phase (°)")
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

# Final adjustments
plt.title('Closed Loop PSRR Bode Plot for externally compensated LDO with light load current (2 mA)')
plt.show()
