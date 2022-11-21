# https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3
from itertools import permutations


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int((num ** (1 / 2))) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    num_list = [x for x in numbers]

    num_p = []
    for i in range(1, len(num_list) + 1):
        num_p += list(permutations(num_list, i))

    all_number = []
    for x in num_p:
        all_number.append(int("".join(x)))

    all_number = list(set(all_number))

    answer = 0
    for num in all_number:
        if is_prime(num):
            answer += 1

    return answer
