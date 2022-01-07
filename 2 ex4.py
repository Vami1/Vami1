
import pandas as pd
df1 = pd.DataFrame ( data =
 { 'yr1': { 'qtr1':4500, 'qtr2': 5700}, 
   'yr2' :{ 'qtr1':7800, 'qtr2':9800}} index = ['Rno.1', 'Rno.2','Rno.3' ])
print (df1)
for (col, colSeries) in df1.iteritems():
	print ("Column index:" , col )
	print ("contaning:")
	print  (colSeries)
	