"""
Main Pipeline for Titanic Data Preprocessing.

This script orchestrates the entire preprocessing pipeline:
1. Read the dataset with error handling
2. Drop unnecessary features based on configuration
3. Generate a data quality report

The pipeline is designed to be modular and reusable.
"""

import sys
from pathlib import Path

# Import the preprocessing functions
from preprocessing import read_data_file, drop_unnecessary_features, check_data_type
from config import COLS_TO_DROP


def main():
    """
    Execute the complete preprocessing pipeline.
    
    The pipeline:
    1. Reads the Titanic dataset from the specified path
    2. Drops unnecessary columns based on config
    3. Generates and displays a data quality report
    """
    print("=" * 70)
    print("TITANIC DATA PREPROCESSING PIPELINE")
    print("=" * 70)
    
    # Step 1: Read the dataset
    print("\n[1] Loading Dataset...")
    print("-" * 40)
    
    # FIXED: Using raw string (r prefix) for Windows path
    file_path = "Titanic.csv"
    
    # Alternative options (uncomment one):
    # Option 1: Using forward slashes
    # file_path = "C:/Users/mb169/Desktop/Cairo depi/cA_AIS2 G-_ML/Assignments/Preprocessing Assignment /Titanic.csv"
    
    # Option 2: Using double backslashes
    # file_path = "C:\\Users\\mb169\\Desktop\\Cairo depi\\cA_AIS2 G-_ML\\Assignments\\Preprocessing Assignment \\Titanic.csv"
    
    # Option 3: Using pathlib (most robust)
    # file_path = Path("C:/Users/mb169/Desktop/Cairo depi/cA_AIS2 G-_ML/Assignments/Preprocessing Assignment /Titanic.csv")
    
    # Debug: Print the file path to verify
    print(f"Looking for file at: {file_path}")
    
    df = read_data_file(file_path)
    
    if df is None:
        print("Exiting: Dataset could not be loaded.")
        return
    
    print(f"\nInitial dataset loaded successfully.")
    print(f"Columns: {list(df.columns)}")
    
    # Step 2: Drop unnecessary features
    print("\n[2] Dropping Unnecessary Features...")
    print("-" * 40)
    print(f"Columns to drop (from config): {COLS_TO_DROP}")
    
    df_cleaned = drop_unnecessary_features(df, COLS_TO_DROP)
    
    # Step 3: Generate data quality report
    print("\n[3] Generating Data Quality Report...")
    print("-" * 40)
    
    report = check_data_type(df_cleaned)
    
    # Step 4: Save report (optional)
    print("\n[4] Saving Report...")
    print("-" * 40)
    
    # Save the report to a CSV file
    report_filename = "data_quality_report.csv"
    try:
        report.to_csv(report_filename)
        print(f"Report saved to '{report_filename}'")
    except Exception as e:
        print(f"Warning: Could not save report: {str(e)}")
    
    print("\n" + "=" * 70)
    print("PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    
    # Return the cleaned DataFrame for potential further use
    return df_cleaned


if __name__ == "__main__":
    # Execute the main pipeline
    cleaned_df = main()
    
    # You can now work with cleaned_df for further analysis
    # Example: print(cleaned_df.head())