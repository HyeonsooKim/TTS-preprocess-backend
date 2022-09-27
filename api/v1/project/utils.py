# api.v1.project.utils.py

# Embedded
import re

def preprocess(list):
    """ 텍스트 전처리 함수 """
    result = []

    # '.', '!', '?' 로 문장이 구분됩니다.
    splited_text = re.split(r'([.!?])', list[0])

    # 한글, 영어, 숫자, 물음표, 느낌표, 마침표, 따옴표, 공백를 제외한 나머지는 문장에 포함되지 않습니다.
    regex = '[^ㄱ-ㅎ가-힣a-zA-Z0-9?!.\'\" ]'

    for i in range(len(splited_text) // 2):
        # 문장의 맨앞, 맨뒤에는 공백이 위치하지 않습니다
        s = splited_text[2 * i].strip()
        s = re.sub(regex, '', s)

        # 빈 문장은 삭제됩니다.
        # 빈 문장이 아닐 경우 문장부호 다시 붙인 후 저장
        if len(s) > 0:
            result.append(s + splited_text[2 * i + 1])

    # 마지막 문장에 문장부호가 없는 경우 따로 추가
    if len(splited_text) % 2:
        s = splited_text[-1].strip()
        s = re.sub(regex, '', s)

        # 빈 문장이 아닐 경우 저장
        if len(s) > 0:
            result.append(s)

    return result