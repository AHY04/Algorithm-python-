def solution(my_string, num1, num2):
    answer = list(my_string)
    answer[num1], answer[num2] = answer[num2], answer[num1]
    
    return ''.join(answer)

## '구분자'.join(리스트)함수를 사용해 리스트에 있는 요소를 하나의 문자열로 바꿔준다. (ex: '_'.join(['a', 'b', 'c']) -> "a_b_c")
