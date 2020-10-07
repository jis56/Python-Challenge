import os
import csv

election_data_csv = os.path.join('PyPoll','Resources', 'election_data.csv')

row_count = 0
candidates = {}
candidate_options = []

with open(election_data_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader, None)

        for row in csvreader:

            row_count += 1

            candidate = str(row[2])

            if candidate not in candidate_options:
                candidate_options.append(candidate)

            if candidate not in candidates:
                candidates[candidate] = 1
            else:
                candidates[candidate] += 1

print(candidate_options)


