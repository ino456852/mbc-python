# todo_logic.py

# 계산기 시작 시 초기 입력값을 반환
def load():
    return ''  # 빈 문자열로 초기화


# 계산 결과나 수식을 저장하고 싶을 때 사용하는 함수 (여기선 생략 가능)
def save(expression):
    # 예: 마지막 수식을 파일에 저장할 수도 있음
    # with open('calc_history.txt', 'a') as file:
    #     file.write(expression + '\n')
    pass  # 지금은 사용 안 함


# 버튼을 눌렀을 때 해당 문자(char)를 현재 수식에 추가
def regist(char, expression):
    return expression + char


# 현재 수식을 그대로 리턴하는 함수 (사실 필요 없지만 예시용)
def list(expression):
    return expression


# 리스트에서 항목을 찾는 함수 (계산기에는 필요 없어서 제외)
# def find(no):
#     pass


# = 버튼 눌렀을 때 수식을 계산
def update(expression):
    try:
        result = eval(expression)  # 수식 계산
        return str(result)         # 결과를 문자열로 반환
    except:
        return 'Error'  # 계산 중 오류 발생 시


# C 버튼 눌렀을 때 마지막 문자 삭제
def delete(expression):
    return expression[:-1]  # 마지막 문자 제거
