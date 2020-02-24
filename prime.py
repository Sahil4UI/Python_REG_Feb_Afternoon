for val in range(2, 21):
    for n in range(2, val):
        if (val % n) == 0:
            break
    else:print(val)
