import random
def gambler_problem():
    stake = int(input("Enter the initial stake: "))
    goal = int(input("Enter the goal amount: "))
    trials = int(input("Enter the number of trials: "))

    wins = 0
    total_bets = 0

    for _ in range(trials):
        current_stake = stake
        bets = 0
        while current_stake > 0 and current_stake < goal:
            bets += 1
            if random.random() < 0.5:
                current_stake += 1
            else:
                current_stake -= 1
        if current_stake == goal:
            wins += 1
        total_bets += bets

    print(f"Winning percentage: {wins / trials * 100:.2f}%")
    print(f"Average number of bets: {total_bets / trials:.2f}")

gambler_problem()
