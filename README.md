# ODA
Olympic Data Analysis Dashboard
This Python script creates a web-based dashboard using Streamlit for analyzing Olympic data. The dashboard provides various features for exploring and visualizing Olympic data, including medal tallies, overall analysis, country-wise analysis, and athlete-wise analysis.
Prerequisites
Before running the script, make sure you have the following installed:

    Python 3.x
    Streamlit
    Pandas
    Plotly
    Matplotlib
    Seaborn

Installation

Clone the repository:

    git clone https://github.com/your-username/olympic-data-analysis.git

Install the required dependencies:

       pip install streamlit pandas plotly matplotlib seaborn

Usage

Navigate to the project directory:

       cd olympic-data-analysis

Run the Streamlit app:

       streamlit run olympic_analysis.py

Access the dashboard in your web browser at the provided URL.

Features

    Medal Tally: View medal tallies for specific years and countries.
    Overall Analysis: Explore overall statistics, participating nations over the years, events over the years, sports over the years, and athletes over the years.
    Country-wise Analysis: Analyze medal tallies and top athletes for specific countries.
    Athlete-wise Analysis: Explore the distribution of ages for gold medalists, height vs. weight for athletes, and more.

Data Sources
The script reads data from the following CSV files:

    athlete_events.csv: Contains information about Olympic athletes and events.
    noc_regions.csv: Provides mapping between National Olympic Committees (NOC) and their respective regions.
