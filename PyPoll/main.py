# Import the modules
import os
import csv

# Set the path to where the csv file is located
election_data_csv = os.path.join("Resources", "election_data.csv")

# Set the path for where the text file will be written to
text_path =os.path.join("python-challenge", "PyPoll", "Analysis", "Analysis.txt")

# Set variables
total_votes = 0
candidates = []
candidate_votes = {}
vote_percentange = 0
winner = ""
winning_count = 0

# Open as a csv file
with open(election_data_csv) as csvfile:
    
    # Using csvreader to specify the variable and delimiter
    csvreader=csv.reader(csvfile, delimiter=',')
    
    # Read header row first and store
    csv_header=next(csvreader)
    print(f"csv Header: {csv_header}")
    
    # Read each row of data after skipping header
    for row in csvreader:
        
        # Calculate total votes
        total_votes += 1

        # Get the candidates from each row
        c = row[2]
    
        # Check if the candidate matches with one already mentioned and if not add it to a blank list
        if c not in candidates:
            candidates.append(c)
            
            # Start tracking the total number of votes for each candidate
            candidate_votes[c] = 0

        # Add a vote to each candidates total
        candidate_votes[c] += 1

# Open the file path where the text file will be saved
with open(text_path, 'w') as txtfile:

    # Print the title and the total overall votes to the terminal
    print("Election Results")

    print("----------------------------------------")

    print(f"Total Votes: {total_votes}")

    print("----------------------------------------")

    # Write the title and total votes to the text file
    txtfile.write("Election Results\n")
    txtfile.write("----------------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("----------------------------------------\n")

    # Use a for loop to get the total number and the percentage of votes for each candidate by associating the list of candidates with the candidates votes
    for c in candidate_votes:
        
        # Determine total number of votes each candidate earned
        vote_count = candidate_votes[c]
        
        # Calculate what percentage of the vote each candidate earned
        vote_percentange = float(vote_count) / float(total_votes) * 100

        # Print a list of candidates, the percentage earned and the total number of votes earned to the terminal
        print(f"{c}: {vote_percentange:.3f}% ({vote_count})")

        # write a list of candidates, the percentage earned and the total number of votes earned to the text file
        txtfile.write(f"{c}: {vote_percentange:.3f}% ({vote_count})\n")

        # Determine the winner using the total votes each candidate earned
        if (vote_count > winning_count):

            winning_count = vote_count

            winner = (c)
    
    # Print the winner to the terminal
    print("----------------------------------------")

    print(f"Winner: {winner}")

    print("----------------------------------------")

    # Write the winner to the text file
    txtfile.write("----------------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("----------------------------------------\n")Code will follow here
