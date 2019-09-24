import csv
import os


a = os.listdir('.')
b = [] 
for name in a: 
    if not name.endswith('jpg-2'): 
        b.append(name) 
# C: 최종적으로 추출된 파일들
c =set(b)

with open('../annotation_final.csv', 'r') as q: 
        cs = csv.reader(q)
        annotation_final_dict = {}
        after_list = [] 
        for row in cs: 
            filename, number = row
            annotation_final_dict[filename] = number
            after_list.append(filename) 
        # D: annotation의 key 값만 있음                
        d = set(after_list) 


e = d - (d - c) # => 최종 annotation에서, file에는 없는 것들 제거
for after_filename in e:
    w = open('../annotation_final2.csv', 'at')
    after_cs =csv.writer(w)
    after_cs.writerow([after_filename, annotation_final_dict[after_filename]])
    w.close()


# 7개짜리만 추출
with open('../annotation_final2.csv', 'r') as q: 
        cs = csv.reader(q) 
        for row in cs: 
            filename, number = row 
            if len(number) == 7: 
                w = open('../annotation_len7.csv', 'at') 
                after_cs = csv.writer(w) 
                after_cs.writerow([filename, number]) 
                w.close() 