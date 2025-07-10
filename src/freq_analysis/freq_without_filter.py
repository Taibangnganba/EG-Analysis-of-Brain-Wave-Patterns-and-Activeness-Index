import os
import pandas as pd
import numpy as np
from scipy.signal import welch, butter, filtfilt

# Define frequency bands (Hz)
bands = {
    'delta': (0.5, 4),
    'theta': (4, 8),
    'alpha': (8, 13),
    'beta': (13, 30),
    'gamma': (30, 45)
}

# Set your top-level data folder
data_root = r'C:\#PROJECT\EEG\auditory-evoked-potential-eeg-biometric-dataset-1.0.0\Raw_Data_csv'
fs = 256  # Set your sampling frequency

# Bandpass filter design: 1-40 Hz Butterworth
def bandpass_filter(signal, fs, low=1, high=40, order=2):
    b, a = butter(order, [low, high], btype='band', fs=fs)
    return filtfilt(b, a, signal)

all_features = []

# Loop through all subject folders
for subject in os.listdir(data_root):
    subject_path = os.path.join(data_root, subject)
    if os.path.isdir(subject_path):
        for filename in os.listdir(subject_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(subject_path, filename)
                df = pd.read_csv(file_path)
                # Optional: rename columns if needed (strip spaces)
                rename_map = {
                    ' EXG Channel 0': 'T7',
                    ' EXG Channel 1': 'F8',
                    ' EXG Channel 2': 'Cz',
                    ' EXG Channel 3': 'P4'
                }
                df.rename(columns=rename_map, inplace=True)
                # Remove leading/trailing spaces from all column names
                df.columns = df.columns.str.strip()
                features = {'subject': subject, 'filename': filename}
                for ch in ['T7', 'F8', 'Cz', 'P4']:
                    if ch in df.columns:
                        # Ensure numeric and drop NaN
                        data = pd.to_numeric(df[ch], errors='coerce').dropna().to_numpy()  # [1][3][4][5]
                        if len(data) > 0:
                            nperseg = min(len(data), fs*2)
                            freqs, psd = welch(data, fs=fs, nperseg=nperseg)
                            for band, (low, high) in bands.items():
                                idx = np.logical_and(freqs >= low, freqs <= high)
                                features[f'{ch}_{band}'] = np.mean(psd[idx])
                        else:
                            # If data is empty, fill with NaN
                            for band in bands:
                                features[f'{ch}_{band}'] = np.nan
                    else:
                        # If channel missing, fill with NaN
                        for band in bands:
                            features[f'{ch}_{band}'] = np.nan
                all_features.append(features)

# Save all features to a summary CSV
features_df = pd.DataFrame(all_features)
features_df.to_csv('eeg_frequency_features_all_subjects.csv', index=False)
print("Summary CSV saved successfully.")
