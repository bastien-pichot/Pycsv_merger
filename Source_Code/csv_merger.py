import pandas as pd
import os
from pathlib import Path
import logging
from typing import List, Set

def validate_columns(template_file: Path, input_files: List[Path]) -> bool:
    try:
        # Read template columns
        template_cols = pd.read_csv(template_file, sep=';', nrows=0).columns
        template_cols_set = set(template_cols)
        
        # Check each input file
        for file in input_files:
            input_cols = pd.read_csv(file, sep=';', nrows=0).columns
            input_cols_set = set(input_cols)
            
            if template_cols_set != input_cols_set:
                logging.error(f"Column mismatch in {file.name}")
                logging.error(f"Missing columns: {template_cols_set - input_cols_set}")
                logging.error(f"Extra columns: {input_cols_set - template_cols_set}")
                return False
            
            # Check column order
            if not all(a == b for a, b in zip(template_cols, input_cols)):
                logging.error(f"Column order mismatch in {file.name}")
                return False
                
        return True
    except Exception as e:
        logging.error(f"Error during column validation: {str(e)}")
        return False

def merge_csv_files(
    input_folder: Path,
    template_folder: Path,
    output_folder: Path,
    batch_size: int = 100000
) -> None:

    try:
        # Ensure output folder exists
        output_folder.mkdir(parents=True, exist_ok=True)
        
        # Get list of input files
        input_files = list(input_folder.glob('*.csv'))
        if not input_files:
            logging.error("No CSV files found in input folder")
            return
            
        # Get template file
        template_file = next(template_folder.glob('*.csv'), None)
        if not template_file:
            logging.error("No template file found")
            return
            
        # Validate column structure
        if not validate_columns(template_file, input_files):
            logging.error("Column validation failed")
            return
            
        # Create output file
        output_file = output_folder / 'merged_output.csv'
        
        # Read template to get column names and types
        template_df = pd.read_csv(template_file, sep=';', nrows=0)
        
        # Create dictionary of data types (all columns as string to preserve leading zeros)
        dtype_dict = {col: str for col in template_df.columns}
        
        # Write header from template
        template_df.to_csv(output_file, sep=';', index=False, mode='w')
        
        # Process each input file in batches
        for file in input_files:
            logging.info(f"Processing file: {file.name}")
            
            # Calculate number of rows in file
            total_rows = sum(1 for _ in open(file, 'r')) - 1  # Subtract header row
            
            # Process file in batches
            for i in range(0, total_rows, batch_size):
                try:
                    # Read batch with string datatypes to preserve leading zeros
                    df_chunk = pd.read_csv(
                        file,
                        sep=';',
                        skiprows=range(1, i + 1) if i > 0 else None,
                        nrows=batch_size,
                        dtype=dtype_dict
                    )
                    
                    # Write to output file, preserving string format
                    df_chunk.to_csv(
                        output_file,
                        sep=';',
                        mode='a',
                        header=False,
                        index=False,
                        quoting=1  # QUOTE_ALL to preserve leading zeros
                    )
                    
                    logging.info(f"Processed rows {i} to {min(i + batch_size, total_rows)} of {file.name}")
                    
                except Exception as e:
                    logging.error(f"Error processing batch in {file.name}: {str(e)}")
                    raise
                    
        logging.info("Merge completed successfully")
        
    except Exception as e:
        logging.error(f"Error during merge process: {str(e)}")
        raise

if __name__ == "__main__":
    # Define paths
    current_dir = Path.cwd()
    input_folder = current_dir / 'Inputs'
    template_folder = current_dir / 'Template'
    output_folder = current_dir / 'Outputs'
    
    # Execute merge
    merge_csv_files(input_folder, template_folder, output_folder)