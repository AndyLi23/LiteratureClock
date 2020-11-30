import datetime

def timetostring(hour, pm):
    
    #hour = int(str(datetime.datetime.today()).split(" ")[1].split(":")[0])
   # minute = int(str(datetime.datetime.today()).split(" ")[1].split(":")[1])
    #pm = True
    #if hour == 0:
    #    hour = 12
    #    pm = True
    #elif(hour > 12):
    #    hour = hour - 12
     #   pm = True

        
    nums = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve"]
    
    aft = [" in the afternoon", " o&apos;clock", " o&apos;clock in the afternoon", " pm"]
    even = [" in the evening", " at night", " o&apos;clock", " o&apos;clock in the evening", " o&apos;clock at night", " pm"]
    morn = [" in the morning", " o&apos;clock"," o&apos;clock in the morning", " am"]
    
    if(hour == 12 and pm):
        return ["midnight"]
    elif(hour == 12):
        return ["noon"]
    elif(hour > 4 and pm):
        return [nums[hour] + i for i in even]
    elif(pm):
        return [nums[hour] + i for i in aft]
    else:
        return [nums[hour] + i for i in morn]