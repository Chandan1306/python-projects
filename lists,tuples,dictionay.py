  #  LIST TOPIC
print("LIST TOPIC\n".center(40))
Rcb = ["Virat","Rajath","Dev"] #Initializing
Rcb.insert(2,"Dinesh karthik")#insert
Rcb[3] = "Bhuvi"        #Alter or replace
Rcb.remove("Rajath")     #delete
print(Rcb)
Rcb.append("Rajath") #adding
Rcb.append("Dev")  #can only add once imme can append only one term per try
print(Rcb)
print(Rcb[-3])  #prints the specific values according to the postion
print(Rcb[:3])  #Prints the list till the position  from forward
print(Rcb[:-3]) #Prints the list till the position  from Backwards
print() #prints emplty line
print()


#  TUPLES TOPIC
print("TUPLE TOPIC\n".center(40))
Score = ("Virat",269, 180, 146)  #initalizing the domains
Player, Runs, Balls_faced, Strike_Rate = Score #initializing the address for the domains 
print(Runs)
print(Balls_faced)
print(Strike_Rate)
print(Player)

Rcb = {"Virat","Rajath","Dev"} #Initializing
Rcb.add("Dinesh karthik") #adding
print(Rcb)
Rcb.discard("Dev") #deleting
print(Rcb)
print() #prints emplty line
print()


#Dictionary Topic
# Print the heading centered within a 40-character width, followed by a newline
print("Dictionary TOPIC\n".center(40))

# Print an empty line for spacing
print()

# Create a dictionary named 'Scores' storing player statistics as key-value pairs
Scores = {
    "Name": "Virat Kohli",
    "Score": 269,
    "Balls_Faced": 186,
    "Strike_Rate": 144.62
}

# Access and print the value associated with the key 'Name' using square brackets
print(Scores["Name"])

# Access and print the value associated with the key 'Score' using the .get() method
print(Scores.get("Score"))

# Add a new key-value pair ('4s': 5) to the dictionary
Scores["4s"] = 5
# Print the updated dictionary
print(Scores)

# Update the existing value of the 'Name' key from 'Virat Kohli' to 'VK'
Scores["Name"] = "VK"
# Print the dictionary after the update
print(Scores)

# Remove the key '4s' and its value from the dictionary using .pop()
Scores.pop("4s")
# Print the dictionary after removing the key
print(Scores)

# Print an empty line for spacing
print()

# Loop through all key-value pairs in the dictionary and print them formatted with a colon
for key, value in Scores.items():
    print(key, ":", value)

# Print an empty line for spacing
print()

# Print a view object containing all the keys in the dictionary
print(Scores.keys())

# Print a view object containing all the values in the dictionary
print(Scores.values())
