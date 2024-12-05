import matplotlib.pyplot as plt

# File path to the .txt file
file_path = "Plots/LDO_45nm_int_90_Tr.txt"  # Replace with your actual file path

# Initialize lists to store the data
time = []
v_out = []

# Read the data from the file
try:
    with open(file_path, 'r') as file:
        # Skip the header line
        header = file.readline()
        
        # Read and parse each line
        for line in file:
            columns = line.strip().split('\t')
            time.append(float(columns[0]))
            v_out.append(float(columns[1]))
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit(1)
except Exception as e:
    print(f"Error reading the file: {e}")
    exit(1)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time, v_out, label="V(out)", linewidth=1.5)
plt.title("Transient Response for Internally compensated LDO regulator")
plt.xlabel("Time (s)")
plt.ylabel("V(out) (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
