#test_thread_con.py
# Threading 효과를 실감해 보자
import threading, time
import concurrent.futures
class Job:
  def __init__(self):
     self.list = []
  def do_something(self, n):
     print(f"\nJob {n} has begun.")
     time.sleep(n) # 이 job processing을 n초 동안 중지한다.
     print(f"Job {n} has ended.", end=' ')
     self.list.append(n) # 완료된 job을 속속 list에 모은다.
     return n 
L = [1.2, 1.3, 1]
print(" With threading:")
t0 = time.time()
job = Job() # Job class의 instance 생성
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(job.do_something, n=n) for n in L]
    for f in concurrent.futures.as_completed(results):
       print("f.result() = ", f.result())
print("job.list : ", job.list)
tf = time.time() 
print("Time taken with threading: ", round(tf-t0, 2))
print("\n Without threading:")
t0 = time.time() # datetime.datetime.now()
job = Job() # Job class의 instance 생성
for n in L:
   job.do_something(n)
print("\njob.list : ", job.list)
tf = time.time() # datetime.datetime.now()
print("Time taken without threading: ", round(tf-t0, 2))
