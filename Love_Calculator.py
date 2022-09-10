#Love Caculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



n = name1.lower()
m = name2.lower()

T = n.count("t") + m.count("t")
R = n.count("r") + m.count("r")
U = n.count("u") + m.count("u")
E = n.count("e") + m.count("e")
total = T + R + U + E
L = n.count("l") + m.count("l")
O = n.count("o") + m.count("o")
V = n.count("v") + m.count("v")
E = n.count("e") + m.count("e")
sum = L + O + V + E

res = total * 10 + sum

if res < 10 or res >90: 
  print(f"your love score is {res} ,you go together like coke and mentos")
elif res >40 and res<50:
  print(f"your love score is {res} , you look great together")
else:
  print(f"your love score is {res}")
  
