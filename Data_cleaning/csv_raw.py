import pandas as pd
import os

# Input and output folder paths
input_folder = r'C:\#PROJECT\EEG\auditory-evoked-potential-eeg-biometric-dataset-1.0.0\Raw_Data'
# output_folder = 
output_folder = r'C:\#PROJECT\EEG\auditory-evoked-potential-eeg-biometric-dataset-1.0.0\Raw_Data_csv'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all .txt files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        txt_path = os.path.join(input_folder, filename)
        csv_filename = filename.replace('.txt', '.csv')
        csv_path = os.path.join(output_folder, csv_filename)
        
        # Adjust the delimiter as needed: ',' for comma, '\t' for tab, delim_whitespace=True for space
        df = pd.read_csv(txt_path, delimiter=',')  # Change delimiter if needed
        df.to_csv(csv_path, index=False)
        print(f"Converted {filename} to {csv_filename} in CSV_Output folder.")
