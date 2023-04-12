days = [69,98,420,666,9,911,67,46,39]

for x in range(len(days)-1):
    for y in range(len(days)-x-1):
        if days[y] > days[y+1]:
            temp = days[y]
            days[y] = days[y+1]
            days[y+1] = temp

print(days)
