data = open("budget", "r")
budget = data.read().rstrip().split("\n")
for i in budget:
  for j in budget:
      for k in budget:
        if int(i) + int(j) + int(k) == 2020:
          print(int(i)*int(j)*int(k))
          exit()
