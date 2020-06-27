import random
lst = [
    "You Will Not Be Affected By Corona",
    "You Will Have The Worst Time In Quarantine",
    "You Will Find Something Intresting To Do In Quarantine",
    "Within 5 Days, You will Start To Exersize",
    "You Will Take Advantage Of Quarantine And Sleep All Day", 
    "You Will Change Because of Corona", 
    "You Will Achieve Something Great During Quarantine"
]  

def fortune_teller(lst):
 if raw_input("Do You Want To Learn Your Fortune?") == "yes" or " yes":
    rand_int = random.randint(0,6)
    return lst[rand_int]
 else:
   "Im sorry, I didn't get that, please reply with yes"

print(fortune_teller(lst))
