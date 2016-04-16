import psycopg2
import sys

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
    
if len(sys.argv) == 2:
    arg = (sys.argv[1])
	cur.execute("""SELECT count FROM checker WHERE word=%s""", (arg,))
    checker = cur.fetchall()
	if checker:
        cur.execute("""SELECT * FROM tweets WHERE word=%s""", (arg,))
		for rec in records:
			print """  "%s": %s"""%(rec[0],rec[1])
    else:
        print "Please input valid word."
    conn.commit()
else:
    print "Please define only ONE word to search (use '' around phrases)."
