import os


board = list([[0 for _ in range(8)] for _ in range(8)])
board[3][3] = 1
board[3][4] = 2
board[4][3] = 2
board[4][4] = 1
print('初始盤面： 1 為先手，2 為後手')
for line in board:
    print(line)
print()
game = True
g_round = 1 
while game:
    for player in ['先手1', '後手2']:
        print(f'第 {g_round} 回合')
        notyet = True
        while notyet:
            try:
                coord = input(f'輪到{player}，請指定落子處（1-1 ~ 8-8）：')
                if coord == 'end': break
                coord = list(map(eval, coord.split('-')))
                coord = list(map(lambda x: x-1, coord))
                assert board[coord[0]][coord[1]] == 0
                notyet = False
            except:
                print('輸入錯誤，請檢查是否該處已有棋子，再重新輸入')
        if coord == 'end': break
        board[coord[0]][coord[1]] = 1 if player == '先手1' else 2
        try:
            if (board[coord[0]][coord[1]+1] > 0) and (board[coord[0]][coord[1]+1] != board[coord[0]][coord[1]]):
                nextstep = 2
                try:
                    while (board[coord[0]][coord[1]+nextstep] > 0) and (board[coord[0]][coord[1]+nextstep] != board[coord[0]][coord[1]]):
                        nextstep += 1
                except:
                    nextstep -= 1
                finally:
                    if (board[coord[0]][coord[1]+nextstep] > 0) and (board[coord[0]][coord[1]+nextstep] == board[coord[0]][coord[1]]):
                        for chess in range(1, nextstep):
                            board[coord[0]][coord[1]+chess] = board[coord[0]][coord[1]]
        except:
            pass
        try:
            if (board[coord[0]][coord[1]-1] > 0) and (board[coord[0]][coord[1]-1] != board[coord[0]][coord[1]]):
                nextstep = 2
                try:
                    while (board[coord[0]][coord[1]-nextstep] > 0) and (board[coord[0]][coord[1]-nextstep] != board[coord[0]][coord[1]]):
                        nextstep += 1
                except:
                    nextstep -= 1
                finally:
                    if (board[coord[0]][coord[1]-nextstep] > 0) and (board[coord[0]][coord[1]-nextstep] == board[coord[0]][coord[1]]):
                        for chess in range(1, nextstep):
                            board[coord[0]][coord[1]-chess] = board[coord[0]][coord[1]]
        except:
            pass
        try:
            if (board[coord[0]+1][coord[1]] > 0) and (board[coord[0]+1][coord[1]] != board[coord[0]][coord[1]]):
                nextstep = 2
                try:
                    while (board[coord[0]+nextstep][coord[1]] > 0) and (board[coord[0]+nextstep][coord[1]] != board[coord[0]][coord[1]]):
                        nextstep += 1
                except:
                    nextstep -= 1
                finally:
                    if (board[coord[0]+nextstep][coord[1]] > 0) and (board[coord[0]+nextstep][coord[1]] == board[coord[0]][coord[1]]):
                        for chess in range(1, nextstep):
                            board[coord[0]+chess][coord[1]] = board[coord[0]][coord[1]]
        except:
            pass
        try:
            if (board[coord[0]-1][coord[1]] > 0) and (board[coord[0]-1][coord[1]] != board[coord[0]][coord[1]]):
                nextstep = 2
                try:
                    while (board[coord[0]-nextstep][coord[1]] > 0) and (board[coord[0]-nextstep][coord[1]] != board[coord[0]][coord[1]]):
                        nextstep += 1
                except:
                    nextstep -= 1
                finally:
                    if (board[coord[0]-nextstep][coord[1]] > 0) and (board[coord[0]-nextstep][coord[1]] == board[coord[0]][coord[1]]):
                        for chess in range(1, nextstep):
                            board[coord[0]-chess][coord[1]] = board[coord[0]][coord[1]]
        except:
            pass    
        try:
            if (board[coord[0]+1][coord[1]+1] > 0) and (board[coord[0]+1][coord[1]+1] != board[coord[0]][coord[1]]):
                nextstep = 2
                try:
                    while (board[coord[0]+nextstep][coord[1]+nextstep] > 0) and (board[coord[0]+nextstep][coord[1]+nextstep] != board[coord[0]][coord[1]]):
                        nextstep += 1
                except:
                    nextstep -= 1
                finally:
                    if (board[coord[0]+nextstep][coord[1]+nextstep] > 0) and (board[coord[0]+nextstep][coord[1]+nextstep] == board[coord[0]][coord[1]]):
                        for chess in range(1, nextstep):
                            board[coord[0]+chess][coord[1]+chess] = board[coord[0]][coord[1]]
        except:
            pass 
        try:
            if (board[coord[0]+1][coord[1]-1] > 0) and (board[coord[0]+1][coord[1]-1] != board[coord[0]][coord[1]]):
                nextstep = 2
                try:
                    while (board[coord[0]+nextstep][coord[1]-nextstep] > 0) and (board[coord[0]+nextstep][coord[1]-nextstep] != board[coord[0]][coord[1]]):
                        nextstep += 1
                except:
                    nextstep -= 1
                finally:
                    if (board[coord[0]+nextstep][coord[1]-nextstep] > 0) and (board[coord[0]+nextstep][coord[1]-nextstep] == board[coord[0]][coord[1]]):
                        for chess in range(1, nextstep):
                            board[coord[0]+chess][coord[1]-chess] = board[coord[0]][coord[1]]
        except:
            pass
        try:
            if (board[coord[0]-1][coord[1]+1] > 0) and (board[coord[0]-1][coord[1]+1] != board[coord[0]][coord[1]]):
                nextstep = 2
                try:
                    while (board[coord[0]-nextstep][coord[1]+nextstep] > 0) and (board[coord[0]-nextstep][coord[1]+nextstep] != board[coord[0]][coord[1]]):
                        nextstep += 1
                except:
                    nextstep -= 1
                finally:
                    if (board[coord[0]-nextstep][coord[1]+nextstep] > 0) and (board[coord[0]-nextstep][coord[1]+nextstep] == board[coord[0]][coord[1]]):
                        for chess in range(1, nextstep):
                            board[coord[0]-chess][coord[1]+chess] = board[coord[0]][coord[1]]
        except:
            pass
        try:
            if (board[coord[0]-1][coord[1]-1] > 0) and (board[coord[0]-1][coord[1]-1] != board[coord[0]][coord[1]]):
                nextstep = 2
                try:
                    while (board[coord[0]-nextstep][coord[1]-nextstep] > 0) and (board[coord[0]-nextstep][coord[1]-nextstep] != board[coord[0]][coord[1]]):
                        nextstep += 1
                except:
                    nextstep -= 1
                finally:
                    if (board[coord[0]-nextstep][coord[1]-nextstep] > 0) and (board[coord[0]-nextstep][coord[1]-nextstep] == board[coord[0]][coord[1]]):
                        for chess in range(1, nextstep):
                            board[coord[0]-chess][coord[1]-chess] = board[coord[0]][coord[1]]
        except:
            pass
        os.system('clear')
        print('最新盤面：')
        for line in board:
            print(line)
        print()
        if 0 not in sum(board, []):
            game = False
            break
    if coord == 'end': break
    g_round += 1

先手 = 0
後手 = 0
for i in sum(board, []):
    if i == 1:
        先手 += 1
    elif i == 2:
        後手 += 1
if 先手 > 後手:
    print(f'先手：{先手}，後手：{後手}，先手贏！')
elif 先手 < 後手:
    print(f'先手：{先手}，後手：{後手}，後手贏！')
else:
    print(f'先手：{先手}，後手：{後手}，和局！')