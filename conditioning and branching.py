player_name="Lionel Messi"
sport="soccer"
achievements=7
if achievements>10:
    print(f"{player_name} plays {sport} and has {achievements} achivements.")
else:
    print(f"{player_name} does not have more than 10 achievements.")
player_name="Roger Federer"
sport="Tennis"
achievements=20
if sport=="Tennis" or achievements==20:
    print(f"{player_name} meets the criteria! They play {sport} and have {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria")
player_name="Ussain bolt"
sport="Athletics"
achievements=8
if achievements<10 and sport!="scoccer":
    print(f"{player_name} plays {sport} and has only {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria.")
