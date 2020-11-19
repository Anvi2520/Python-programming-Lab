import re
result=re.findall(r'\d{2}-\d{2}-(\d{4})','Hello, my name is Anvitha and my date of joining is 12-06-2020 and have experience of more then 2 years')
print("Date of appointment is:",result)

import re
list=['7838456789','1234567890','9876543210','8901234567','4567890123']
for i in list:
    result=re.findall(r'[7-9]{1}[0-9]{9}',i)
    if result:
        print(result,end=" ")


import re
pattern=r'[aeiou]'
if re.search(pattern,"bcdfg"):
    print("\nmatch found")
else:
    print("\nnot found")


import re
def pluralize(noun):
    if re.search('[sxz]$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeiousgkprt]h$',noun):
        return re.sub('$','es',noun)
    elif re.search('[aeiou]y$',noun):
        return re.sub('y$','ys',noun)
    else:
        return noun + 's'
list=["bush","fox","toy","cap"]
for i in list:
    print(i,'-',pluralize(i))
