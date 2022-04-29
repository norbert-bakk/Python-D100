#Python list --> data structure

from os import stat


states_of_US = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# realted data, order is also important
print(states_of_US[5])
# -1 --> negative index --> starts counting from the end of the list --> -0 doesnt exists
# we can change also stuff in the list
states_of_US[5] = "MassaCSusetts"
print(states_of_US[5])

# .append will add a single item to the list
states_of_US.append("Québéc")
print(states_of_US[50])

# 5. Data structures pythoc documentation
# .extend([]) --> adding couple of more items
states_of_US.extend(["Ontario", "Saskatchewan", "Manitoba"])
