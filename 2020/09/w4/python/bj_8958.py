# baekjoon 8958. OX퀴즈

n = int(input())

for _ in range(n):
    ox_string = input()

    total_score = 0 
    accum_score = 0
    
    for ox in ox_string:
        if ox == "O":
                accum_score += 1
                total_score += accum_score
        else:
            accum_score = 0

    print(total_score)
    
                


