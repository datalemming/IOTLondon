#Changed to load just the '668' dataset due to file size of the full dataset

#Changed to load into the TS 1.4 table 'aarhus'
"""
['extid', 'varchar', False, 1, 1, None, None]
['ts', 'timestamp', False, 2, 2, 30, 'd']
['avgMeasuredTime', 'sint64', False, None, None, None, None]
['avgSpeed', 'sint64', False, None, None, None, None]
['medianMeasuredTime', 'sint64', False, None, None, None, None]
['vehicleCount', 'sint64', False, None, None, None, None]
['id', 'sint64', False, None, None, None, None]
"""
#SMDE 16/9/2016
#
#Will iterate through the 13.7m csv file and put into Riak in batches of 100
#SMDE 2/3/16

from riak import RiakClient
from datetime import datetime
import calendar
import csv
def changetime(stime):
            dt=datetime.strptime(stime,'%Y-%m-%dT%H:%M:%S')
            #print dt
            return calendar.timegm(datetime.timetuple(dt))*1000
            
c=RiakClient()
c.ping()


#to load data in the table

totalcount=0
batchcount=0
batchsize=100
ds=[]
t=c.table('aarhus')
print t


with open('./dataset-668-all.csv', 'rU') as infile:
    r=csv.reader(infile)
    for l in r:
		if l[0]!='status':
			newl=[str(l[3]),datetime.strptime(l[5],'%Y-%m-%dT%H:%M:%S'),int(l[1]),int(l[2]),int(l[4]),int(l[6]),int(l[7])]
			totalcount=totalcount+1
			#print count
			ds.append(newl)
			batchcount=batchcount+1
			if batchcount==batchsize:
				#add the records to the table
				print "Count at  ", totalcount
				to=t.new(ds)
				print "Created ts object"
				print "Storage result:  ",to.store()
				batchcount=0
				ds=[]       
infile.close()
print "Input file closed"
to=t.new(ds)
print "Storage result:  ",to.store()
print totalcount
