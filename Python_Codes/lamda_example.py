def call_10_times(func):
    for i in range(10):
        # Callback Function
        func(i)

call_10_times(lambda number: print("Hello. World!", number))