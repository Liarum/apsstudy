# baekjoon 10951. A+B -4

# 두 정수 A, B 를 입력받은 다음 A + B를 출력
"""
1 1
2 3
3 4
9 8
5 2
"""

import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    sys.stdout.write(str(a+b)+"\n")
