import json
import timetostring
import random

def getRawStr():
    with open("results/results.json", "r") as fin:
        r = json.loads(fin.read())


    d = timetostring.getcurtime()

    return random.choice(r[str(d[0])][str(d[1])])
    
    


if __name__ == '__main__':

    print(getRawStr())