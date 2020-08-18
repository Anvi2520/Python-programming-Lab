cntf = 0
cntn = 0
for num in range (1,101): 
    if (num * num) % 10 == 4: 
        cntf += 1 
    if (num * num) % 10 == 9:
        cntn += 1
print("ending by 4: ",cntf,"\nending by 9: ",cntn) 
