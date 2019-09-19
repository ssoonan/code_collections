import csv


with open('annotation_final.csv', 'r') as q: 
    cs = csv.reader(q) 
    for row in cs: 
        filename, number = row 
        if len(number) == 7: 
            w = open('annotation_after.csv', 'at') 
            after_cs = csv.writer(w) 
            # csv.writer에는 writerow로 iterable을 넣어서 write함!
            after_cs.writerow([filename, number]) 
            w.close() 
             
