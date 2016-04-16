import psycopg2
import sys

conn = psycopg2.connect(database="twitter", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

# Checks if there is exactly one argument    
if len(sys.argv) == 2:
    arg = (sys.argv[1])
    # Queries argument against checklist
    cur.execute("SELECT word FROM checker WHERE word like %s", (arg,))
    checker = cur.fetchall()
    # If word is in the checklist
    if checker:
	arg2 = "%" + arg + "%" # Adds wildcards to argument
        cur.execute("SELECT * FROM tweets WHERE word like %s order by count desc", (arg2,))
	records = cur.fetchall()	
	# Lists arguments (Tweet, Count)	
	for rec in records:
		print """  "%s": %s"""%(rec[0],rec[1])
    # if word is not in the checklist
    else:
        print "Please input valid word."
    conn.commit()
# If 0 or more than 1 word is passed as an argument
else:
    print "Please define only ONE word to search (use '' around phrases)."
