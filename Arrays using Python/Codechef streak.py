
def find_winner(N, om_solved, addy_solved):
    om_max_streak = 0
    addy_max_streak = 0
    om_current_streak = 0
    addy_current_streak = 0
    
    for i in range(N):
        if om_solved[i] > 0:
            om_current_streak += 1
            om_max_streak = max(om_max_streak, om_current_streak)
        else:
            om_current_streak = 0
        
        if addy_solved[i] > 0:
            addy_current_streak += 1
            addy_max_streak = max(addy_max_streak, addy_current_streak)
        else:
            addy_current_streak = 0
    
    if om_max_streak > addy_max_streak:
        return "Om"
    elif addy_max_streak > om_max_streak:
        return "Addy"
    else:
        return "Draw"


T = int(input())
for _ in range(T):
    N = int(input())
    om_solved = list(map(int, input().split()))
    addy_solved = list(map(int, input().split()))
    
    winner = find_winner(N, om_solved, addy_solved)
    print(winner)
