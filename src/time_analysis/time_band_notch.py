import os
import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt, iirnotch

# Set your top-level data folder
data_root = r'C:\#PROJECT\EEG\auditory-evoked-potential-eeg-biometric-dataset-1.0.0\Raw_Data_csv'
fs = 256  # Set your sampling frequency

# Bandpass filter design: 1-40 Hz Butterworth
def bandpass_filter(signal, fs, low=1, high=40, order=2):
    b, a = butter(order, [low, high], btype='band', fs=fs)
    return filtfilt(b, a, signal)
# Notch filter: remove 50 Hz
def notch_filter(signal, fs, freq=50, Q=30):
    b, a = iirnotch(freq, Q, fs)
    return filtfilt(b, a, signal)

# Time domain feature extraction
def extract_time_features(signal):
    features = {}
    features['mean'] = np.mean(signal)
    features['std'] = np.std(signal)
    features['var'] = np.var(signal)
    features['skew'] = pd.Series(signal).skew()
    features['kurtosis'] = pd.Series(signal).kurtosis()
    features['ptp'] = np.ptp(signal)  # Peak-to-peak
    features['rms'] = np.sqrt(np.mean(signal**2))
    # Zero-crossing rate
    features['zcr'] = ((signal[:-1] * signal[1:]) < 0).sum() / len(signal)
    return features

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
                df.columns = df.columns.str.strip()
                features = {'subject': subject, 'filename': filename}
                for ch in ['T7', 'F8', 'Cz', 'P4']:
                    if ch in df.columns:
                        data = pd.to_numeric(df[ch], errors='coerce').dropna().to_numpy()
                        if len(data) > 0:
                            data = bandpass_filter(data, fs)
                            data = notch_filter(data, fs)
                            feats = extract_time_features(data)
                            for k, v in feats.items():
                                features[f'{ch}_{k}'] = v
                        else:
                            for k in ['mean','std','var','skew','kurtosis','ptp','rms','zcr']:
                                features[f'{ch}_{k}'] = np.nan
                    else:
                        for k in ['mean','std','var','skew','kurtosis','ptp','rms','zcr']:
                            features[f'{ch}_{k}'] = np.nan
                all_features.append(features)

# Save all features to a summary CSV
features_df = pd.DataFrame(all_features)
features_df.to_csv('eeg_time_features_all_subjects_with_filters.csv', index=False)
print("Time domain summary CSV saved successfully.")
