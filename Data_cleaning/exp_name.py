import os
import re

# Mapping experiment numbers to experiment names
exp_map = {
    '01': '3MRSEO',
    '02': '3MRSEC',
    '05': '3MNLEH',
    '06': '3MNNLEH',
    '07': '3MNMEH',
    '08': '3MNLBH',
    '09': '3MNNLBH',
    '10': '3MNMBH'
}

main_folder = r'C:\#PROJECT\EEG\auditory-evoked-potential-eeg-biometric-dataset-1.0.0\Raw_Data_csv'

for subject_folder in os.listdir(main_folder):
    subject_path = os.path.join(main_folder, subject_folder)
    if os.path.isdir(subject_path):
        for filename in os.listdir(subject_path):
            if filename.endswith('.csv'):
                # Try to match with session number first
                match = re.match(r'(s\d+)_ex(\d+)_(s\d+)\.csv', filename)
                if match:
                    subject, experiment, session = match.groups()
                    exp_name = exp_map.get(experiment)
                    if exp_name:
                        new_filename = f"{subject}_{exp_name}_{session}.csv"
                    else:
                        continue  # Experiment not in mapping, skip
                else:
                    # Try to match without session number
                    match2 = re.match(r'(s\d+)_ex(\d+)\.csv', filename)
                    if match2:
                        subject, experiment = match2.groups()
                        exp_name = exp_map.get(experiment)
                        if exp_name:
                            new_filename = f"{subject}_{exp_name}.csv"
                        else:
                            continue  # Experiment not in mapping, skip
                    else:
                        continue  # Not matching any pattern, skip

                old_path = os.path.join(subject_path, filename)
                new_path = os.path.join(subject_path, new_filename)
                print(f"Renaming: {filename} -> {new_filename}")
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")
                except PermissionError:
                    print(f"SKIPPED (file in use): {old_path}")
