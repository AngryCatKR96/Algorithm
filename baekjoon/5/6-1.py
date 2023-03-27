def solve(a):
    ans = 0
    while a:
        ans += a.pop()
    return ans