list01=["1","2","3","4","5","6",]
print(list01)
i=0
while i < 6:
    if "1" in list01[i]:
        list01[i]="a"
        i=i+1
    elif "2" in list01[i]: 
        list01[i]="b"
        i=i+1
    elif "3" in list01[i]:
        list01[i]="c"
        i=i+1
    elif "4" in list01[i]:
        list01[i]="d"
        i=i+1
    elif "5" in list01[i]:
        list01[i]="e"
        i=i+1
    elif "6" in list01[i]:
        list01[i]="f"
        i=i+1
    else:
        list01[i]="g"
        i=i+1
print(list01)