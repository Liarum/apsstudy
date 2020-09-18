# baekjoon 2439. 별찍기 -2
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
    stdout.write(" "*(n-i)+"*"*i+"\n")