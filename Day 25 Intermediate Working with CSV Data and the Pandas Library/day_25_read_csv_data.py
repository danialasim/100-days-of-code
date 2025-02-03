with open("day_25_weather-data.csv") as data_file:
    data = data_file.readlines()
    print(data)

import csv

from sympy.physics.units import temperature

with open("day_25_weather-data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas  # Import the pandas library for reading, manipulating, and analyzing structured data.

# Read data from the CSV file into a pandas DataFrame.
# This will allow you to perform data manipulation and analysis easily.
data = pandas.read_csv("day_25_weather-data.csv")
print(type(data))  # Print the type of the object to confirm it is a DataFrame.
print(type(data))  # Another type check (possibly redundant).

# Convert the DataFrame to a dictionary.
# This can be useful if you need to process the data in a format compatible with native Python structures.
data_dict = data.to_dict()
print(data_dict)  # Print the dictionary representation of the data for inspection.

# Extract the 'temp' column as a list of integers.
# This is useful if you want to perform manual computations on the temperature data.
temp_list = data["temp"].to_list()
print(temp_list)  # Print the list of temperatures for verification.

# Calculate the average temperature manually using basic Python operations.
average = sum(temp_list) / len(temp_list)
print(average)  # Print the calculated average temperature.

# Compute the mean temperature using pandas' built-in `.mean()` method for simplicity.
print(data["temp"].mean())  # Print the mean temperature.

# Find the highest temperature using pandas' built-in `.max()` method.
print(data["temp"].max())  # Print the maximum temperature value.

# Access the 'condition' column using two different notations for flexibility.
print(data["condition"])  # Access and print using bracket notation.
print(data.condition)  # Access and print using dot notation (works for valid column names).

# Retrieve a subset of the DataFrame where the 'day' matches "Monday".
# This filters the rows to get data specific to Monday.
print(data[data.day == "Monday"])  # Print the data for Monday.

# Retrieve the row where the temperature equals the maximum temperature in the dataset.
# This is useful to analyze the details of the day with the highest temperature.
print(data[data.temp == data.temp.max()])  # Print the row with the highest temperature.

# Extract only the data for Monday to perform specific calculations.
monday = data[data.day == "Monday"]
print(monday.condition)  # Print the weather condition for Monday.

# Convert the Monday temperature to an integer.
# Use `.iloc[0]` to get the scalar value from the single-row Series.
monday_temp = int(monday.temp.iloc[0])  # Ensure compatibility and avoid warnings.
# Convert the Monday temperature from Celsius to Fahrenheit.
monday_temp_f = (monday_temp * 9 / 5) + 32
print(monday_temp_f)  # Print the temperature in Fahrenheit for Monday.

# Create a new dataset from scratch using a dictionary.
# This demonstrates creating a DataFrame programmatically.
data_dict = {
    "students": ["Amy", "James", "Angela"],  # A list of student names.
    "scores": [76, 56, 65]  # Corresponding scores for each student.
}

# Convert the dictionary into a pandas DataFrame.
data = pandas.DataFrame(data_dict)

print(data)  # Print the newly created DataFrame to inspect its contents.

# Save the newly created DataFrame to a CSV file.
# This allows data to be persisted for further use or sharing.
data.to_csv("day_25_new_data.csv")
