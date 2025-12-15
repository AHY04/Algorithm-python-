def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer+=int(i)
    return answer

## isdigit()함수는 문자열 내의 모든 문자가 숫자 문자(0-9)로만 구성되어 있을 때 True를 반환하고, 그렇지 않을 경우 False를 반환
