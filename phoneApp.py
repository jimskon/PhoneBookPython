#!/usr/bin/env python3
# namelookup.py - Program to display name statistics
# James Skon, 2019
#!/usr/bin/env python

import cgi;
import cgitb
cgitb.enable()
# the following causes a message to be written in /tmp if the python program fails
cgitb.enable(display=0, logdir="/tmp")


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
    USER = "skon"
    DB = "PhoneAppDB"
    PASS="PhilanderChase"
    self.mydb = mysql.connector.connect(
      host=HOST,
      user=USER,
      passwd=PASS,
      database=DB
    )
    return

  def findByLast(self,last):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM Phonebook WHERE Last like '%"+last+"%'");
    myresult = mycursor.fetchall()
    return(myresult)
           
  def findByFirst(self,first):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM Phonebook WHERE First like '%"+first+"%'");
    myresult = mycursor.fetchall()
    return(myresult)
           
  def delete(self,idnum):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("DELETE FROM Phonebook WHERE ID='"+idnum+"'")
      self.mydb.commit()
    except Exception as e:
      return "Error,"+ str(e)
    finally:
      self.mydb.close()
    return ("success")
           
  def addEntry(self,first,last,phone,ptype):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("INSERT INTO Phonebook(First,Last,Phone,Type) VALUES ('"+first+"','"+last+"','"+phone+"','"+ptype+"')")
      self.mydb.commit()
    except Exception as e:
      return "Error,"+ str(e)
    finally:
      self.mydb.close()
    return ("success")
           
  def editEntry(self,idnum,first,last,phone,ptype):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("UPDATE Phonebook SET First = '"+first+"', Last ='"+last+"', Phone ='"+phone+"', Type ='"+ptype+"' WHERE ID='"+idnum+"'")
      self.mydb.commit()
    except Exception as e:
      return "Error,"+ str(e)
    finally:
      self.mydb.close()
    return ("success")
           
def printResults(results):
  print("Success,",end="")
  first=True
  for row in results:
    for field in row:
      if first:
        first = False
      else:
        print(",",end="",sep="")
      print(field,end="",sep="")
  print()
  return

def fixAttr(s):
  # fix missing attribute by converting to empty string 
  if s==None:
    return("")
  return(s)

def printHeader():
  print ("""Content-type: text/html\n""")

def main():
  printHeader()
  # the following allow debug messages to be written into /tmp
  #l=open("/tmp/skon.log","a")
  #l.write("Test Message:")
  pb=phoneBook()
  form = cgi.FieldStorage()
  if (form.getvalue("operation")):
    operation=form.getvalue("operation")
    #l.write("op:"+operation)
    search=form.getvalue("find")
    # Fix Null search parameter
    search=fixAttr(search)
    if search==None:
      search=""
    if "Last" in operation:
      pbResults=pb.findByLast(search)
      printResults(pbResults)
    elif "First" in operation:
      pbResults=pb.findByFirst(search)
      printResults(pbResults)
    elif "Type" in operation:
      pbResults=pb.findByType(search)
      printResults(pbResults)
    elif "Add" in operation:
      first=form.getvalue("afname")
      last=form.getvalue("alname")
      phone=form.getvalue("aphone")
      ptype=form.getvalue("atype")
      first=fixAttr(first)
      last=fixAttr(last)
      phone=fixAttr(phone)
      ptype=fixAttr(ptype)
      pbResults=pb.addEntry(first,last,phone,ptype)
      printResults(pbResults)
    elif "edit" in operation:
      idnum=form.getvalue("editid")
      first=form.getvalue("editfname")
      last=form.getvalue("editlname")
      phone=form.getvalue("editphone")
      ptype=form.getvalue("edittype")
      first=fixAttr(first)
      last=fixAttr(last)
      phone=fixAttr(phone)
      ptype=fixAttr(ptype)
      pbResults=pb.editEntry(idnum,first,last,phone,ptype)
      printResults(pbResults)
    elif "delete" in operation:
      rid=form.getvalue("deleteid")
      pbResults=pb.delete(rid)
      printResults(pbResults)
    else:
      printResults("Error,Bad command:"+operation)
      #l.write("Error,Bad command:"+operation)
    #l.close()
  else:
    print("Error in submission")
        
main()
