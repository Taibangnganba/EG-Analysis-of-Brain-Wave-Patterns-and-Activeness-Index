import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV
data_root = r"C:\#PROJECT\EEG\code\eeg_frequency_features_all_subjects.csv"
df = pd.read_csv(data_root)
#print(df.columns.tolist())
# Compute Activeness Index
df['Activeness_Index'] = (
    0.2 * df['T7_beta'] +
    0.3 * df['F8_beta'] +
    0.3 * df['Cz_beta'] +
    0.2 * df['P4_beta']
) / (
    0.2 * df['T7_theta'] +
    0.3 * df['F8_theta'] +
    0.3 * df['Cz_theta'] +
    0.2 * df['P4_theta']
)

# Pivot table: rows=Subject, columns=Experiment, values=mean Activeness_Index
subject_experiment_table = df.pivot_table(
    index='Subject', 
    columns='Experiment', 
    values='Activeness_Index', 
    aggfunc='mean'
)

#print(subject_experiment_table)



plt.figure(figsize=(20,10))
           
sns.heatmap(subject_experiment_table, annot=True, cmap='viridis')
plt.title('Activeness Index: Each Subject in Each Experiment', fontsize=14,
          bbox=dict(facecolor='wheat', alpha=0.5, boxstyle='round,pad=0.5'))


plt.xlabel('Experiment')
plt.ylabel('Subject')
plt.tight_layout()

plt.savefig(r"C:\#PROJECT\EEG\code\activeness_index.png", bbox_inches='tight', dpi=300)
plt.close()

plt.show()

print("Activeness Index computed and saved.")

#with filters
data_root_filters = r"C:\#PROJECT\EEG\code\eeg_frequency_features_all_subjects_with_filters.csv"
df = pd.read_csv(data_root_filters)
#print(df.columns.tolist())
# Compute Activeness Index
df['Activeness_Index'] = (
    0.2 * df['T7_beta'] +
    0.3 * df['F8_beta'] +
    0.3 * df['Cz_beta'] +
    0.2 * df['P4_beta']
) / (
    0.2 * df['T7_theta'] +
    0.3 * df['F8_theta'] +
    0.3 * df['Cz_theta'] +
    0.2 * df['P4_theta']
)

# Pivot table: rows=Subject, columns=Experiment, values=mean Activeness_Index
subject_experiment_table = df.pivot_table(
    index='Subject', 
    columns='Experiment', 
    values='Activeness_Index', 
    aggfunc='mean'
)

#print(subject_experiment_table)

plt.figure(figsize=(20,10))
           
sns.heatmap(subject_experiment_table, annot=True, cmap='viridis')
plt.title('Activeness Index: Each Subject in Each Experiment using Filters', fontsize=14,
          bbox=dict(facecolor='wheat', alpha=0.5, boxstyle='round,pad=0.5'))


plt.xlabel('Experiment')
plt.ylabel('Subject')
plt.tight_layout()

plt.savefig(r"C:\#PROJECT\EEG\code\activeness_index_with_filters.png", bbox_inches='tight', dpi=300)
plt.close()

plt.show()

print("Activeness Index with filterscomputed and saved.")

