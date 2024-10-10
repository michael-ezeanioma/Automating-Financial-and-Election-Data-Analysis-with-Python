# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast (A counter)

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {} #Stores vote count for each candidate

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1 #increments total vote variable by one based on how many rows there is

        # Get the candidate's name from the row
        candidate = row[2] 
        if candidate in candidate_votes: #If the candidate is already in the dictionary, increment the count
            candidate_votes[candidate] += 1
        # If the candidate is not already in the candidate list, add them
        else:
            candidate_votes[candidate] = 1


# Open a text file to save the output
#with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
print("Election Results\n")
print(f"-------------------------\n\nTotal votes: {total_votes}"
      "\n\n-------------------------\n")

for candidate, votes in candidate_votes.items(): 
    percentage = (votes / total_votes) * 100 #calculating candidate percentage of votes
    print(f"{candidate}: {percentage:.2f}% ({votes})")
    
        #Add a vote to the candidate's count
max_votes_candidate = max(candidate_votes, key = candidate_votes.get) #max vot getter line
max_votes = candidate_votes[max_votes_candidate]

print(f"\n-------------------------\n\nWinner: {max_votes_candidate}"
      "\n\n-------------------------")


    # Write the total vote count to the text file


    # Save the winning candidate summary to the text file
