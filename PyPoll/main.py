# import modules for OS and CSV

import os
import csv

#variables declaration

total_votes_casted = 0

candidates = []
unique_candidates = []
each_candidate_counts = []
percentage_votes = []

unique_candidate_count = 0
percentage_vote = 0
winner = ""

# Set the file path
csvpath = os.path.join('Resources','election_data.csv')

# open the csv file from the above path and read it to process further
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # iterate all the rows and create a list of all the votes - which represents candidates
    for row in csvreader:
        # this list holds candidates appearances
        candidates.append(row[2])
    
    # iterate above created list and create a new list with unique candidate names
    for candidate in candidates:
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
    
    # use the above two lists and create a new list for each 
    # candidate votes casted using list comprehension
    for unique_candidate in unique_candidates:
        unique_candidate_count = len([individual_candidate for individual_candidate 
                                      in candidates if individual_candidate == unique_candidate])
        each_candidate_counts.append(unique_candidate_count)
    
    # length of the list created for total votes represents the total votes casted
    total_votes_casted = len(candidates)

    # iterate each candidate counts list and find the percentage of votes 
    # casted for each candidate and create a new list for the percentage
    for each_candidate_count in each_candidate_counts:
        percentage_vote = round((each_candidate_count/total_votes_casted)*100,3)
        percentage_votes.append(percentage_vote)

    # use the max function and find the maximum percentage, 
    # use the index of that max percentage and find the candidate name from unique candidate list
    winner = unique_candidates[percentage_votes.index(max(percentage_votes))]
    

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes_casted}")
    print("-------------------------")
    
    # use the range and length function to iterate the list through the number of unique candidates
    # and print the unique candidate name, percentage of votes, vote counts for each iteration
    for i in range(len(unique_candidates)):
        print(f"{unique_candidates[i]}: {percentage_votes[i]}% ({each_candidate_counts[i]})")

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")


    # Export the analyis to the text file

    poll_analysis_file = os.path.join("analysis", "poll_analysis.txt")
    with open(poll_analysis_file, "w") as poll_file:
        poll_file.write("Election Results\n")
        poll_file.write("-------------------------\n")
        poll_file.write(f"Total Votes: {total_votes_casted}\n")
        poll_file.write("-------------------------\n")
        
        for i in range(len(unique_candidates)):
            poll_file.write(f"{unique_candidates[i]}: {percentage_votes[i]}% ({each_candidate_counts[i]})\n")

        poll_file.write("-------------------------\n")
        poll_file.write(f"Winner: {winner}\n")
        poll_file.write("-------------------------\n")  