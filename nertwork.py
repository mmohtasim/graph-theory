my_str = "UVACLYZLJBYL"

for i in range(26):
    new_str = ""
    for c in my_str:
        new_c = ord(c) + i
        if new_c > 90:
            new_c = new_c - 90 + 64
        new_str = new_str + chr(new_c)

    print(str(i) + "------>" + new_str)
