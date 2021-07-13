a = int(input())

# a 가홀수일 경우 Weird 를 출력
# a 가 짝수이고 2와 5 사이일 경우 Not Weird 출력
# a 가 짝수이고 6과 20 사이일 경우 Weird 출력
# a 가 20 보다 클 경우 Not Weird 출력


k = "Weird"
kn = "Not Weirtd"

if a % 2 != 0:
    print(k)

    if 2 < a < 5:
        print(kn)
    elif 6 < a < 20:
        print(k)
