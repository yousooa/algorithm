# 시저 암호
# 힌트: 알파벳 수 26
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].islower:
            s[i] = chr((ord(s[i]) - ord("a") + n) % 26 + ord("a"))
        elif s[i].isupper:
            s[i] = chr((ord(s[i]) - ord("A") + n) % 26 + ord("A"))
    return "".join(s)