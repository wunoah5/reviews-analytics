# 因為每讀一筆就印出來一次計數，會導致速度很慢。
# 因此修改讓他每數一千次印出
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))