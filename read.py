data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))
print('档案读取完了，总共有', len(data), '笔资料')

sum_line = 0 # 平均长度=总长度/个数
for x in data:
    sum_line += len(x)
print('留言平均长度为: ', sum_line / len(data))

#y = []
#for d in data:
    #if len(d) < 100:
        #y.append(d)

y = [d for d in data if len(d) < 100]   
print('共有', len(y), '条留言少于100字')

#bad = []
#for q in data:
    #if 'bad' in q:
        #bad.append(q)
#print(len(bad))
#print(bad[5])

bad = [q for q in data if 'bad' in q]
print('提到bad的留言有', len(bad), '条')
print('例如\n', bad[3])

