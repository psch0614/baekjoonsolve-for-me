a = input()
goal = a

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
for i in croatia :
    goal = goal.replace(i, 'a')

print(len(goal))
