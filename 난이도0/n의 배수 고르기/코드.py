def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n == 0:
            answer.append(i)
    return answer

## array.append(x)형태로 사용하며 array에 새로운 요소 추가 가능
## array.extend(iterable)은 입력한 iterable자료형의 항목들을 array의 맨 끝에 모두 추가
## array.insert(i,x)는 array의 원하는 위치 i앞에 x값 삽입 가능
