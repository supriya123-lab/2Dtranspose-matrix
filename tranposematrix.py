X = [[1,6],
    [4 ,6],
    [3 ,3]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
      for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
