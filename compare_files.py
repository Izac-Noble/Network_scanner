import pandas as pd
import os

def compare_files(file1_path, file2_path, output_dir="/Users/nobleyiga/PycharmProjects/NETWORK_PROJECT/files"):
    # This Loads CSV files
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # This Standardize's column names
    df1.columns = df1.columns.str.strip().str.lower()
    df2.columns = df2.columns.str.strip().str.lower()

    # Debug: Check if 'name' column exists
    if "name" not in df1.columns or "name" not in df2.columns:
        print("Error: One of the files is missing a 'name' column.")
        return

    # Check for IP addresses
    has_IP1 = "IP_address" in df1.columns
    has_IP2 = "IP_address" in df2.columns

    # Determine merge key
    merge_key = ["name"]
    if has_IP1 and has_IP2:
        merge_key.append("IP_address")

    # Perform merging to find matches
    merged_df = df1.merge(df2, on=merge_key, how="inner")

    # Find unmatched records in file1
    unmatched_df = df1[~df1["name"].isin(merged_df["name"])]

    # Extract filenames for naming output files
    file1_name = os.path.basename(file1_path).replace(".csv", "")
    file2_name = os.path.basename(file2_path).replace(".csv", "")

    # Define output file paths
    matched_records = os.path.join(output_dir, f"matched_{file1_name}_vs_{file2_name}.csv")
    unmatched_records = os.path.join(output_dir, f"unmatched_{file1_name}_vs_{file2_name}.csv")

    # Save results
    merged_df.to_csv(matched_records, index=False)
    unmatched_df.to_csv(unmatched_records, index=False)

    print(f"✅ Comparison complete.\nMatched records saved to: {matched_records}\nUnmatched records saved to: {unmatched_records}")

# Example usage
compare_files(
    "/Users/nobleyiga/PycharmProjects/NETWORK_PROJECT/files/file1.csv",
    "/Users/nobleyiga/PycharmProjects/NETWORK_PROJECT/files/LanSweeper_AllComputers_report.csv"
)