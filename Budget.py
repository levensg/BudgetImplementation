from gui import Ui_MainWindow
from PyQt4.QtGui import QApplication, QMainWindow
import sys
import MySQLdb

def dbProcessor(op, host, user, password, dbname):	
	try:
		db  =  MySQLdb.connect(host, user, password) # create a connection
		cursor  =  db.cursor() # prepare a cursor object
		cursor.execute(op + ' DATABASE ' + dbname + ';')
	except MySQLdb.Error as e:
		try:
			print( "Error %d: %s\n" % (e.args[0], e.args[1]))
		except IndexError:
			print( "Error %d: %s\n" % str(e))	
		
		print( "Exiting application...")
		
		sys.exit(1)
	else:
	
		if 'CREATE'  ==  op:
			print( "Database %s has been created" % dbname)
		elif 'DROP'  ==  op:
			print( "Database %s has been deleted" % dbname)

		cursor.close()
		db.close()


def budgetTbProcessor(op, host, user, password, dbname):
	try:
		db  =  MySQLdb.connect(host, user, password, dbname)
		cursor  =  db.cursor()

		if op  ==  'CREATE':
			sql_command  = """ CREATE TABLE BUDGET (
								TYPE CHAR(20),
								AMOUNT CHAR(20),
								DESCRIPTION CHAR(20),
								IN_OUT CHAR(20)
							)"""
		elif op  ==  'DROP':
			sql_command  =  'DROP TABLE BUDGET'
		else:
			print ('%s is not a valid option for method budgetTbCreator()' % op)
			sys.exit(1)
				
		cursor.execute(sql_command)
		
	except MySQLdb.Error as e:
		try:
			print( "Error %d: %s\n" % (e.args[0], e.args[1]))
		except IndexError:
			print ("Error %d: %s\n" % str(e)	)	
		
		print( "Exiting application..."	)	
		
		sys.exit(1)
	else:
		if op  ==  'CREATE':
			print ("TABLE budget in DATABASE %s has been created..." % dbname)
		elif op  ==  'DROP':
			print( "TABLE budget in DATABASE %s has been deleted..." % dbname		)
		
		cursor.close()
		db.close()


def addEntry(host, user, password, dbname, tbname, amount_type, amount, description, in_out, ui):
	try:
		db  =  MySQLdb.connect(host, user, password, dbname) # create a connection
		cursor  =  db.cursor() # prepare a cursor object
		
		check_existance  =  cursor.execute("""SELECT * from %s where type  =  %s and 
                                                                             amount  =  %s and
                                                                             description  =  %s and
                                                                             in_out  =  %s """ % (tbname, amount_type, amount, description, in_out))

		if check_existance  ==  0:
			sql_command  =  ('''INSERT INTO %s (type, amount, description, in_out)
						VALUES (%s, %s, %s, %s);''') % (tbname, amount_type, amount, description, in_out)
			cursor.execute(sql_command)
			db.commit()
			ui.REPORT_lbl.setText('Entry %s %s has been added to table %s' % (amount_type, amount, tbname))
			print ('Entry %s %s has been added to table %s' % (amount_type, amount, tbname))
			
		else:
			ui.REPORT_lbl.setText('Entry %s %s already exists' % (amount_type, amount))
			print('Entry %s %s already exists' % (amount_type, amount))
		
		
	except MySQLdb.Error as e:
		try:
			ui.REPORT_lbl.setText("Error %d: %s\n" % (e.args[0], e.args[1]))
			print ("Error %d: %s\n" % (e.args[0], e.args[1]))
		except IndexError:
			ui.REPORT_lbl.setText("Error %d: %s\n" % str(e))
			print ("Error %d: %s\n" % str(e))
		
		print ("Exiting application...")
		
		
		sys.exit(1)
	else:		
		
		cursor.close()
		db.close()
		
def removeEntry(host, user, password, dbname, tbname, amount_type, amount,ui):

	try:
		db  =  MySQLdb.connect(host, user, password, dbname) # create a connection
		cursor  =  db.cursor() # prepare a cursor object
		
		check_existance  =  cursor.execute("SELECT * from %s where type  =  %s and amount  =  %s" % (tbname, amount_type, amount))		
		
		if check_existance:
			sql_command  =  "DELETE FROM %s WHERE type  =  %s and amount  =  %s" % (tbname, amount_type, amount)
			cursor.execute(sql_command)		
			db.commit()
			print('Entry %s %s has been removed from table %s' % (amount_type, amount, tbname))
			ui.REPORT_lbl.setText('Entry %s %s has been removed from table %s' % (amount_type, amount, tbname))
		else:
			print ('Entry %s %s does not exist' % (amount_type, amount))
			ui.REPORT_lbl.setText('Entry %s %s does not exist' % (amount_type, amount))
		
	except MySQLdb.Error as e:
		try:
			print ("Error %d: %s\n" % (e.args[0], e.args[1]))
			ui.REPORT_lbl.setText("Error %d: %s\n" % (e.args[0], e.args[1]))
		except IndexError:
			print ("Error %d: %s\n" % str(e))
			ui.REPORT_lbl.setText("Error %d: %s\n" % str(e))
		
		print("Exiting application...")
		ui.REPORT_lbl.setText("Exiting application...")
		sys.exit(1)
	else:		
		cursor.close()
		db.close()	

		
def returnEntries(host, user, password, dbname, tbname,ui):

	entry_list  =  []

	try:
		db  =  MySQLdb.connect(host, user, password, dbname) # create a connection
		cursor  =  db.cursor() # prepare a cursor object
		
		sql_command  =  "SELECT * FROM BUDGET"
		
		cursor.execute(sql_command)
			
		data  =  cursor.fetchall()
		
	except MySQLdb.Error as e:
		try:
			print ("Error %d: %s\n" % (e.args[0], e.args[1]))
			ui.REPORT_lbl.setText("Error %d: %s\n" % (e.args[0], e.args[1]))
		except IndexError:
			print ("Error %d: %s\n" % str(e))
			ui.REPORT_lbl.setText("Error %d: %s\n" % str(e))
		
		print( "Exiting application...")
		
		sys.exit(1)
	else:
		print ('Entry list has been retrieved successfully')
		ui.REPORT_lbl.setText('Entry list has been retrieved successfully')
		
		return data
		
		cursor.close()
		db.close()	

def getBalance(host, user, password, dbname, tbname, ui):

	try:
		db  =  MySQLdb.connect(host, user, password, dbname) # create a connection
		cursor  =  db.cursor() # prepare a cursor object

                
		cursor.execute("SELECT amount FROM %s where in_out  =  'in'" % (tbname))
		money_in  =  list(cursor.fetchall())
		cursor.execute("SELECT amount FROM %s where in_out  =  'out'" % (tbname))
		money_out  =  list(cursor.fetchall())
		
		if len(money_in) == 0 and len(money_out) == 0:
			return 0
		else:
			a = 0
			for i in money_in:
				for j in i:
					j = int(j)
					a = a+j
			
			b = 0
			for i in money_out:
				for j in i:
					j = int(j)
					b = b+j
			return a-b
		
	except MySQLdb.Error as e:
		try:
			print "Error %d: %s\n" % (e.args[0], e.args[1])
			ui.REPORT_lbl.setText("Error %d: %s\n" % (e.args[0], e.args[1]))
		except IndexError:
			print "Error %d: %s\n" % str(e)
			ui.REPORT_lbl.setText("Error %d: %s\n" % str(e))
		
		print "Exiting application..."		
		
		sys.exit(1)
	else:		
		
		cursor.close()
		db.close()

def report_all(ui):
        b = []
        entries = list(returnEntries('localhost','root','levon92','MYDATABASE',"BUDGET",ui))

        if not entries:
                ui.REPORT_lbl.setText("There are no records.")
                return
        
        for i in entries:
                b.append("\n")
                for j in (i):
                        
                        b.append(str(j))
                        b.append(" ")
        b = "".join(b)
        ui.REPORT_lbl.setText(b)
        
def add(ui):        
	amount_type = str(ui.TYPE_te.text())
	amount = str(ui.AMOUNT_te.text())
	description = str(ui.DESCRIPTION_te.text())
	in_out = str(ui.IN_OUT_cb.currentText())

	if not amount_type or not amount or not description:
		ui.REPORT_lbl.setText('Please specify all fields')
		return
        
	if not is_number(amount):
		ui.REPORT_lbl.setText('Please enter a number for amount')
		ui.AMOUNT_te.setText("")
		return
	
	addEntry( 'localhost', 'root', 'levon92', 'MYDATABASE', "BUDGET", "'{}'".format(amount_type),\
                                                                          "'{}'".format(amount), \
                                                                          "'{}'".format(description),\
                                                                          "'{}'".format(in_out),\
                                                                          ui)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def remove(ui):
	amount_type = str(ui.TYPE_te.text())
	amount = str(ui.AMOUNT_te.text())
	description = str(ui.DESCRIPTION_te.text())
	in_out = str(ui.IN_OUT_cb.currentText())

	if not amount_type or not amount:
		ui.REPORT_lbl.setText("Please specify both 'Type' and 'Amount' fields")
		return
	
	removeEntry( 'localhost', 'root', 'levon92', 'MYDATABASE', "BUDGET", "'{}'".format(amount_type), "'{}'".format(amount),ui)


def balance(ui):
	amount_type = str(ui.TYPE_te.text())
	amount = str(ui.AMOUNT_te.text())
	description = str(ui.DESCRIPTION_te.text())
	in_out = str(ui.IN_OUT_cb.currentText())
	balance = str(ui.BALANCE_te.text())	
	result = str(getBalance( 'localhost', 'root', 'levon92', 'MYDATABASE', "BUDGET", ui))
	ui.BALANCE_te.setText(result)

def ex (ui):
        sys.exit()
      
def main():
        #dbProcessor('CREATE', 'localhost','root','levon92','MYDATABASE')
        #dbProcessor('DROP', 'localhost','root','levon92','MYDATABASE')		

        #budgetTbProcessor('CREATE', 'localhost','root','levon92','MYDATABASE')
        #budgetTbProcessor('DROP', 'localhost','root','levon92','MYDATABASE')		

	app  =  QApplication(sys.argv)
	window  =  QMainWindow()
	ui =  Ui_MainWindow()
	ui.setupUi(window)
	
	
	window.show()

	ui.ADD_btn.clicked.connect(lambda: add(ui))
	ui.REPORT_ALL_btn.clicked.connect(lambda: report_all(ui))
	ui.REMOVE_btn.clicked.connect(lambda: remove(ui))
	ui.BALANCE_btn.clicked.connect(lambda: balance(ui))
	ui.EXIT_btn.clicked.connect(lambda: ex(ui))
	sys.exit(app.exec_())
		
if __name__  ==  '__main__':
    main()
