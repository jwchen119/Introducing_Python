second = 1
minute = 1
second_per_hour = 60 * second * 60 * minute
seconds_per_day = second_per_hour * 24

print('浮點除法:')
print(seconds_per_day / second_per_hour)
print('整數除法:')
print(seconds_per_day // second_per_hour)
print('除法除浮點特性外結果一致')
