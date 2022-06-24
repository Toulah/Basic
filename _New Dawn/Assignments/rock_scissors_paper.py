# Rock Scissors Paper
# Rock=R, Scissors=S, Paper=P,
import random

elements = ["R", "S", "P"]
players = ["Demola", "Olaide", "Phillips", "Abd'Gafar", "Ibrahim", "Tobi", "Fatai"]
player_2 = random.choice(players)
print(f"""Welcome to the maiden edition of Rock Scissors Paper game
my name is {player_2} may I know your name please""")
player_1 = input("my name is: ")
# player_1 = external player, player_2 = computer

no_of_rounds = input("How many rounds would you like to play: ")

print(f"""Thank you {player_1}, 
at the prompt, please type R, P or S
R, P, and S each stand for Rock, Paper and Scissors respectively""")


p_1r = []
p_2r = []

rounds = 1
while rounds < (int(no_of_rounds) + 1):
    p_1 = input(player_1 + ": ")
    p_1 = p_1.upper()
    p_2 = random.choice(elements)
    print(player_2 + ": " + p_2)
    # r1 = result of external player, r2 result of CPU
    if p_1 == p_2:
        r1 = 0
        r2 = 0
    elif p_1 == "R" and p_2 == "S":
        r1 = 1
        r2 = 0
    elif p_1 == "R" and p_2 == "P":
        r1 = 0
        r2 = 1
    elif p_1 == "P" and p_2 == "R":
        r1 = 1
        r2 = 0
    elif p_1 == "P" and p_2 == "S":
        r1 = 0
        r2 = 1
    elif p_1 == "S" and p_2 == "P":
        r1 = 1
        r2 = 0
    elif p_1 == "S" and p_2 == "R":
        r1 = 1
        r2 = 0
    else:
        r1 = 0
        r2 = 1
        print("you have lost a round, please input R, S or P to continue")
    rounds += 1
    p_1r.append(r1)
    p_2r.append(r2)
    print(player_1 + ": " + str(p_1r))
    print(player_2 + ": " + str(p_2r))
