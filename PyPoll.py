#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:54:05 2018

@author: davidmartinez
"""

# csv module
import csv

# files
csvfile_input = "election_data.csv"
txtfile_output = os.path.join("election_analysis.txt")

# votes tracker
total_votes = 0

# candidate options and vote counters
candidate_options = []
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0

# read the csv and convert it into a list of dictionaries
with open(csvfile_input) as election_data:
    reader = csv.DictReader(election_data)

    # for each row...
    for row in reader:

        # run the loader animation
        print(". ", end=""),

        # add to the total vote count
        total_votes = total_votes + 1

        # extract the candidate name from each row
        candidate_name = row["Candidate"]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # begin tracking candidate's voter count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# print the results and export the data to our text file
with open(txtfile_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # save final vote count to the text file
    txt_file.write(election_results)

    # determine the winner by looping through the counts
    for candidate in candidate_votes:

        # retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)