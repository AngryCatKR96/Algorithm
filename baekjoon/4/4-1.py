import sys

input = sys.stdin.readline

seq = []

N = input()
seq = input().split()
v = input().strip()
 
print(seq.count(v))