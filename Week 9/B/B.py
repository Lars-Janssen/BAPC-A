def max_sub_array(L):
    n = len(L)
    best_sum = 0
    current_sum = 0
    for i in range(n):
        current_sum = max(0, current_sum + L[i])
        best_sum = max(best_sum, current_sum)
    return best_sum

firstline = input().split()
commercials = int(firstline[0])
price = int(firstline[1])
students = input().split()
profits = [int(students[i]) - price for i in range(commercials)]
print(max_sub_array(profits))