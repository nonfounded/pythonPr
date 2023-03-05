def s():
    global lst
    #
    for i in range(len(lst)):
        finish = True
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                finish = False
        if finish:
            break


lst = input().split()
print(lst)
s()
print(lst)
