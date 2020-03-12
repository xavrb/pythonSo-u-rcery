def maxVotes(votes):
	processedInfo = {
		}
	nmax = 0 
	processedVotes = []
	winners ={}
	for x in votes:
		if len(processedVotes)>0:
			nmax = max(processedVotes)

		if x not in processedInfo:
			if votes.count(x)>=nmax:
				processedInfo[x]= votes.count(x)
				#winners.append(x)
				processedVotes.append(votes.count(x))
			else:
				pass

		else:
			pass 

	for x in processedInfo:
		if processedInfo[x]==nmax:
			winners[x] = processedInfo[x] 
	return sorted(winners)[0]







votes = ["john", "johnny", "johnny", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"]
print(maxVotes(votes))
