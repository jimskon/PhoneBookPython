
import mysql.connector

class phoneBook:
  '''
  A class for interfacing with a mysql database
  '''
  def __init__(self):
    '''
    Create a connection to the database
    '''
    HOST = "localhost"
    USER = "test"
    DB = "test"
    PASS="KenyonTest2020"
    self.mydb = mysql.connector.connect(
      host=HOST,
      user=USER,
      passwd=PASS,
      database=DB,
      auth_plugin='mysql_native_password'
    )
    return

  def findByLast(self,last):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM PhoneBook WHERE Last like '%"+last+"%'");
    myresult = mycursor.fetchall()
    return(myresult)

  def findByFirst(self,first):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM PhoneBook WHERE First like '%"+first+"%'");
    myresult = mycursor.fetchall()
    return(myresult)

  def delete(self,idnum):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("DELETE FROM PhoneBook WHERE ID='"+idnum+"'")
      self.mydb.commit()
    except Exception as e:
      return "Error,"+ str(e)
    finally:
      self.mydb.close()
    return ("success")

  def addEntry(self,first,last,phone,ptype):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("INSERT INTO PhoneBook(First,Last,Phone,Type) VALUES ('"+first+"','"+last+"','"+phone+"','"+ptype+"')")
      self.mydb.commit()
    except Exception as e:
      return "Error,"+ str(e)
    finally:
      self.mydb.close()
    return ("success")

  def editEntry(self,idnum,first,last,phone,ptype):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("UPDATE PhoneBook SET First = '"+first+"', Last ='"+last+"', Phone ='"+phone+"', Type ='"+ptype+"' WHERE ID='"+idnum+"'")
      self.mydb.commit()
    except Exception as e:
      return "Error,"+ str(e)
    finally:
      self.mydb.close()
    return ("success")
