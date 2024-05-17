import random
class Match:
    def __init__(self, score, player1, player2, year, tournament):
        self.score = score
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.year = year
        self.tournament = tournament


match1 = Match("6-3 3-6 7-6", "Roger Federer", "Rafael Nadal", 2008, "Wimbledon")
match2 = Match("6-4 6-4 6-4", "Andy Murray", "Juan Martin del Potro", 2012, "Olympics")
match3 = Match("5-7 6-4 6-4", "Jack Sock", "Novak Djokovic", 2007, "US Open")
match4 = Match("4-6 6-3 6-3", "Dominic Thiem", "Alexander Zverev", 2020, "US Open")
match5 = Match("7-5 3-6 6-1", "Stan Wawrinka", "Kei Nishikori", 2015, "French Open")
match6 = Match("6-2 5-7 6-4", "David Ferrer", "Jo-Wilfried Tsonga", 2013, "Australian Open")
match7 = Match("7-6 4-6 6-3", "Marin Cilic", "Grigor Dimitrov", 2017, "Wimbledon")
match8 = Match("6-4 3-6 6-3", "Tomas Berdych", "Milos Raonic", 2016, "French Open")
match9 = Match("4-6 7-5 6-2", "Kevin Anderson", "Lucas Pouille", 2018, "US Open")
match10 = Match("5-7 7-6 6-4", "John Isner", "Gael Monfils", 2019, "Australian Open")


def main():
    print("Welcome to the Tennis Betting Game!")

    match1.winner = match1.player1
    match2.winner = match2.player1
    match3.winner = match3.player2
    match4.winner = match4.player1
    match5.winner = match5.player2
    match6.winner = match6.player2
    match7.winner = match7.player1
    match8.winner = match8.player2
    match9.winner = match9.player1
    match10.winner = match10.player1

    matches = random.sample([match1, match2, match3, match4, match5, match6, match7, match8, match9, match10], 3)

    #             0        1        2
    #matches = [match4, match8, match9]
    match = input("Enter the match number (1, 2, 3): ")

    current_match = matches[int(match) - 1]

    print("Match: " + current_match.player1 + " vs " + current_match.player2)
    print("Tournament: " + current_match.tournament)
    print("Year: " + str(current_match.year))

    money = input("How much are you betting ($): ")
    bet_guess = input("Enter your guess (1 or 2): ")

    if bet_guess == "1":
        guessed_player = current_match.player1
    if bet_guess == "2":
        guessed_player = current_match.player2

    if current_match.winner == guessed_player:
        print("Congratulations! You won $" + str(money * 2))
    else:
        print("Congratulations, you lost $" + str(money))

if __name__ == "__main__":
    main()