import pymysql

# executemany 파트

cur = pymysql.connect()

sql = """ 
INSERT INTO brs_yoonkh.post_lists (id, post_type_num, title_name) VALUES (%s, %s, %s)"""
data = (('10', '10', '여자친구 게시판'),
        ('11', '11', '마마무 게시판'), 
        ('12', '12', '블랙핑크 게시판'), 
        ('13', '13', '위너 게시판'), 
        ('14', '14', '아이콘 게시판')) 
cur.executemany(sql, data) 