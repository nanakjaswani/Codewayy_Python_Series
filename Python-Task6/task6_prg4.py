import re

a_string = input("Enter the string ")
substring = "at"

matches = re.finditer(substring, a_string)


matches_positions = [match.start() for match in matches]

print(matches_positions)
