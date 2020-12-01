data = open("budget", "r")
budget = data.read().rstrip().split("\n")
for i in budget:
  for j in budget:
    if int(i) + int(j) == 2020:
      print(int(i)*int(j))
      exit()
