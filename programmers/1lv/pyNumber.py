# 문자열 내 p와 y의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
  return s.lower().count("y") == s.lower().count("p")