import sys
input = sys.stdin.readline   #빠른입력

#입력데이터 정리
#입력 받기 + 행별 분할
data, brokenTeams, subTeams = [list(map(int, input().split(" "))) for i in range(3)]

#list를 변수로 해체 및 할당 (전체팀수, 부서진팀수, 여분있는팀수)
all, brokenCnt, subCnt = [data[i] for i in range(3)]







print(all, brokenCnt ,subCnt)
print(brokenTeams)
print(subTeams)



# my_list = ["apple orange", "banana cherry", "grape lemon"]
# split_list = [item.split() for item in my_list]
# print(split_list)
# https://www.educative.io/answers/what-is-attributeerror-list-object-has-no-attribute-split