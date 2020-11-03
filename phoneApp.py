#!/usr/bin/env python3
# namelookup.py - Program to display name statistics
# James Skon, 2019
import sys
import json
import cgi
import cgitb
#cgitb.enable()
# the following causes a message to be written in /fifo if the python program fails
cgitb.enable(display=0, logdir="/home/fifo")

sys.path.insert(1, '/home/skon/PhoneBookPython/')

from phoneBook import phoneBook

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
  l=open("/home/fifo/skon.log","a")
  l.write("Test Message:")
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
      print(json.dumps(pbResults))
    elif "First" in operation:
      pbResults=pb.findByFirst(search)
      print(json.dumps(pbResults))
    elif "Type" in operation:
      pbResults=pb.findByType(search)
      print(json.dumps(pbResults))
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
      print(json.dumps(pbResults))
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
      print(pbResults)
      print(json.dumps(pbResults))
    elif "delete" in operation:
      rid=form.getvalue("deleteid")
      pbResults=pb.delete(rid)
      print(json.dumps(pbResults))
    else:
      print("Error,Bad command:"+operation)
      #l.write("Error,Bad command:"+operation)
    l.close()
  else:
    print("Error in submission")

main()
