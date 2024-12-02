# Overview

This project demonstrates the power of Python scripting for automating and analyzing large datasets. It includes two real-world scenarios: financial analysis (PyBank) and election data processing (PyPoll). By leveraging Python, these analyses go beyond the capabilities of Excel, showcasing efficient handling of complex datasets.

# Challenges

# 1. PyBank: Financial Analysis 
__Objective:__

Analyze company financial records from budget_data.csv to calculate:

- Total number of months in the dataset.
- Net total amount of "Profit/Losses."
- Average changes in "Profit/Losses."
- Greatest increase in profits (date and amount).
- Greatest decrease in profits (date and amount).



__Example output:__

Financial Analysis
---------------

Total Months: 86

Total: $22564198

Average Change: $-8311.11

Greatest Increase in Profits: Aug-16 ($1862002)

Greatest Decrease in Profits: Feb-14 ($-1825558)

__Key Features:__

- Results printed to the terminal.
  
- Outputs exported to a text file.
   
# 2. PyPoll: Election Results Analysis
__Objective:__

Process election data from election_data.csv to determine:

- Total number of votes cast.
- List of candidates who received votes.
- Percentage of votes each candidate won.
- Total votes each candidate received.
- The winner of the election based on popular vote.
  
__Results:__

Example output:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------

# Key Features:

Results printed to the terminal.
Outputs exported to a text file.

# Files

PyBank_starter.py: Python script for the PyBank analysis.
PyPoll_starter.py: Python script for the PyPoll analysis.
Datasets: CSV files used in the analyses (budget_data.csv and election_data.csv).

# Requirements

__Data Handling:__
Read data from CSV files using Python's csv module.
Efficiently store and process large datasets.

__Output:__
Print results to the terminal for both challenges.
Export results to formatted text files.

__Error-Free Execution:__
Ensure scripts run without errors and produce consistent results.

__Clean and Documented Code:__
Include detailed comments for clarity.
Remove debugging artifacts.

# Technologies Used

Python: Core programming language for scripting.
CSV Module: To read and write CSV files.
File I/O: For exporting results to text files.

# How to Use

1. Clone this repository to your local machine.
2. Place the datasets (budget_data.csv and election_data.csv) in the same directory as the scripts.
3. Run the scripts:
For PyBank: python PyBank_starter.py
For PyPoll: python PyPoll_starter.py
4. Review the printed results in the terminal and the exported text files.

<!--Mod 3-->
