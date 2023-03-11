#test_thread1.py
import threading, time
class Job_:
  def __init__(self):
     self.val = [0, 0]
  def counter(self, N, i=1, Ts=0):
     print(f"\nJob_ {i} with Ts={Ts} has begun.")
     if i==1:
       for n in range(N):  self.val[0] += 1;  time.sleep(Ts)
     else:
       for n in range(N):  self.val[1] -= 1;  time.sleep(Ts)     
     print(f"Job_ {i} has ended.", end=' ')     
N = 1000;  Ts = 0
L = [1, 2] # job 번호로 구성된 list
job = Job_()  # Job_ class의 instance 생성  
# threading 없이 (list L에 있는 번호에 해당되는) job들을 수행해보자.
t0 = time.time() 
for i in L:  
   job.counter(N, i, Ts)
print("\njob.val : ", job.val)
tf = time.time()  # Job_ class의 instance 생성  
print("Time taken without threading: ", round(tf-t0, 2))
job = Job_()  # Job_ class의 instance 생성  
# threading을 사용해서 (list L에 있는 번호에 해당되는) job들을 수행해보자.
t0 = time.time()
threads = []
for i in L:
   thread = threading.Thread(target=job.counter, args=(N,I,Ts))
   thread.start()
   threads.append(thread)
for thread in threads:
   thread.join()
print("\njob.val : ", job.val)
tf = time.time() 
print("Time taken with threading: ", round(tf-t0, 2))
