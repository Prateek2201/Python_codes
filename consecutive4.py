def freqChk(arr):
    ele_cnt={}
    for element in arr:
        if element in ele_cnt:
            ele_cnt[element]+=1
        else:
            ele_cnt[element]=1
    for key,value in ele_cnt.items():
        if(value>=4):
            return key

def get_rows(grid):
    return [[c for c in r]for r in grid]
def get_columns(grid):
    return zip(*grid)
def get_diagonal(grid):
    b=[None]*(len(grid)-1)
    grid=[b[i:]+r+b[:i]for i,r in enumerate(get_rows(grid))]
    return [[c for c in r if not None]for r in get_columns(grid)]

n=int(input())
grid=[]
for i in range(n):
    grid.append(list(map(int,input().split(" "))))
finalList=[]
for i in range(n):
    finalList.append(freqChk(grid[i]))
columns= [[grid[j][i]for j in range(len(grid))]for i in range(len(grid[0]))]
for i in range(len(columns)):
    finalList.append(freqChk(columns[i]))
diagonal=get_diagonal(grid)
for i in range(len(diagonal)):
    finalList.append(freqChk(diagonal[i]))

finalList=[i for i in finalList if i]
if len(finalList)==0:
    print('-1')
else:
    print(min(finalList))
