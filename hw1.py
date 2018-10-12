import re
import argparse

parser = argparse.ArgumentParser(description = "Date event regex for text analytics homework 1")
parser.add_argument("--input", default="input.txt", help="Path to input file")
parser.add_argument("--output", default="output.txt", help="Path to output file")


def find_holidays(input_text, results):
	""" This function searches for US Holidays from the following reference and returns matches.
	It looks for the full holiday name including day and if distinguishable, the hoiday name without day.

	Args:
		input_text (string): Input text to search 
		results (array): Array of matched results for the input text

	Returns:
		input_text (string): Input text without the matches
		results (array): An updated results array with the new matches
	""" 

	holidays = ["New Year's( Day)?",
				"Martin Luther King, Jr. Day",
				"George Washington’s Birthday",
				"Memorial Day",
				"Independence Day",
				"Labor Day",
				"Columbus Day",
				"Veterans Day",
				"Thanksgiving( Day)?",
				"Christmas( Day)?"]

	# Loops through each holiday in the list and creates a list of matches
	for holiday in holidays:
		regex = r"\b%s\b" % holiday
		matches = re.finditer(regex, input_text)
		# For each match in the matches list, appends to results and removes from input text so it's not double counted
		for match in matches:
			results.append(match.group())
			input_text = input_text.replace(match.group(), "")

	return input_text, results

def find_numbered_dates(input_text, results):
	""" This function searches for strings with a number only date component in the American notation (MM/DD/YYYY, MM-DD-YY, etc.) and returns matches.
	The string must have the date component and can have an optional time component, like afternoon or a specific time.

	Args:
		input_text (string): Input text to search 
		results (array): Array of matched results for the input text

	Returns:
		input_text (string): Input text without the matches
		results (array): An updated results array with the new matches
	""" 

	num_dates = r"\b[0-1]?[0-9][\/-][0-2]?[0-9][\/-](\d{4}\b|\d{2}\b)\s?(\d{0,2}(:\d{2})?\s?(am|AM|a.m.|pm|PM|p.m.)|morning|afternoon|evening|night)?"
	matches = re.finditer(num_dates, input_text)
	# For each match in the matches list, appends to results and removes from input text so it's not double counted
	for match in matches:
		results.append(match.group())
		input_text = input_text.replace(match.group(), "")

	return input_text, results

def find_dates_DOW(input_text, results):
	""" This function searches for strings with any type of written out date including a day of week and returns matches.
	The string must have the date component and can have an optional time component, like afternoon or a specific time.

	Args:
		input_text (string): Input text to search 
		results (array): Array of matched results for the input text

	Returns:
		input_text (string): Input text without the matches
		results (array): An updated results array with the new matches
	""" 

	# Supply list of weekdays and months to iterate through for regex
	weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

	# Utilize string substitution to create regular expressions for every combination of weekday and month
	for month in months:
		for day in weekdays:
			regex = r'(%s|%s)%s(%s)?\b\.?,?\s?(the\s\d{1,2}(st|nd|rd|th)?\sof\s)?(%s|%s)%s(%s)?\.?\s\d{0,2}(st|nd|rd|th)?,?\s?\d{0,4}\s?(\d{0,2} \
				(:\d{2})?\s?(am|AM|a.m.|pm|PM|p.m.)|morning|afternoon|evening|night)?' \
				% (day[0], day[0].lower(), day[1:3], day[3:], month[0], month[0].lower(), month[1:3], month[3:])
			matches = re.finditer(regex, input_text)
			# For each match in the matches list, appends to results and removes from input text so it's not double counted
			for match in matches:
				results.append(match.group())
				input_text = input_text.replace(match.group(), "")

	return input_text, results

def find_dates(input_text, results):
	""" This function searches for strings with any type of written out date and returns matches.
	The string must have the date component and can have an optional time component, like afternoon or a specific time.

	Args:
		input_text (string): Input text to search 
		results (array): Array of matched results for the input text

	Returns:
		input_text (string): Input text without the matches
		results (array): An updated results array with the new matches
	""" 

	# Supply list of months to iterate through for regex
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

	# Utilize string substitution to create regular expressions for every month
	for month in months:
		regex = r'(the\s\d{1,2}(st|nd|rd|th)?\sof\s)?(%s|%s)%s(%s)?\.?\s(\d{1,2}(st|nd|rd|th)?,\s\d{4}|\d{1,2}(st|nd|rd|th)?|\d{4})\s?(at\s)?(\d{0,2}\
			(:\d{2})?\s?(am|AM|a.m.|pm|PM|p.m.)|morning|afternoon|evening|night)?' % (month[0], month[0].lower(), month[1:3], month[3:])
		matches = re.finditer(regex, input_text)
		for match in matches:
			results.append(match.group())
			input_text = input_text.replace(match.group(), "")

	return input_text, results

def find_DOW(input_text, results):
	""" This function searches for strings with a day of week and returns matches.
	The string must have the day of week component and can have an optional time component, like afternoon or a specific time.

	Args:
		input_text (string): Input text to search 
		results (array): Array of matched results for the input text

	Returns:
		input_text (string): Input text without the matches
		results (array): An updated results array with the new matches
	""" 

	# Supply list of weekdays to iterate through for regex
	weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

	# Utilize string substitution to create regular expressions for every weekday
	for day in weekdays:
		regex = r'(%s|%s)%s(%s)?\b(\sthe\s\d{1,2}(st|nd|rd|th)?\s)?(\sat)?\s?(\.?,?\s?\d{0,2}(:\d{2})?\s?(am|AM|a.m.|pm|PM|p.m.)|morning|afternoon|\
			evening|night)?' % (day[0], day[0].lower(), day[1:3], day[3:])
		matches = re.finditer(regex, input_text)
		for match in matches:
			results.append(match.group())
			input_text = input_text.replace(match.group(), "")

	return input_text, results

def main(input_path, output_path):
	# Read input file
	with open(input_path, "r") as file:
		input_text = file.read()

	# Create empty array to store results
	results = []

	# Search for all date events
	input_text, results = find_holidays(input_text, results)
	input_text, results = find_numbered_dates(input_text, results)
	input_text, results = find_dates_DOW(input_text, results)
	nput_text, results = find_dates(input_text, results)
	input_text, results = find_DOW(input_text, results)

	# Write out results to text file
	with open(output_path, "w") as output:
		for result in results:
			output.write(result + "\n")

if __name__ == "__main__":
	args = parser.parse_args()
	input_path = args.input
	output_path = args.output

	main(input_path, output_path)
