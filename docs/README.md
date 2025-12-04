# MakeVotesMatter Engagement Analysis

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

## Installation & Setup

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

```
├─ data
│   ├─ processed
│   │  └─  # .feather generated for streamlit here
│   └─ raw  # donations.csv and main_report.csv required here
│      └─ action_data  # '<num>-actions' action data files required here
│
├─ requirements.txt
├─ scripts
│  └─ run_etl.py
├─ src
│  ├─ extract
│  │  ├─ extract.py
│  │  ├─ extract_actions.py
│  │  ├─ extract_donations.py
│  │  └─ extract_main.py
│  │  
│  ├─ load
│  │  ├─ app.py
│  │   load.py
│  │  
│  ├─ transform
│  │  ├─ clean_report.py
│  │  ├─ combine_donations.py
│  │  ├─ create_scores.py
│  │  ├─ normalise_column.py
│  │  ├─ tags.py
│  │  └─ transform.py
│  │  
│  ├─ utils
│     └─ logging_utils.py
└─ tests
   ├─ unit_tests
   │  ├─ extract_test.py
   │  └─ transformation_test.py


```

## Testing

Use pytest for testing

```bash
# Not exactly rocket science
pytest 
```

## Future Improvements

1. Widen scope on tags to determine demographic
2. Ability to select any tag for charts not pre-set tags (would remove need for bool cols) 
3. Api enabled script which could run over set period
4. Quick-load feature which loads streamlit app without ETL process (uses previous load)
5. Ensure reliability of ActionNetwork report
6. Increased and chained logic operations for tag selection on visualisations  

## License

This project was created for educational purposes as part of the Digital Futures Academy curriculum. Please consult with Digital Futures Academy for usage permissions.

# Important Notes

1. This project requires manual data export from ActionNetwork (because api takes like 4 hours)

2. Sensitive supporter data should be handled according to GDPR regulations

3. Accuracy of results are dependent on recency of data aquired and amount of data

4. Contact MVM administrators for access to required data sources










