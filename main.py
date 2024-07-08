import time 
from random import randint

def is_even(n: int) -> bool:
    if n <= 0:
        False 
    return n % 2 == 0


def get_reward(num: int) -> int:
    """ Return reward based on the number"""
    if num <= 0:
        return 0

    if is_even(num):
        return 1    
    
    return 0

reward_system = {
    "add": 0, "sub": 0
}


def get_decision() -> int:
    global reward_system

    add_weightage = reward_system["add"]+1
    sub_weightage = reward_system["sub"]+1


    num = randint(1,100)
    threshold = (add_weightage/(add_weightage+sub_weightage))*100
    if num < threshold:
        return 1
    return -1 


def walk(step_count=1000):
    START = 0

    for _ in range(step_count):

        """ rule 1: get decision to add or subtract 1 from the number"""
        direction = get_decision() 
        START+= direction


        reward = get_reward(START)
        if reward > 0:
            if direction == 1:
                reward_system["add"] += 1
            else:
                reward_system["sub"] += 1
    return START







def simulate():
    simulations = []
    for _ in range(100):
        res = walk()
        simulations.append(res)
    print(simulations)


simulate()
