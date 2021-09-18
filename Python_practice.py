# print("Hello World")
# counties = ["Arapahoe","Denver","Jefferson"]
# counties.append("El Paso")
# counties.remove("Arapahoe")
# counties[2]=("Denver")
# counties[0]=("El Paso")
# counties.append("Arapahoe")
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# for county in voting_data:
#     print(f'{county["county"]} county has {county["registered_voters"]} registered voters.')
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# for county_dict in voting_data:
#     print(county_dict['registered_voters'])
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     # print(county + " county has " + str(voters) + " registered voters.")
#     print(f"{county} county has {voters} registered voters.")
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# print(message_to_candidate)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
     print(f"{county} county has {voters:,} registered voters.")

