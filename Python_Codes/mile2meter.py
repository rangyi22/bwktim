MILE_TO_METER = 1609

# meter = 1 * MILE_TO_METER
# print(1, 'mile is', meter)
# meter = 2 * MILE_TO_METER
# print(2, 'mile is', meter)
# meter = 3 * MILE_TO_METER
# print(3, 'mile is', meter)
# meter = 4 * MILE_TO_METER
# print(4, 'mile is', meter)

i = 1
while i < 101:
    meter = i * MILE_TO_METER
    print(i, 'mile is', meter)
    i += 1