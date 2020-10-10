import os
import csv

election_data_csv = os.path.join('PyPoll','Resources', 'election_data.csv')

vote_count = 0
candidate_votes = {}
winner = ""
winning_vote = 0
votes = 0

with open(election_data_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader, None)

        for row in csvreader:

            vote_count += 1

            candidate = str(row[2])

            if candidate not in candidate_votes:
                candidate_votes[candidate] = 1
            else:
                candidate_votes[candidate] += 1

print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {int(vote_count)}")
print("---------------------------------------")

for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percentage = float(votes)/float(vote_count) * 100
    formatted_percentage = '{0:.3f}'.format(vote_percentage) 

    if votes > winning_vote:
        winning_vote = votes
        winner = candidate      

    outcome = (f"{str(candidate)}: {float(formatted_percentage)}% ({int(votes)})")
    print(outcome)

print("---------------------------------------")
print(f"Winner: {str(winner)}")
print("---------------------------------------")

output_file = os.path.join('PyPoll','Analysis','analysis.txt')

with open(output_file, "w") as datafile:
    datafile.write("Election Results\n")
    datafile.write("---------------------------------------\n")
    datafile.write(f"Total Votes: {int(vote_count)}\n")
    datafile.write("---------------------------------------\n")

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(vote_count) * 100
        #formatted_percentage = '{0:.3f}'.format(vote_percentage)

        if votes > winning_vote:
            winning_votes = votes
            winner = candidate         

        outcome = (f"{str(candidate)}: {'{:.3f}'.format(vote_percentage)} ({int(votes)})")
        datafile.write(outcome + "\n")

    #print(formatted_percentage)

    datafile.write("---------------------------------------\n")
    datafile.write(f"Winner: {str(winner)}\n")
    datafile.write("---------------------------------------\n")



