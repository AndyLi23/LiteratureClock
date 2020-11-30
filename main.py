import timetostring

with open("./scrapedbooks/books.txt", "r") as fin:
    l = fin.read().split("\n")
    
for hour in range(1, 13):
    a = 0
    b = 1
    for i in l:
        try: 
            with open("./scrapedbooks/" + i, "r") as fin:
                t = fin.read().lower()
                for j in timetostring.timetostring(hour, True):
                    if t.find(j) != -1:
                        #print(i, t[t.find(j):t.find(j)+len(j)])
                        a += 1
            
                        
                for j in timetostring.timetostring(hour, False):
                    if t.find(j) != -1:
                        #print(i, t[t.find(j):t.find(j)+len(j)])
                        b += 1
                        

                               
        except:
            pass
    
    if a == 0:
        print(hour, True)
    if b == 0:
        print(hour, False)

    