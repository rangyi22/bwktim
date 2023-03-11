#test_thread.py
import threading
import time
class Job:
  def __init__(self):
     self.list = []
  def do_something(self, n):
     print(f"\nJob {n} has begun.")
     time.sleep(n)  # n초 동안 중지
     print(f"Job {n} has ended.", end=' ')
     self.list.append(n)
L = [1.2, 1.3, 1] # 각 job을 수행하는 데 소요되는 미리 정해진) 시간 모음
job = Job() # Job class의 instance 생성
# threading을 이용하지 않고 L에 포함된 job들을 차례로 실행한다.
t0 = time.time() #datetime.datetime.now()
for n in L:
   job.do_something(n)
print("\njob.list : ", job.list)
tf = time.time() 
print("Time taken without threading: ", round(tf-t0, 2))
job = Job() # Job class의 instance 생성
# 이제 (L에 모아진 job들에 대해) threading을 이용해본다
t0 = time.time() 
threads = []
for n in L:
   thread = threading.Thread(target=job.do_something, args=(n,))
   thread.start()
   threads.append(thread)
for thread in threads:
   thread.join()
print("\njob.list : ", job.list)
tf = time.time() 
print("Time taken with threading: ", round(tf-t0, 2))
