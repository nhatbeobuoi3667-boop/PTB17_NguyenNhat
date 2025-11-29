import random

def spin_rows():
    symbols = ['🍒','🍉', '🍋', '🔔', '7️⃣']
    return [random.choice(symbols) for _ in range(3)]
def print_rows(row):
    print("*"*12)
    print(" | ".join(row))
    print("*"*12)
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 6
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '7️⃣':
            return bet * 30
    return 0
def main():
    balance = 100000000

    print("-"*24)
    print("Welcome to Python Slots!")
    print("Symbols: 🍒 🍉 🍋 🔔 7️⃣")
    print("-"*24)

    while balance > 0:
        print(f"Your curent balance is: ${balance} ")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet
        row = spin_rows() 
        print("Spining...\n")
        print_rows(row)

        payout = get_payout(row, bet)

        # check for triple 7 first (JACKPOT)
        if row[0] == row[1] == row[2] == '7️⃣':
            print(f"JACKPOT!!! YOU WON {payout}")
        elif payout > 0:
            print(f"You won {payout}")
        else:
            print("You lost this round, sorry")
        
        balance += payout
        play_again = input("Do you want to play again(Y/N): ").upper()
        if play_again != "Y":
            break
    if balance > 0:
        print("Thank you for playing!")
    else:
        print("You don't anymore money")

if __name__ == '__main__':
    main()