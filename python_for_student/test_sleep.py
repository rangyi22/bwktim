#test_sleep.py
import time
start = time.perf_counter() # (다음 행부터 작업이) 시작되는 시점
for i in range(5):
    print(i)
    time.sleep(0.5)
end = time.perf_counter() # (바로 전 행까지 작업이) 끝난 시점
run_time = end – start  # 작업을 실행하는 데 걸린 시간
print(run_time)
