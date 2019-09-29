# -*- coding:utf-8 -*-

import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                     passwd='mirim2', db='seoulnight', charset='utf8')
cursor = db.cursor()


def create_review(id, location, article, star_score):
    sql = "INSERT INTO review (id, location, article, star_score) VALUES ('" + \
        id+"','"+location+"','"+article+"',"+str(star_score)+");"
    cursor.execute(sql)
    db.commit()
    db.close()
    return get_review_all()


def get_review(location):
    sql = "select * from review where location = " + location
    cursor.execute(sql)
    result = cursor.fetchone()
    db.close()
    return result


def get_review_all():
    sql = "select * from review"
    cursor.execute(sql)
    result = cursor.fetchone()
    db.close()
    return result

def modify(id, newarticle):
    sql = "UPDATE review SET article = '" +newarticle+"' WHERE id = '"+id +"'"
    cursor.execute(sql)
    db.commit()
    db.close
    return {"ok":True}

def delete(id,location):
    sql = "DELETE review WHERE id = " + id + " and location = " + location 
    cursor.execute(sql)
    db.commit()
    db.close
    return {"ok":True}
    


if __name__ == '__main__':
    create_review("nam", "seoul", "안뇽", 5)
