# MakeVotesMatter Engagement Analysis

## 📋 Description

Data engineering capstone project for Digital Futures Academy. This project analyzes engagement patterns for MakeVotesMatter (MVM) by processing donation data, supporter information, and ActionNetwork action data. The goal is to identify demographics and behaviors of both highly engaged and minimally engaged supporters to inform MVM's outreach strategy.

**Questions set by MVM:**

- What are the demographics of our most engaged supporters?
- What are the demographics of our least engaged supporters?
- What is the segment overlap between donors and action takers?

## Features

- **Data Merging**: Combines donation data, core supporter data, and counts of actions taken from multiple sources
- **Distribution Scoring**: Calculates engagement scores based on distribution metrics for actions and donations
- **Data Enrichment**: Cleans and enriches raw data for analysis
- **Complex tag sorting logic**: Allows for multi-level logic for tag analysis
- **Interactive Dashboard**: Streamlit app for dynamically exploring and visualising demographic data vs engagement

## Tech Stack

- **Python 3.12**
- **Pandas** - Data manipulation and analysis
- **Streamlit** - Interactive web application
- **Dependencies**: See `requirements.txt`

## ⚙️ Installation & Setup

### Prerequisites

1. **Python 3.12+** installed
2. **ActionNetwork Access**: You must have access to an admin level MVM ActionNetwork account
3. **Required Data Files**: Obtain the following from ActionNetwork:
   - Donations report (since Jan 1)
   - Supporters report of of "subscribed"
   - Individual actions taken reports

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alexcbeale-code/mvm-capstone.git
   ```
2. **Install Dependancies**:
   ```bash
   pip install -e .
   ```
3. **Development**:
   ```bash
   # run tests
   pytest 

   # execute project and open streamlit page 
   run_etl
   ```

run_etl opens your browser automatically,
otherwise visit http://localhost:8501/

## Repo Structure

put tree here

## Testing

Use pytest for testing

```bash
# Not exactly rocket science
pytest 
```

📈 Future Improvements

📄 License

This project was created for educational purposes as part of the Digital Futures Academy curriculum. Please consult with Digital Futures Academy for usage permissions.

Important Notes

 This project requires manual data export from ActionNetwork (because api takes 4 hours)

Sensitive supporter data should be handled according to GDPR regulations

Accuracy of results are dependent on recency of data aquired and amount of data

Contact MVM administrators for access to required data sources
