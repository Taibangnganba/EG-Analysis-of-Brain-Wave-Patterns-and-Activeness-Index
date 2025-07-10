import os
import shutil
import re

input_folder = r'C:\#PROJECT\EEG\auditory-evoked-potential-eeg-biometric-dataset-1.0.0\Raw_Data_csv'

# Only process files that match the subject naming pattern, e.g., s01_ex01_s01.txt
pattern = re.compile(r'^(s\d{2})_.*\.(txt|csv)$', re.IGNORECASE)

for filename in os.listdir(input_folder):
    match = pattern.match(filename)
    if match:
        subject_id = match.group(1)
        subject_folder = os.path.join(input_folder, subject_id)
        os.makedirs(subject_folder, exist_ok=True)
        src = os.path.join(input_folder, filename)
        dst = os.path.join(subject_folder, filename)
        shutil.move(src, dst)
        print(f"Moved {filename} to folder {subject_id}")
    else:
        print(f"Skipped {filename} (does not match subject file pattern)")
