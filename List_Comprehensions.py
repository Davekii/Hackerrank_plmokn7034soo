x = int(input())
y = int(input())
z = int(input())


n = int(input())


a =[(i,j,k) for i in range(n) for j in range(n) for k in range(n) if 0 <= i <= x and 0 <= j <= y and 0 <= k <= z and i+j+k != n ] 

print(a)

