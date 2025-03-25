# Automated Inactive Computer Scanner

## 📌 Project Overview
This project automates the process of identifying inactive computers across an entire campus network. It replaces a manual spreadsheet-based approach, making the process more efficient and accurate. The program compares records from multiple systems to determine which computers are missing from certain databases and generates structured reports.

## 🔥 Features
- Scans and compares computer records from **Active Directory, WSUS, Lansweeper, Wazuh,** and other sources.
- Identifies **inactive or missing computers** based on name matching.
- Generates **CSV reports** highlighting matched and missing computers.
- Supports multiple input files with flexible comparison logic.
- Automates a previously manual process, improving efficiency and accuracy.

## ⚙️ Installation & Setup
### **Prerequisites**
- Python 3.x
- Required libraries:
  ```bash
  pip install pandas
  ```
  
## 🚀 Usage
### **Running the Comparison**
```bash
python main.py
```

### **Expected Output**
- `matched_computers.csv` → List of computers found in multiple systems.
- `missing_computers.csv` → List of computers that are missing from one or more systems.

## 📂 File Structure
```
/inactive-computer-scanner
│── /files                  # Directory for input CSV files  
│   ├── file1.csv           # Active Directory Export  
│   ├── file2.csv           # WSUS Report  
│── main.py                 # Main script to run the comparison  
│── requirements.txt        # Required Python packages  
│── README.md               # Project documentation  
```

## 📊 Example Output
| Name    | WSUS | Lansweeper | Wazuh |  
|---------|------|-----------|------|  
| PC-001  | ✔    | ✖         | ✔    |  
| PC-002  | ✖    | ✖         | ✔    |  
| PC-003  | ✔    | ✔         | ✔    |  

## 🔧 Contributions & Future Improvements
- Contributions are welcome! Open an issue or submit a PR.
- Planned features:
  - **GUI version** for easier use
  - **Automated email reports**
  - **Database integration** for better tracking

