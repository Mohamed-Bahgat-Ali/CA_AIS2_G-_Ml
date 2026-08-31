"""
Configuration file for the preprocessing pipeline.
Contains dataset-specific settings.
"""

# Columns to drop from the dataset
# These are Titanic-specific but can be modified for other datasets
COLS_TO_DROP = ["PassengerId", "Name", "Ticket", "Cabin"]

# Other configuration settings can be added here
# Example: TARGET_COLUMN = "Survived"
# Example: CATEGORICAL_FEATURES = ["Sex", "Embarked"]