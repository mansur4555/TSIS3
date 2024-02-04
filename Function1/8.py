def spy_games(li):

    
    for idx in range(len(li)):
        
        if [0,0,7] == li[idx:idx+3]:
            return True

    
    return False

y = list(input())
print(spy_games(y))