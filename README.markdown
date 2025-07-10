# EEG Analysis of Brain Wave Patterns and Activeness Index

## Project Overview
This repository contains a Python-based pipeline for analyzing open-access EEG data from [PhysioNet](https://doi.org/10.13026/ps31-fc50). The project focuses on cleaning EEG data using Butterworth and notch filters, analyzing Root Mean Square (RMS) in the time domain and Power Spectral Density (PSD) in the frequency domain for alpha, beta, theta, and delta waves, and computing an activeness index to quantify subject engagement across various experimental conditions. PSD is estimated using the Welch method. The pipeline is designed to be reproducible and adaptable for other EEG datasets.

## Features
- **Data Preprocessing**: Artifact removal, Butterworth and notch filtering, and signal normalization.
- **Time-Domain Analysis**: Computation of RMS to assess signal amplitude across experiments, enhanced by filtering.
- **Frequency-Domain Analysis**: PSD estimation using the Welch method for key brain wave bands across experiments.
- **Activeness Index**: A custom metric to assess subject engagement based on RMS and PSD features.
- **Visualization**: Plots for RMS trends, PSD spectra, and activeness index across experiments.

## Requirements
- Python 3.8+
- Libraries: `numpy`, `scipy`, `mne`, `matplotlib`, `seaborn`, `pandas`, `scikit-learn`
- PhysioNet EEG dataset [Auditory evoked potential EEG-Biometric dataset](https://doi.org/10.13026/ps31-fc50)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/[your-repo-name].git
   ```
2. Download the PhysioNet dataset and place it in the `Data_cleaning/` directory.

## Usage
1. Compute and visualize the activeness index in frequency domain:
   ```bash
   python freq_ac_index.py --input eeg_frequency_features_all_subjects_with_filters.csv
   ```
2. Compute and visualize the activeness index in time domain:
   ```bash
   python time_ac_index.py --input eeg_time_features_all_subjects_with_filters.csv
   ```

## Directory Structure
- `Data_cleaning/`: Raw and processed EEG data
- `src/`: Python scripts for preprocessing, RMS and PSD analysis, and visualization
- `Results/`: Output plots for RMS, PSD, and activeness index
- `freq_analysis/`: Python scripts for frequency domain analysis
- `time_analysis/`: Python scripts for time domain analysis
- `Naming/`: shows overview of naming in the graph
- `README.md`: This file
- `LICENSE`: License information

## Results
The analysis reveals distinct RMS and PSD patterns across experimental conditions. Butterworth and notch filters significantly improve time-domain RMS clarity with minimal impact on frequency-domain PSD, likely due to the Welch method's robustness. Visualizations are saved in the `Results/` directory.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for bug fixes or enhancements.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments

This project was inspired by the PhysioNet EEG dataset and the research paper "Auditory evoked potential EEG-Biometric dataset".
- Abo Alzahab, N., Di Iorio, A., Apollonio, L., Alshalak, M., Gravina, A., Antognoli, L., Baldi, M., Scalise, L., & Alchalabi, B. (2021). Auditory evoked potential     EEG-Biometric dataset (version 1.0.0). PhysioNet. RRID:SCR_007345. https://doi.org/10.13026/ps31-fc50
- Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P.C., Mark, R., Mietus, J.E., Moody, G.B., Peng, C.K. and Stanley, H.E., 2000. PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220. RRID:SCR_007345.

## Contact
For any questions or feedback, please contact [Kambam Taibangnganba](https://github.com/Taibangnganba)