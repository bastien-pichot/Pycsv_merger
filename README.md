# Pycsv_merger
User Guide - CSV Merger Tool
Overview
This tool allows you to merge multiple CSV files into a single file, following a column structure defined by a template file.
Important Prerequisites

All files must be in CSV format with semicolon (;) delimiter
Input files must have exactly the same structure (same columns) as the template file
File names are not important

Folder Structure
The tool uses three folders that are created automatically:

Inputs: Folder containing the files to be merged
Template: Folder containing the template file
Outputs: Folder where the result will be saved

Usage Steps
1. Template Preparation

Place your template file in the Template folder
This file defines the expected column structure
Important: Verify that your template contains the correct columns in the correct order

2. Preparing Files to Merge

Place all files to be merged in the Inputs folder
Important: Verify that all your files:

Are in CSV format with semicolon (;) delimiter
Have exactly the same columns as the template
File names don't matter



3. Merging Files

Double-click on the CSV_Merger.exe executable
Click the "Start Merge" button
Wait for the process to complete
A confirmation message will appear once the merge is finished

4. Retrieving the Result

The merged file will be available in the Outputs folder
The output file will be in CSV format with semicolon (;) delimiter

Common Issues Troubleshooting
Error Message "No CSV files found in input folder"
➢ Verify that:

Your files are in the Inputs folder
Your files have the .csv extension

Error Message "No template CSV file found"
➢ Verify that:

Your template file is in the Template folder
The file has the .csv extension

Error Message "Column validation failed"
➢ Verify that:

All your input files have exactly the same columns as the template
The columns are in the same order
Column names are exactly identical (pay attention to spaces and case)

Important Notes

File names have no importance for the tool's operation
Only the column structure must be identical between files
The tool processes files in batches to handle large volumes of data
It is recommended to backup your files before merging
Leading zeros in columns are preserved (e.g., "001" will not become "1")

Support
If you encounter issues:

Verify that all prerequisites are met
Ensure all files are in the correct format (CSV with semicolon delimiter)
Check the column structure of your files
