import pandas as pd
import os

# Set your directory path
input_folder = r'C:\#PROJECT\EEG\auditory-evoked-potential-eeg-biometric-dataset-1.0.0\Raw_Data'

# Loop through all .txt files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        txt_path = os.path.join(input_folder, filename)
        csv_filename = filename.replace('.txt', '.csv')
        csv_path = os.path.join(input_folder, csv_filename)
        
        # Adjust the delimiter as needed. 
        # Common: ',' for comma, '\t' for tab, delim_whitespace=True for space
        df = pd.read_csv(txt_path, delimiter=',')  # Change delimiter if needed
        df.to_csv(csv_path, index=False)
        print(f"Converted {filename} to {csv_filename}")
