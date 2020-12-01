import timetostring
import re
import random
import json
from string import punctuation

if __name__ == '__main__':
    with open("./scrapedbooks/books.txt", "r") as fin:
        l = fin.read().split("\n")
        
    d = dict()

    for hour in range(1, 13):
        
        print("Parsing hour " + str(hour))
        
        d[hour] = dict()
        d[hour][1] = []
        d[hour][0] = []
        for i in l:
            
            with open("./scrapedbooks/" + i, "r") as fin:
                t1 = fin.read()
                t = t1.lower()
                for j in timetostring.timetostring(hour, True):
                    if t.find(j) != -1:
                        temp = t.find(j)
                        ts = re.split(' |\n', t1)
                        
                        a = -1
                        ind = 0
                        
                        for k in ts:
                            a += 1 + len(k)
                            if(a > temp):
                                break
                            ind += 1
                        
                        good = False
                        good1 = False
                        
                        for i in range(len(ts[ind])):
                            if ts[ind][i:].lower() == j.split(" ")[0]:
                                ts[ind] = ts[ind][:i] + "**" + ts[ind][i:]
                                good = True
                                break
                        
                        for i in range(len(ts[ind + len(j.split(" ")) - 1])):
                            if ts[ind + len(j.split(" ")) - 1][:i+1].lower() == j.split(" ")[-1] and (not j.split(" ")[-1] == "am" or ts[ind + len(j.split(" ")) - 1][:i+1] == j.split(" ")[-1]):
                                ts[ind + len(j.split(" "))-1] = ts[ind + len(j.split(" "))-1][:i+1].lower() + "**" + ts[ind + len(j.split(" "))-1][i+1:]
                                good1 = True
                                break
                        
                        if good and good1:
                            d[hour][1].append(" ".join(ts[ind-50:ind+50]))

                for j in timetostring.timetostring(hour, False):
                    if t.find(j) != -1:
                        temp = t.find(j)
                        ts = re.split(' |\n', t1)
                        
                        a = -1
                        ind = 0
                        
                        for k in ts:
                            a += 1 + len(k)
                            if(a > temp):
                                break
                            ind += 1

                        good = False
                        good1 = False
                        
                        for i in range(len(ts[ind])):
                            if ts[ind][i:].lower() == j.split(" ")[0]:
                                ts[ind] = ts[ind][:i] + "**" + ts[ind][i:]
                                good = True
                                break
                        
                        for i in range(len(ts[ind + len(j.split(" ")) - 1])):
                            if ts[ind + len(j.split(" ")) - 1][:i+1].lower() == j.split(" ")[-1] and (not j.split(" ")[-1] == "am" or ts[ind + len(j.split(" ")) - 1][:i+1] == j.split(" ")[-1]):
                                ts[ind + len(j.split(" "))-1] = ts[ind + len(j.split(" "))-1][:i+1].lower() + "**" + ts[ind + len(j.split(" "))-1][i+1:]
                                good1 = True
                                break
                        
                        if good and good1:
                            d[hour][0].append(" ".join(ts[ind-50:ind+50]))
                        
    print("Writing to JSON")
                        
    json_object = json.dumps(d, indent = 4)  

    with open("./results/results.json", "w+") as fout:
        fout.write(json_object) 
    



    