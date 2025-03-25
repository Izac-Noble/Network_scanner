import pandas as pd

# File paths
input_file = "/files/WSUS_AllComputers_ComputerStatus.csv"  # Update this
output_file = "/files/WSUS_cleaned_output.csv"  # Update name as needed

# Load CSV file
df = pd.read_csv(input_file)

# Remove ".cmc.edu" from all values
df = df.applymap(lambda x: x.replace(".cmc.edu", "") if isinstance(x, str) else x)

# Save cleaned data to a new CSV file
df.to_csv(output_file, index=False)

print(f"✅ Cleaning complete! Saved as: {'WSUS_cleaned_output.csv'}")