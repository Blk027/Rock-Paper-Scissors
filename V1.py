#Beck waz here
import random

strategy_name = "Beat last move if repeating or counter mine or beat common patterns"

def beat_move(move):
    if (move=="r"):
        return "p"
    if (move == "p"):
        return "s"
    if (move=="s"):
        return "r"

def move(my_history, their_history):
    """This player always starts with rock
    """

    if (len(their_history) < 1):
        return "p"
    
    if (len(their_history) < 2):
        return "r"
    
    if (len(their_history) < 3):
        return "s"
   
    if (their_history[-1] == "p"):
        if (their_history[-2] == "s"):
            return "r"
    
    if (their_history[-1] == "s"):
        if (their_history[-2] == "p"):
            return "s"
    
    if (their_history[-1] == "s"):
        if (their_history[-2] == "r"):
            return "p"
    
    if (their_history[-1] == "r"):
        if (their_history[-2] == "s"):
            return "r"
    
    if (their_history[-1] == "p"):
        if (their_history[-2] == "r"):
            return "p"
    
    if (their_history[-1] == "r"):
        if (their_history[-2] == "p"):
            return "s"
    
    if (their_history[-1] == "r"):
        if (their_history[-2] == "p"):
            if (their_history[-3] == "s"):
                return "p"

    if (their_history[-1] == "s"):
        if (their_history[-2] == "r"):
            if (their_history[-3] == "p"):
                return "s"
    
    if (their_history[-1] == "p"):
        if (their_history[-2] == "s"):
            if (their_history[-3] == "r"):
                return "p"

    if (their_history[-1] == their_history[-2]):
        return beat_move(their_history[-1])
    return random.choice(["r", "p", "s"])
