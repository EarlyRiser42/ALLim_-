def solution(str1, str2):
    list1, list2 = [], []
    # 두 문자씩 끊어서 list에 넣는다. 이때 두 문자중 하나라도 영문자가 아니면 넣지않고, 넣을때는 소문자 변환하여 넣는다
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            list1.append((str1[i] + str1[i + 1]).lower())

    for j in range(len(str2) - 1):
        if str2[j].isalpha() and str2[j + 1].isalpha():
            list2.append((str2[j] + str2[j + 1]).lower())

    # 합집합 원소의 개수를 구하기 위해 미리 두 list의 길이들을 더한다. 왜냐하면 합집합은 전체 원소의 개수- 교집합 원소의 개수이기 때문이다.
    parent = len(list1) + len(list2)
    # 둘다 공집합이라면 65536 return
    if not list1 and not list2:
        return 65536
    # 하나라도 공집합이라면 교집합은 0이므로 0 return
    elif not list1 or not list2:
        return 0
    else:
        child = 0
        if len(list1) >= len(list2):
            for element in list2:
                if element in list1:
                    # 한 list에 있는 원소가 다른 list에 있다면 count를 하나 올린 후 다른 list에서 그 원소를 삭제함으로써 중복연산되는 것을 방지.
                    child += 1
                    del list1[list1.index(element)]
        else:
            for element in list1:
                if element in list2:
                    child += 1
                    del list2[list2.index(element)]
        # 합집합 = 전체 집합 - 교집합
        parent -= child
        return int((child / parent) * 65536)
