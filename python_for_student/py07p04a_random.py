#py07p04a_random.py
import random
event_freq = {'H': 0, 'T': 0}
events = list(event_freq.keys())
for i in range(1000000):
   event_freq[random.     (events)] += 1
print(event_freq)
