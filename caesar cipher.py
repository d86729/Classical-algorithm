def cipher():
    txt = "demo_demo_demo_demo_demo_demo_demo_demo_demo_demo"
    # txt = input()
    for i in range(ord("z")-ord("a")):
        idx = i + ord("a")
        # print(idx)
        for j in range(len(txt)):
            change = ord(txt[j])+i
            if change > ord('z'):
                change -= ord("z")-ord("a") + 1
            print(chr(change), end='')
        print()
    return


cipher()
