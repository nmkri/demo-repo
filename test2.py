def mysplit(s):
    final = []
    app = []
    
    for char in s:
        if char == " ":
            if app == []:
                continue
            final.append("".join(app))
            app = []
        else:
            app.append(char)
    else:
        if app == []:
            return final
        final.append("".join(app))
    return final

print(mysplit("we wish you a merry christmas"))
print(mysplit("    rrrrr    "))
print(mysplit("andahappy new year"))
