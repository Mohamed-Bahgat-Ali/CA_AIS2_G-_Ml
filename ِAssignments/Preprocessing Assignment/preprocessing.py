"""
Preprocessing Module for Data Loading and Quality Assessment.

This module provides reusable functions for:
- Loading CSV files with error handling
- Dropping features dynamically
- Generating data quality reports

Author: [Your Name]
Date: [Current Date]
"""

import pandas as pd
import os
from typing import List, Optional


def read_data_file(file_path: str) -> Optional[pd.DataFrame]:
    """
    Read a CSV file and return a pandas DataFrame with robust error handling.

    This function handles common file reading errors gracefully by providing
    clear, user-friendly error messages instead of letting the program crash
    with cryptic pandas errors.

    Parameters
    ----------
    file_path : str
        The path to the CSV file to be read.

    Returns
    -------
    Optional[pd.DataFrame]
        A pandas DataFrame containing the data from the CSV file,
        or None if an error occurs.

    Raises
    ------
    No exceptions are raised; all errors are caught and printed.

    Examples
    --------
    >>> df = read_data_file("data/titanic.csv")
    >>> print(df.shape)
    (891, 12)
    
    >>> df = read_data_file("non_existent.csv")
    Error: The file 'non_existent.csv' does not exist.
    """
    try:
        # Check if file path is valid
        if not file_path:
            print("Error: Empty file path provided.")
            return None
            
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            return None
            
        # Check if file is readable (has .csv extension)
        if not file_path.lower().endswith('.csv'):
            print(f"Warning: The file '{file_path}' may not be a CSV file.")
            
        # Attempt to read the CSV file
        df = pd.read_csv(file_path)
        
        # Check if DataFrame is empty
        if df.empty:
            print("Warning: The file was read successfully but contains no data.")
            
        print(f"Success: File '{file_path}' loaded successfully.")
        print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
        
        return df
        
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
        
    except pd.errors.ParserError:
        print(f"Error: The file '{file_path}' contains parsing errors. "
              "Please check the file format.")
        return None
        
    except PermissionError:
        print(f"Error: Permission denied. Cannot read '{file_path}'.")
        return None
        
    except UnicodeDecodeError:
        print(f"Error: Encoding issue. The file '{file_path}' may use "
              "a different character encoding.")
        return None
        
    except Exception as e:
        print(f"Unexpected error while reading '{file_path}': {str(e)}")
        return None


def drop_unnecessary_features(df: pd.DataFrame, 
                             cols_to_drop: List[str]) -> pd.DataFrame:
    """
    Drop specified columns from a DataFrame.

    This function removes columns provided through the cols_to_drop parameter.
    It is designed to work with any dataset and does not contain any
    dataset-specific logic.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame from which columns will be removed.
    cols_to_drop : List[str]
        A list of column names to be dropped from the DataFrame.

    Returns
    -------
    pd.DataFrame
        A new DataFrame with the specified columns removed.

    Notes
    -----
    - The function creates a copy of the original DataFrame to avoid
      modifying the original data.
    - Only columns that exist in the DataFrame will be dropped.
    - If no valid columns are specified, the original DataFrame is returned
      with a warning.

    Examples
    --------
    >>> df = pd.DataFrame({'A': [1,2], 'B': [3,4], 'C': [5,6]})
    >>> drop_unnecessary_features(df, ['A', 'B'])
       C
    0  5
    1  6
    
    >>> drop_unnecessary_features(df, ['NonExistent'])
    Warning: No valid columns to drop.
       A  B  C
    0  1  3  5
    1  2  4  6
    """
    # Create a copy to avoid modifying the original DataFrame
    df_copy = df.copy()
    
    # Validate input
    if not isinstance(cols_to_drop, list):
        raise TypeError("cols_to_drop must be a list of column names.")
    
    # Filter only columns that exist in the DataFrame
    existing_cols = [col for col in cols_to_drop if col in df_copy.columns]
    missing_cols = [col for col in cols_to_drop if col not in df_copy.columns]
    
    # Report missing columns
    if missing_cols:
        print(f"Warning: The following columns were not found: {missing_cols}")
    
    # Drop the columns if any exist
    if existing_cols:
        df_copy = df_copy.drop(columns=existing_cols)
        print(f"Dropped columns: {existing_cols}")
        print(f"Remaining columns: {list(df_copy.columns)}")
    else:
        print("Warning: No valid columns to drop.")
    
    return df_copy


def check_data_type(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a comprehensive data quality report for each column.

    This function creates a detailed summary of the DataFrame's structure,
    including column names, data types, and the number of unique values.
    The report helps identify categorical features, numerical features,
    and columns with many unique values.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame to be analyzed.

    Returns
    -------
    pd.DataFrame
        A transposed DataFrame with the following columns:
        - Column Name: The name of each column
        - Data Type: The pandas data type of the column
        - Unique Count: The number of unique values in the column
        - Null Count: The number of missing values (for completeness)
        - Sample Values: A sample of values from the column

    Notes
    -----
    The returned DataFrame is transposed for easier readability,
    especially when dealing with many columns.

    Examples
    --------
    >>> df = pd.DataFrame({
    ...     'Age': [25, 30, 25, 35],
    ...     'Sex': ['M', 'F', 'M', 'F'],
    ...     'Fare': [100, 200, 150, 300]
    ... })
    >>> check_data_type(df)
                 Age    Sex    Fare
    Datatype    int64  object  int64
    Unique      3      2       4
    Null        0      0       0
    Sample      [25, 30, 35] [M, F] [100, 200, 150, 300]
    """
    # Validate input
    if df is None or df.empty:
        print("Error: DataFrame is None or empty.")
        return pd.DataFrame()
    
    # Create the report dictionary
    report = {
        'Datatype': df.dtypes,
        'Unique Count': df.nunique(),
        'Null Count': df.isnull().sum(),
        'Null Percentage': (df.isnull().sum() / len(df) * 100).round(2),
        'Sample Values': df.apply(lambda x: x.dropna().unique()[:3].tolist() if not x.dropna().empty else ['No values'])
    }
    
    # Convert to DataFrame and transpose
    report_df = pd.DataFrame(report).T
    
    # Add column name as index label
    report_df.index.name = 'Column Name'
    
    # Print summary statistics
    print("=" * 60)
    print("DATA QUALITY REPORT")
    print("=" * 60)
    print(f"Total rows: {len(df)}")
    print(f"Total columns: {len(df.columns)}")
    print("\nColumn Summary:")
    print("-" * 60)
    print(report_df)
    print("=" * 60)
    
    # Additional insights
    print("\nInsights:")
    print(f"- {len(df.select_dtypes(include=['object']).columns)} categorical columns")
    print(f"- {len(df.select_dtypes(include=['int64', 'float64']).columns)} numerical columns")
    
    # Identify potential categorical columns (low unique values)
    categorical_candidates = df.nunique()[df.nunique() < 10].index.tolist()
    if categorical_candidates:
        print(f"- Potential categorical features: {categorical_candidates}")
    
    # Identify high cardinality columns
    high_cardinality = df.nunique()[df.nunique() > len(df) * 0.5].index.tolist()
    if high_cardinality:
        print(f"- High cardinality columns (potential IDs): {high_cardinality}")
    
    return report_df