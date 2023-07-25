# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven",
           "eleven", "eighteen", "two", "fiftyonemkkmk"]


# TODO: The min() function finds the minimum value
print(f"this is smallest value in the list {min(values)}")
print(f"this is smallest value in the list: {min(strings)}")

# TODO: The max() function finds the maximum value
print(f"This is the largest value in the list: {max(values)}")
print(f"This is the largest value in the list: {max(strings)}")

# TODO: define a custom "key" function to extract a data field
print(f"This is the smallest value in the list: {min(strings, key=len)}")
print(f"This is the largest value in the list: {max(strings, key=len)}")

# TODO: open the data file and load the JSON
with open("/workspaces/advanced-python-working-with-data-4312001/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def find_values(dataitem):
    magnitude = dataitem['properties']['mag']
    if magnitude is None:
        magnitude = 0

    return float(magnitude)


print(data['metadata']['title'])
print(len(data['features']))

print(min(data['features'], key=find_values))
print("\n")
print(max(data['features'], key=find_values))
