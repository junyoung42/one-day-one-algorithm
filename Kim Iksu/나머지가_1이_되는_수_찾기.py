# https://school.programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):
    answer = 2
    while n % answer != 1:
        answer += 1

    return answer
