import pymysql

class Database:

  insertCMD = 'insert into users(username,email,password) values(%s,%s,%s)'
  deleteCMD = 'delete from users where email = %s'
  updateCMD = 'update users set username = %s where email = %s'

  def __init__(self):
    try:
      self.db = pymysql.connect(host='database.cueluwhjjs5i.us-west-1.rds.amazonaws.com',user='admin',password='nikhilD8',charset='utf8mb4')
      self.cursor = self.db.cursor()
      self.cursor.execute('use nikhil')
    except:
      print("can't connect")
  
  def fetch(self):
    self.cursor.execute("select * from users")
    return self.cursor.fetchall()
  
  def add(self,data):
    try:
      self.cursor.execute(self.insertCMD,data)
      self.cursor.connection.commit()
      return 1
    except Exception as e:
      return {'error':str(e)}
  
  def findUser(self,email):
    self.cursor.execute("select password from users where email= %s",(email,))
    return self.cursor.fetchone()
  
  def delete(self,mail):
    try:
      self.cursor.execute(self.deleteCMD,(mail,))
      self.cursor.connection.commit()
      return 1
    except Exception as e:
      return {'error':str(e)}
  
  def update(self,email,username):
    try:
      self.cursor.execute(self.updateCMD,(username,email))
      self.cursor.connection.commit()
      return 1
    except Exception as e:
      return {'error':str(e)}
  
  def close(self):
    self.cursor.connection.close()

