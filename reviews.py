# 算出留言的平均長度(字數)
data = []
count = 0
with open('reviews2.txt', 'r') as f:
    for line in f:    #在讀取時是把一列資料讀進去，因此寫入data時也就是一筆留言
        data.append(line)    
        count += 1
        if count % 1 == 0:
            print(len(data))    #因為data是清單，因此len算來的是一百萬筆，而非所有文字的數量

# 這邊在計算總字數(空白也算)
sum_len = 0
for d in  data:
    sum_len= sum_len + len(d)
print(sum_len)    #印出總字數
print(sum_len/len(data))    #總字數除以筆數就是留言的平均字數