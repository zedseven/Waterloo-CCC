wonGames = 0

game1 = input("")
game2 = input("")
game3 = input("")
game4 = input("")
game5 = input("")
game6 = input("")

if game1 == "W":
    wonGames += 1
if game2 == "W":
    wonGames += 1
if game3 == "W":
    wonGames += 1
if game4 == "W":
    wonGames += 1
if game5 == "W":
    wonGames += 1
if game6 == "W":
    wonGames += 1

if wonGames == 0:
    print(-1)
elif wonGames > 0 and wonGames <= 2:
    print(3)
elif wonGames > 2 and wonGames <= 4:
    print(2)
elif wonGames > 4 and wonGames <= 6:
    print(1)
