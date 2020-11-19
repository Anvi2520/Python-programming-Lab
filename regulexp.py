import re
pattern=r"[\w.-]+@[\w.-]+"
string="Please send your feedback at info@oxford.com"
match=re.search(pattern,string)
if match:
    print("Email to:",match.group())
else:
    print("No match")
