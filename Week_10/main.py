import pprint
import re

# How automate the borking stuff makes matches
myRegexPatterns = re.compile(r"\d\d\d")
print(myRegexPatterns.search("abc123def"))

# A different way to do the same thing:
# Did we find a pattern?  Here, yes:
print(re.search(r"\d\d\d", "abc123def"))


# Did we find a pattern?  Here, no... don't have 4 digits in a row, only 3.
print(re.search(r"\d\d\d\d", "abc123def"))


# We can use this in an if statement to check if we found a match:
if re.search(r"\d\d\d", "abc123def"):
    print("Found match!")
else:
    print("NOT found")

if re.search(r"\d\d\d\d", "abc123def"):
    print("Found match!")
else:
    print("NOT found")


# Is this a phone number?
print(re.search("\d\d\d-\d\d\d-\d\d\d\d", "abc123def"))
print(re.search("\d\d\d-\d\d\d-\d\d\d\d", "612-555-1212"))

# Is there a phone number somewhere in string?
# Pattern is three digits, a dash, three digits, a dash, then four digits.
print(re.search("\d\d\d-\d\d\d-\d\d\d\d", "Do not call 612-555-1212, no one will pick up."))
print(re.search("\d{3}-\d{3}-\d{4}", "Do not call 612-555-1212, no one will pick up."))

# Another shortcut
print(re.search("\d+-\d+-\d+", "Do not call 612-555-1212, no one will pick up."))
# ... but lets too many things pass.
print(re.search("\d+-\d+-\d+", "123-56-7890"))


# Multiple matches
print(re.search("\d{3}-\d{3}-\d{4}", "Do not call 612-555-1212, call 800-223-4567"))
print(re.findall("\d{3}-\d{3}-\d{4}", "Do not call 612-555-1212, call 800-223-4567"))



# Capturing parts
matchObj = re.search("\d\d\d-(\d\d\d)-\d\d\d\d", "Do not call 612-555-1212, no one will pick up.")
print(matchObj.groups())
print(matchObj.group(1))

# Groups within multiple matches
# 'match' gets each full match one at a time, then you can pull groups out of them.
# See: https://pynative.com/python-regex-capturing-groups/#h-regex-capture-group-multiple-times
phoneRegex = re.compile("\d\d\d-(\d\d\d)-\d\d\d\d")
for match in phoneRegex.finditer("Do not call 612-555-1212, call 800-223-4567"):
    print(match.groups())


# Using spaces, non-spaces, and digits
print(re.search("\S\s\d\d\S\S", "a 12_x"))


# Practical example
# https://httpd.apache.org/docs/2.4/logs.html
# https://stackoverflow.com/questions/30956820/log-parsing-with-regex
logEntry1 = '''127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I ;Nav)"'''
logRegex = re.compile("^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] (\S+) (\S+)\s*(\S+)?\s* (\d{3}) (\S+)")

# Parse the log entry with the regex, show results
matchesObj = logRegex.search(logEntry1)
pprint.pprint(matchesObj.groups())

# Get a part of it.
print(matchesObj.group(3))
