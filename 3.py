n = int(input())
used = set()
for i in range(used):
    vst  = input()
    if vst in used:
        print("YES")
    else:
        used.add(vst)
        print("NO")

