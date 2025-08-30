class Operations:
    def sum(x):
        c=x[0]
        for i in x:
            if i>c:
                c=i
        return c
