# Election Analysis


## Overview of Election Audit:

Tom's manager wants to analyse the election data which is in a CSV file type. We have to write a code which reads, analyse and generates a new text file giving us the summary of the analysis.


## Election-Audit Results:

After the detailed analysis we have recieved the following outcome.

1. The first thing we have found is that the total number of votes casted in this congressional election is 369,711.

2. The breakdown of the number of votes and the percentage of total votes for each county in the precinct is as follow:
	County Votes:
	  (County)   (Percentage) (Votes Casted)
	- Jefferson:   10.5%	    (38,855)
	- Denver:      82.8%  	   (306,055)
	- Arapahoe:     6.7%        (24,801)

3. The above data clearly states that the "Denver" county has the largest number of votes.

4. The breakdown of the number of votes and the percentage of the total votes each candidate received.
	  (Candidate's Name)		(Percentage) 	(Votes Casted)
	- Charles Casper Stockham:	  23.0%		   (85,213)
	- Diana DeGette: 		  73.8%		  (272,892)
	- Raymon Anthony Doane: 	   3.1%		   (11,606)

5. The winning canditate is "Diana DeGette". Their vote count is 272,892 and recieved 73.8% of the total votes.


## Election-Audit Summary:

This particular code/ program can be used to analyse data for not just this election, but for any election conducted for any conuty for any number of candidates.

Let me show you a few examples of how this code can be used for other elections too.

1. You have to simply update the data in the CSV file for the county you have elections in.
# Election Analysis


## Overview of Election Audit:

Tom's manager wants to analyse the election data which is in a CSV file type. We have to write a code which reads, analyse and generates a new text file giving us the summary of the analysis.


## Election-Audit Results:

After the detailed analysis we have recieved the following outcome.

1. The first thing we have found is that the total number of votes casted in this congressional election is 369,711.

2. The breakdown of the number of votes and the percentage of total votes for each county in the precinct is as follow:
	County Votes:
	  (County)   (Percentage) (Votes Casted)
	- Jefferson:   10.5%	    (38,855)
	- Denver:      82.8%  	   (306,055)
	- Arapahoe:     6.7%        (24,801)

3. The above data clearly states that the "Denver" county has the largest number of votes.

4. The breakdown of the number of votes and the percentage of the total votes each candidate received.
	  (Candidate's Name)		(Percentage) 	(Votes Casted)
	- Charles Casper Stockham:	  23.0%		   (85,213)
	- Diana DeGette: 		  73.8%		  (272,892)
	- Raymon Anthony Doane: 	   3.1%		   (11,606)

5. The winning canditate is "Diana DeGette". Their vote count is 272,892 and recieved 73.8% of the total votes.


## Election-Audit Summary:

This particular code/ program can be used to analyse data for not just this election, but for any election conducted for any conuty for any number of candidates.

Let me show you a few examples of how this code can be used for other elections too.

1. You have to simply update the data in the CSV file for the county you have elections in.
![image](https://user-images.githubusercontent.com/90114686/133911348-70042aa7-2208-4389-88c1-5b0b0cc4006a.png)
As you can see in the above picture, you have to note few things
The second column should be the "name of the county" and the third column should be the "name of the candidate". So if your data is not in that format make those changes to your data, so that the "name of the county" is on 2nd column and "name of the candidate" should be the third column.

2. You can also make a few minor changes in the code which will allow you to get an analytic report of any election.

![image](https://user-images.githubusercontent.com/90114686/133911355-a3df17f6-d0d9-4c54-818f-ba3436171004.png)

a) Check for the column which has the name of the candidate in the CSV file, 'lets say the its in column 5. Simply replace the code on line 47 with 'candidate_name = row[4]' (5-1)=4, since column index starts at 0.

b) Similarly, check for the column which has the name of the county in the CSV file, 'lets say the its in column 8. Simply replace the code on line 50 with county_name_row = row[7] (8-1)=7, again since the same logic apply on this one too, that is column index starts at 0.

By making any of the follwing changes you can get the desired result.
As you can see in the above picture, you have to note few things
The second column should be the "name of the county" and the third column should be the "name of the candidate". So if your data is not in that format make those changes to your data, so that the "name of the county" is on 2nd column and "name of the candidate" should be the third column.


2. You can also make a few minor changes in the code which will allow you to get an analytic report of any election.

a) Check for the column which has the name of the candidate in the CSV file, 'lets say the its in column 5. Simply replace the code on line 47 with 'candidate_name = row[4]' (5-1)=4, since column index starts at 0.

b) Similarly, check for the column which has the name of the county in the CSV file, 'lets say the its in column 8. Simply replace the code on line 50 with county_name_row = row[7] (8-1)=7, again since the same logic apply on this one too, that is column index starts at 0.

By making any of the follwing changes you can get the desired result.
