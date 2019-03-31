data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
print('档案读取完了，总共有: ', len(data), '笔资料')
sum_len = 0
for d in data:
    sum_len += len(d)
print('每笔留言的平均长度是: ', sum_len / len(data))
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '笔留言长度小于100')
print(new[0])
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '笔留言提到good')
print(good[0])