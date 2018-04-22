e2f = {"dog" : "chien", "cat" : "chat", "walrus" : "morse"}
f2e = {}
for key,value in e2f.items():
    f2e[value] = key
print(f2e["chien"])

