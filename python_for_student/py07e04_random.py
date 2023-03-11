#py07e04_random.py
# 당첨번호 K개 임의선정
import random 
applicants = ['영희','철수','재석','가희','민석','오성','길동','개똥']
K = 2
# ~.sample() 함수를 이용
winners = random.sample(applicants, K)
print(winners)
# ~.shuffle() 함수를 이용
random.shuffle(applicants)
winners1 = applicants[0:K]
print(winners1)
