# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):

    answer = ""
    cur_right = 12
    cur_left = 10

    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            cur_left = n
        elif n in [3, 6, 9]:
            answer += "R"
            cur_right = n
        else:
            if n == 0:
                n = 11

            dist_left = (abs(n - cur_left) // 3) + (abs(n - cur_left) % 3)
            dist_right = (abs(n - cur_right) // 3) + (abs(n - cur_right) % 3)
            print(dist_left, dist_right)

            if dist_left > dist_right:
                answer += "R"
                cur_right = n
            elif dist_left < dist_right:
                answer += "L"
                cur_left = n
            else:
                if hand == "left":
                    answer += "L"
                    cur_left = n
                else:
                    answer += "R"
                    cur_right = n

    return answer
