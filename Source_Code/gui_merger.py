import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import sys
import logging
from datetime import datetime
from csv_merger import merge_csv_files

class CSVMergerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Merger Tool")
        self.root.geometry("500x300")
        
        # Define fixed paths
        self.current_dir = Path.cwd()
        self.input_path = self.current_dir / 'Inputs'
        self.template_path = self.current_dir / 'Template'
        self.output_path = self.current_dir / 'Outputs'
        
        # Configure logging (console only)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler(sys.stdout)]
        )
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Path display labels
        ttk.Label(main_frame, text="Configured Folders:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=(0,10))
        
        ttk.Label(main_frame, text="Input Folder:").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(main_frame, text=str(self.input_path)).grid(row=1, column=1, sticky=tk.W)
        
        ttk.Label(main_frame, text="Template Folder:").grid(row=2, column=0, sticky=tk.W)
        ttk.Label(main_frame, text=str(self.template_path)).grid(row=2, column=1, sticky=tk.W)
        
        ttk.Label(main_frame, text="Output Folder:").grid(row=3, column=0, sticky=tk.W)
        ttk.Label(main_frame, text=str(self.output_path)).grid(row=3, column=1, sticky=tk.W)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, length=400, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(main_frame, textvariable=self.status_var)
        self.status_label.grid(row=5, column=0, columnspan=2)
        
        # Merge button
        self.merge_button = ttk.Button(main_frame, text="Start Merge", command=self.start_merge)
        self.merge_button.grid(row=6, column=0, columnspan=2, pady=20)
        
        # Create directories if they don't exist
        self.create_directories()
    
    def create_directories(self):
        try:
            self.input_path.mkdir(parents=True, exist_ok=True)
            self.template_path.mkdir(parents=True, exist_ok=True)
            self.output_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create directories: {str(e)}")
            self.root.quit()
    
    def start_merge(self):
        # Check if directories exist and are properly configured
        if not all([self.input_path.exists(), self.template_path.exists(), self.output_path.exists()]):
            messagebox.showerror("Error", "One or more required folders do not exist")
            return
        
        # Check if input files exist
        if not list(self.input_path.glob('*.csv')):
            messagebox.showerror("Error", "No CSV files found in input folder")
            return
        
        # Check if template file exists
        if not list(self.template_path.glob('*.csv')):
            messagebox.showerror("Error", "No template CSV file found")
            return
        
        # Disable button and start progress bar
        self.merge_button.state(['disabled'])
        self.progress.start()
        self.status_var.set("Merging files...")
        
        try:
            # Run merge operation with fixed batch size
            merge_csv_files(
                self.input_path,
                self.template_path,
                self.output_path,
                batch_size=100000
            )
            
            # Show success message
            self.status_var.set("Merge completed successfully!")
            messagebox.showinfo("Success", "CSV files have been merged successfully!")
            
        except Exception as e:
            # Show error message
            self.status_var.set("Error occurred during merge")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            logging.error(f"Error during merge: {str(e)}")
            
        finally:
            # Reset GUI state
            self.progress.stop()
            self.merge_button.state(['!disabled'])

def main():
    root = tk.Tk()
    app = CSVMergerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()