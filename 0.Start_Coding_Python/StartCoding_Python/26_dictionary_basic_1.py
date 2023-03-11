# 1. Win/Lose Check
# 2. Name of champions
# 3. Kill
# 4. Death 
# 5. Assist
# When using dictionary
play_data = {
    'result': 'Win',
    'champ_name': 'Viergo',
    'kill': 13,
    'death': 9,
    'assist': 17
}

# keys()
for key in play_data.keys():
    print(key)

# values()
for value in play_data.values():
    print(value)

# items()
for key, value in play_data.items():
    print(key, value)