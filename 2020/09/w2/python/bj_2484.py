# baekjoon 2484. 주사위 네개

from sys import stdin, stdout

n = int(stdin.readline())
players = [list(map(int, stdin.readline().split())) for _ in range(n)]

max_price = 0
for player in players:
    dieyes_cnt = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    for i in range(4):
        dieyes_cnt[player[i]] += 1
    dieyes_cnt = sorted(dieyes_cnt.items(), key=lambda x: x[1], reverse=True)

    if dieyes_cnt[0][1] == 4:
        price = 50000 + dieyes_cnt[0][0] *5000
    elif dieyes_cnt[0][1] == 3:
        price = 10000 + dieyes_cnt[0][0] *1000
    elif dieyes_cnt[0][1] == 2:
        if dieyes_cnt[1][1] == 2:
            price = 2000+ dieyes_cnt[0][0] * 500 + dieyes_cnt[1][0] * 500
        else:
            price = 1000 + dieyes_cnt[0][0] * 100
    elif dieyes_cnt[0][1] == 1:
        price = max(dieyes_cnt[0][0], dieyes_cnt[1][0], dieyes_cnt[2][0], dieyes_cnt[3][0]) * 100

    if price > max_price:
        max_price = price

print(max_price)


########################################################################3

# from sys import stdin, stdout

# n = int(stdin.readline())
# players = [list(map(int, stdin.readline().split())) for _ in range(n)]
# max_money = 0


# for i in range(n):
#     cnt_set = set()
#     cnt_list = [0] * 7
#     a, b, c, d = players[i][0], players[i][1], players[i][2], players[i][3]
    
#     cnt_set.add(a)
#     cnt_list[a] += 1

#     cnt_set.add(b)
#     cnt_list[b] += 1

#     cnt_set.add(c)
#     cnt_list[c] += 1

#     cnt_set.add(d)
#     cnt_list[d] += 1


#     if len(cnt_set) == 1:
#         mon = 50000 + cnt_set.pop() * 5000
#     elif len(cnt_set) == 2:
#         a = cnt_set.pop()
#         b = cnt_set.pop()
#         if cnt_list[a] == 2 and cnt_list[b] == 2:
#             mon = 2000 + a * 500 + b * 500
#         elif cnt_list[a] == 3 or cnt_list[b] == 3:
#             valid_num = cnt_list[a] if cnt_list[a] == 3 else cnt_list[b]
#             mon = 10000 + valid_num * 1000
#     elif len(cnt_set) == 3:
#         a = cnt_set.pop()
#         b = cnt_set.pop()
#         c = cnt_set.pop()
#         valid_num = 0
#         if cnt_list[a] == 2:
#             valid_num = cnt_list[a]
#         elif cnt_list[b] == 2:
#             valid_num = cnt_list[b]
#         else:
#             valid_num = cnt_list[c]
#         mon = 1000 + valid_num * 100
#     else:
#         a = cnt_set.pop()
#         b = cnt_set.pop()
#         c = cnt_set.pop()
#         d = cnt_set.pop()
#         mon = max(a, b, c, d) * 100
    
#     if mon > max_money:
#         max_money = mon

# print(max_money)
    

