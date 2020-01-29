data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
print(len(data))    #印出有多少筆留言，一萬筆。
print(data[0])    #印出第一筆