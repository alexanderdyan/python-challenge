#dependencies
import csv

#files ttto load and output
fileLoad = "raw_data/election_data.csv"
fileOutput = "analysis/election_analysis_1.txt"

#total vote counter
totalVotes = 0

#candidate options and vote counters
candidateOptions = []
candidateVotes = {}

#winning candidate and winning count tracker
winningCandidate = ""
winningCount = 0

#read in the csv and convert it into a list of dictionaries
with open(fileLoad) as election_data:
    reader = csv.DictReader(election_data)

    #for each row...
    for row in reader:

        #add to the total vote count:
        totalVotes = totalVotes + 1

        #extract the candidate name for each row
        candidateName = row["Candidate"]

        #if the candidate does not match any exisiting candidate...
        if candidateName not in candidateOptions:

            #add it to the list of candidates in the running
            candidateOptions.append(candidateName)

            #add begin tracking that candidate's voter count
            candidateVotes[candidateName] = 0

        #then add a vote to that candidate's count
        candidateVotes[candidateName] = candidateVotes[candidateName] + 1

#print the results and export the data to our text file
with open(fileOutput, "w") as txt_file:

    #print the final vote count
    electionResults = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalVotes}\n"
        f"-------------------------\n"
    )
    print(electionResults)

    #save the final vote count to the text file
    txt_file.write(electionResults)

    #determine the winner by looping through the counts
    for candidate in candidateVotes:

        #retrieve the vote count and percentage
        votes = candidateVotes.get(candidate)
        votesPercentage = float(votes) / float(totalVotes) * 100

        #determing winning vote count and candidate
        if (votes > winningCount):
            winningCount = votes
            winningCandidate = candidate
        
        #print each candidate's voter count and percentage
        voterOutput = f"{candidate}: {votesPercentage:.3f}% ({votes})\n"
        print(voterOutput)

        #save each candidate's voter count and percentage to text file
        txt_file.write(voterOutput)
    
    #print the winning candidate
    winningCandidateSummary = (
        f"-----------------------\n"
        f"Winner: {winningCandidate}\n"
        f"-----------------------\n"
    )
    print(winningCandidateSummary)

    #save the winning candidate's name to the text file
    txt_file.write(winningCandidateSummary)