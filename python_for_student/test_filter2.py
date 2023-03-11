#test_filter2.py
L1 = ["Python", "C#", "Java", "Go"]
L2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "C#"]
# 교집합(intersection) 구하기
L_int = list(filter(lambda x: x in L1, L2))
print("Intersection between two lists: ", L_int)
# 대칭적 차집합(symmetric difference) 또는 배타적 합집합 구하기
L12 = list(filter(lambda x: x not in L2, L1))
L21 = list(filter(lambda x: x not in L1, L2))
L_dif = L12 + L21
print("Difference between two lists: ", L_dif)
