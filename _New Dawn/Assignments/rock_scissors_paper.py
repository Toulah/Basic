# Rock Scissors Paper
# Rock=R, Scissors=S, Paper=P,
import random

elements = ["R", "S", "P"]
players = ["Demola", "Olaide", "Phillips", "Abd'Gafar", "Ibrahim", "Tobi", "Fatai"]
player_2 = random.choice(players)
print(f"""Welcome to the maiden edition of Rock Scissors Paper game
my name is {player_2} may I know your name please""")
player_1 = input("my name is: ")

print(f"""Thank you {player_1}, 
at the prompt, please type R, P or S
R, P, and S each stand for Rock, Paper and Scissors respectively""")
p_1 = input(player_1 + ": ")
p_1 = p_1.upper()
p_2 = random.choice(elements)
print(player_2 + ": " + p_2)
p_1r = []
p_2r = []
if p_1 == p_2:
    r1 = 0
    r2 = 0
    p_1r.append(r1)
    p_2r.append(r2)
    print(player_1 + " = " + str(r1) + ", " + player_2 + " = " + str(r2))
elif p_1 == "R" and p_2 == "S":
    r1 = 1
    r2 = 0
    print(player_1 + " = " + str(r1) + " , " + player_2 + " = " + str(r2))
elif p_1 == "R" and p_2 == "P":
    r1 = 0
    r2 = 1
    print(player_1 + " = " + str(r1) + " , " + player_2 + " = " + str(r2))
elif p_1 == "P" and p_2 == "R":
    r1 = 1
    r2 = 0
    print(player_1 + " = " + str(r1) + " , " + player_2 + " = " + str(r2))
elif p_1 == "P" and p_2 == "S":
    r1 = 0
    r2 = 1
    print(player_1 + " = " + str(r1) + " , " + player_2 + " = " + str(r2))
elif p_1 == "S" and p_2 == "P":
    r1 = 1
    r2 = 0
    print(player_1 + " = " + str(r1) + " , " + player_2 + " = " + str(r2))
elif p_1 == "S" and p_2 == "R":
    r1 = 1
    r2 = 0
    print(player_1 + " = " + str(r1) + " , " + player_2 + " = " + str(r2))
