def markusha(inspector):
    cap = [1] * (inspector + 1)
    for i in range(2, inspector + 1):
        if i == 3 or i == 5:
            cap[i] = 0
        else:
            cap[i] = cap[i - 1] + cap[i - 2]

    return cap[inspector]


print(markusha(20))  # 10946
