import pandas as pd
import os

# File paths
file_paths = {
    "LanSweeper": "/Users/nobleyiga/PycharmProjects/NETWORK_PROJECT/files/LanSweeper_AllComputers_report.csv",
    "WSUS": "/Users/nobleyiga/PycharmProjects/NETWORK_PROJECT/files/WSUS_cleaned_output.csv",
    "Wazuh": "/Users/nobleyiga/PycharmProjects/NETWORK_PROJECT/files/Wazuh_AllAgents.csv",
    "Active_Dir_File1": "/Users/nobleyiga/PycharmProjects/NETWORK_PROJECT/files/file1.csv"
}

dfs = {name: pd.read_csv(path) for name, path in file_paths.items()}

# Standardize column name
for name, df in dfs.items():
    df.columns = df.columns.str.strip().str.lower()

# unique computer names from all files
all_computers = set()
for df in dfs.values():
    all_computers.update(df["name"].dropna().unique())

# DataFrame for missing systems
missing_data = pd.DataFrame({"name": list(all_computers)})

# Mark presence in each system
for system, df in dfs.items():
    missing_data[system] = missing_data["name"].apply(lambda x: "✔" if x in df["name"].values else "✖")

# Save CSV file
output_path = "/Users/nobleyiga/PycharmProjects/NETWORK_PROJECT/files/missing_systems_report.xlsx"
missing_data.to_csv(output_path, index=False)

print(f"Missing systems report saved to: {output_path}")