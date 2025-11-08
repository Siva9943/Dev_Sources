"""
file=open("text_file1","w")
file.write("welcome to file handling")
file.write("hii siva\n")
file.close()
"""
with open("siva.txt") as f:
    print(f.read())
    f.seek(0)
    while True:
        line=f.readline()
        if not line:
            break
        elif "ERROR" in line:
            print(line.strip())
print("finished")

for _ in range(10):
    print("hhii")
