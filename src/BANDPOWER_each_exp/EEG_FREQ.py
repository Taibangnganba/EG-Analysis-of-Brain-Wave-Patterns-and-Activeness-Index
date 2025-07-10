import os
import pandas as pd
import matplotlib.pyplot as plt

# Load your frequency features summary CSV
csv_path = 'eeg_frequency_features_all_subjects.csv'
df = pd.read_csv(csv_path)

# Define bands and channels
bands = ['delta', 'theta', 'alpha', 'beta', 'gamma']
channels = ['T7', 'F8', 'Cz', 'P4']

# Output directory for plots
output_root = 'bandpower_plots'
os.makedirs(output_root, exist_ok=True)

# Loop through each subject
for subject in df['subject'].unique():
    subject_df = df[df['subject'] == subject]
    subject_dir = os.path.join(output_root, str(subject))
    os.makedirs(subject_dir, exist_ok=True)
    
    # Loop through each file/session for this subject
    for idx, row in subject_df.iterrows():
        filename = row['filename']
        plt.figure(figsize=(8, 5))
        
        # Prepare bar heights: each channel's band powers
        bar_heights = []
        for ch in channels:
            band_powers = [row.get(f'{ch}_{band}', float('nan')) for band in bands]
            bar_heights.append(band_powers)
        
        # Plot grouped bar chart
        import numpy as np
        x = np.arange(len(bands))
        width = 0.18
        for i, ch in enumerate(channels):
            plt.bar(x + i*width, bar_heights[i], width, label=ch)
        
        plt.xticks(x + width*1.5, bands)
        plt.ylabel('Power')
        plt.xlabel('Frequency Band')
        plt.title(f'Subject: {subject} | File: {filename}')
        plt.legend()
        plt.tight_layout()
        
        # Save plot
        plot_name = f"{os.path.splitext(filename)[0]}_bandpower.png"
        plt.savefig(os.path.join(subject_dir, plot_name))
        plt.close()

print("All band power plots have been saved in the 'bandpower_plots' folder.")
