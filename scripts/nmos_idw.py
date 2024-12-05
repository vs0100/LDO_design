import pandas as pd
import matplotlib.pyplot as plt
import re

# Prompt the user to enter the CSV file path
file_path = 'ptm045\\nmos_ltspice\idw.csv'

try:
    # Read the CSV file
    data = pd.read_csv(file_path)
    
    # Check if there are at least two columns
    if data.shape[1] < 2:
        print("The CSV file must contain at least two columns.")
    else:
        # Determine the number of column pairs
        num_pairs = data.shape[1] // 2
        
        plt.figure(figsize=(10, 7))
        
        # Loop through each pair of columns and plot the curves
        for i in range(num_pairs):
            x = data.iloc[:, 2 * i]      # X data (even-indexed column)
            y = data.iloc[:, 2 * i + 1]  # Y data (odd-indexed column)

            # Extract the legend value from the column name
            column_name = y.name if isinstance(y.name, str) else str(y.name)
            match = re.search(r'l\s+([0-9.eE+-]+)', column_name)
            
            if match:
                # Convert the scientific notation to an absolute value
                legend_value = float(match.group(1)) * 1e9
                # legend_value = int(round(legend_value))  # Convert to integer
            else:
                legend_value = f"Curve {i + 1}"  # Fallback
            
            # Plot the curve
            plt.plot(x, y, label=f"l_nmos = {legend_value} nm", linestyle='-')
        
        # Add plot labels, legend, and grid
        plt.title("nid_w vs ngm_id")
        plt.xlabel("gm/Id")
        plt.ylabel("id/w")
        plt.legend()
        plt.grid(True)
        plt.show()
except FileNotFoundError:
    print("The specified file was not found. Please check the path and try again.")
except pd.errors.EmptyDataError:
    print("The file is empty. Please provide a valid CSV file.")
except Exception as e:
    print(f"An error occurred: {e}")
