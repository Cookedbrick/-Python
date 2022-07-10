from itertools import cycle

cycle_list = [True, 3, 5.44, 'слово']
end = 3*len(cycle_list)
for i in cycle(cycle_list):
    if end == 0:
        break
    print(i)
    end -= 1
