
import pymysql

try:
    # 创建连接实例
    con = pymysql.Connect(user="root", password="123456", database="school")
    # 创建游标对象
    cursor = con.cursor()
    # 通过游标操作数据库添加数据
    cursor.execute("insert into teacher values(0,\"张老师\"),(0,\"刘老师\"),(0,\"王老师\");")
    cursor.execute("insert into class_grade values(0,\"一年级\"),(0,\"二年级\"),(0,\"三年级\"),(0,\"四年级\"),(0,\"五年级\");")
    cursor.execute("insert into class values(0,\"一年一班\",1),(0,\"二年一班\",2),(0,\"一年二班\",1),(0,\"二年二班\",2),\
                   (0,\"二年三班\",2),(0,\"三年一班\",3),(0,\"四年一班\",4),(0,\"四年二班\",4);")
    cursor.execute("insert into student values(0,\"judy\",\"女\",1),(0,\"张三\",\"男\",1),(0,\"李四\",\"女\",1),\
                   (0,\"李武\",\"男\",1),(0,\"kitty\",\"女\",2),(0,\"walter\",\"女\",2),(0,\"doris\",\"男\",2),\
                   (0,\"周公\",\"男\",2),(0,\"胡图\",\"男\",2),(0,\"李毅\",\"男\",2),(0,\"李二\",\"女\",3),\
                   (0,\"李三\",\"女\",3),(0,\"李柳\",\"男\",3),(0,\"张八\",\"男\",3),(0,\"王二\",\"男\",3),\
                   (0,\"王三\",\"男\",3),(0,\"王八\",\"女\",3),(0,\"张八\",\"男\",4),(0,\"王二\",\"女\",4),(0,\"王三\",\"男\",4);")
    cursor.execute("insert into course values(0,\"生物\",1),(0,\"物理\",2),(0,\"化学\",2),(0,\"英语\",3),(0,\"语文\",2);")
    cursor.execute("insert into teacher_class (tid,cid) values(1,1),(1,2),(2,2),(3,1),(3,2),(3,3);")
    cursor.execute("insert into score (stuid,courseid,score) values(1,1,80),(1,2,90),(1,3,88),(1,4,100),(1,5,100),\
                    (2,1,67),(2,3,99),(3,1,55),(3,2,33),(3,4,80),(4,2,56),(4,3,23),(4,4,88),(5,1,78),(6,2,45),(6,4,100),\
                    (6,3,80),(7,1,98),(7,2,85),(7,3,87),(7,4,74),(8,1,81),(8,2,82),(8,3,90),(9,4,96),(10,1,88),(12,1,80);")

    con.commit()

except Exception as e:
    con.rollback()

finally:
    # 释放连接实例
    cursor.close()
    con.close()
