# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    len_elements = len(elements)
    elements = elements * 2

    answer = set()
    for i in range(len_elements):
        for j in range(len_elements):
            answer.add(sum(elements[j : i + j + 1]))

    return len(answer)
