import pandas as pd
import matplotlib.pyplot as plt

# --- WITH FILTERS ---
df_time_filt = pd.read_csv(r"C:\#PROJECT\EEG\code\eeg_time_features_all_subjects_with_filters.csv")

df_time_filt['Time_Activeness_Index'] = (
    df_time_filt['T7_rms'] +
    df_time_filt['F8_rms'] +
    df_time_filt['Cz_rms'] +
    df_time_filt['P4_rms']
)

grouped_filt = df_time_filt.groupby(['Subject', 'Experiment'])['Time_Activeness_Index'].mean().reset_index()
pivot_filt = grouped_filt.pivot(index='Subject', columns='Experiment', values='Time_Activeness_Index')

plt.figure(figsize=(14, 7))
for exp in pivot_filt.columns:
    plt.plot(pivot_filt.index, pivot_filt[exp], marker='o', label=exp)
plt.title('Time Domain Activeness Index (With Filters)')
plt.xlabel('Subject')
plt.ylabel('Time Activeness Index (RMS)')
plt.legend(title='Experiment')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(r"C:\#PROJECT\EEG\code\time_activeness_index_line_with_filters.png", dpi=300)
plt.show()

# --- WITHOUT FILTERS ---
df_time = pd.read_csv(r"C:\#PROJECT\EEG\code\eeg_time_features_all_subjects.csv")

df_time['Time_Activeness_Index'] = (
    df_time['T7_rms'] +
    df_time['F8_rms'] +
    df_time['Cz_rms'] +
    df_time['P4_rms']
)

grouped = df_time.groupby(['Subject', 'Experiment'])['Time_Activeness_Index'].mean().reset_index()
pivot = grouped.pivot(index='Subject', columns='Experiment', values='Time_Activeness_Index')

plt.figure(figsize=(14, 7))
for exp in pivot.columns:
    plt.plot(pivot.index, pivot[exp], marker='o', label=exp)
plt.title('Time Domain Activeness Index (No Filters)')
plt.xlabel('Subject')
plt.ylabel('Time Activeness Index (RMS)')
plt.legend(title='Experiment')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(r"C:\#PROJECT\EEG\code\time_activeness_index_line_no_filters.png", dpi=300)
plt.show()
