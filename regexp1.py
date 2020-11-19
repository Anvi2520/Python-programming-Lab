import re
pattern=r"^[0-9]+ .*"
string="12 abc"
match=re.search(pattern,string)
if match:
    print("match")
