import matplotlib.pyplot as plt

# File path to the .txt file
file_path = "Plots/LDO_45nm_90_Vdd.txt"  # Replace with your actual file path

# Initialize lists to store the data
v1 = []
v_out = []

# Read the data from the file
try:
    with open(file_path, 'r') as file:
        # Skip the header line
        header = file.readline()
        
        # Read and parse each line
        for line in file:
            columns = line.strip().split('\t')
            v1.append(float(columns[0]))  # First column: v1
            v_out.append(float(columns[1]))  # Second column: V(out)
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit(1)
except Exception as e:
    print(f"Error reading the file: {e}")
    exit(1)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(v1, v_out, label="V(out)", linewidth=1.5)
plt.title("Regulated Output Voltage vs VDD (Vin)")
plt.xlabel("V1 (V)")
plt.ylabel("V(out) (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
