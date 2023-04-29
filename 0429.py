#https://school.programmers.co.kr/learn/courses/30/lessons/120815
# def solution(n):
#     for i in range(1,101):
#         if i*6 % n == 0:
#             return i


######################################################################

# https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    return [i for i in range(n+1) if i%2 != 0]

print(solution(10))
print(solution(15))
