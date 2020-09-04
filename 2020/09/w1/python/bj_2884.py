# baekjoon 2883 알람시계

h, m = input().split()
h, m = int(h), int(m)

total_m = (h * 60 + m) - 45
if total_m < 0:
    total_m += 1440\
        
print("{} {}".format(total_m // 60, total_m % 60))

###
# a,b=map(int,input().split());x=a*60+b-45;print(x//60%24,x%60)