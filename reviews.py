# 留言篩選
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:    #在讀取時是把一列資料讀進去，因此寫入data時也就是一筆留言
        data.append(line)    
        count += 1
        if count % 100000 == 0:
            print('已算到', len(data), '筆')    #因為data是清單，因此len算來的是一百萬筆，而非所有文字的數量

# 這邊在計算總字數(空白也算)
sum_len = 0
for d in  data:
    sum_len= sum_len + len(d)
print('留言總字數為', sum_len)    #印出總字數
print('留言平均長度為', sum_len/len(data))    #總字數除以筆數就是留言的平均字數
print('留言平均長度為', round(sum_len/len(data),2))    #round(a,b) 取a的資料四捨五入到小數第b位

# 這邊在篩選留言字數小於100
new = []   #建立一個新清單，用來裝過濾後的資料
for d in data:
    if len(d) < 100:    #如果留言字數小於100才裝進新清單
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')

# 這邊在篩選特定文字
good = []   #建立一個新清單，用來裝過濾後的資料
for d in data:
    if 'good' in d:    #如果留言字數小於100才裝進新清單
        good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

#篩選特定文字的快寫法
good =[d for d in data if 'good' in d]
    # 上面這行 output = [運算 for 變數 in 清單 篩選條件]
    #第一個d因為沒有要運算，因此是把留言append(d)的哪個d放進去good[]
