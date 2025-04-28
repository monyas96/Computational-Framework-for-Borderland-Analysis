# Borderland Dynamics Knowledge Hub

An interactive web application that integrates computational research, mapping tools, and policy reflections to examine borderland dynamics, focusing on the Kenya-Uganda border region.
Acess the streamlit App here: https://monyas96-computational-framework-for-borderland-anal-app-od9dth.streamlit.app/
## Features

- Interactive visualization of Market Potential Index (MPI) and Conflict Exposure Index (CI)
- Comprehensive background and context information
- Policy insights and engagement tools
- ESRI StoryMap integration
- Resources and downloads section

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/borderland-dynamics-hub.git
cd borderland-dynamics-hub
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

The application is organized into several sections:

- Home / Overview: Introduction to the project
- Background and Context: Theoretical framework
- The Model: Detailed explanation of MPI, CI, and Relational Layers
- Data and Implementation: Technical details
- Interactive Visualization: Dynamic maps and controls
- Key Findings: Case study results
- ESRI StoryMap: Interactive story map
- Policy Insights: Policy recommendations
- Resources: Downloadable materials
- Summary: Next steps and future work

# Computational-Framework-for-Borderland-Analysis

## Reproducing and Running the Streamlit App

### 1. Clone the Repository

```bash
git clone https://github.com/monyas96/Computational-Framework-for-Borderland-Analysis.git
cd Computational-Framework-for-Borderland-Analysis
```

### 2. Set Up the Environment

#### Recommended: Using Conda/Miniforge (especially for Apple Silicon/M1/M2/M3 Macs)

```bash
conda create -n borderland python=3.10
conda activate borderland
conda install pandas geopandas matplotlib seaborn altair streamlit pydeck networkx
pip install plotly
```

#### Or, using pip (for Intel/Windows/Linux)

```bash
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
```

### 3. Prepare the Data

- Place the required CSV files (`mpi_border_results.csv`, `ci_results.csv`, etc.) in the project root or as specified in the app.
- If you need to generate these files, run the analysis scripts provided in the repo.

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

- The app will open in your browser at `http://localhost:8501`.

### 5. Using the App

- Use the sidebar to navigate between pages.
- Explore interactive visualizations, download data, and read key insights.

---

## Project Structure

- `app.py` — Main Streamlit app
- `requirements.txt` — Python dependencies
- `*.csv` — Data files for the app
- `10.1.2025_analysis.py` — Data processing/analysis script

---

## License

MIT License © Moneera Yassien

---

## Acknowledgements

See the full documentation and code at [https://github.com/monyas96/Computational-Framework-for-Borderland-Analysis](https://github.com/monyas96/Computational-Framework-for-Borderland-Analysis)
