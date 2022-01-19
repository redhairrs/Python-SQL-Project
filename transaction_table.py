import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='9958626674/rishabh',database='bank')
cur = conn.cursor()
cur.execute('create table transactions(acct_no int(11),date date ,withdrawal_amt bigint(20),amount_added bigint(20) )')
