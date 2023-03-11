def call_10_times(func):
    for i in range(10):
        # Callback Function
        func(i)

def print_hello(number):
    print("Hello. World!", number)

call_10_times(print_hello)