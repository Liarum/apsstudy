# baekjoon 2438. 별 찍기 -1
"""
*
**
***
****
*****
"""

from sys import stdin, stdout
n = int(stdin.readline())
for i in range(1, n+1):
    stdout.write("*"*i+"\n")
