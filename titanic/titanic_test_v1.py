import csv as csv
import numpy as np

csv_file_object = csv.reader(open('csv/train.csv', 'rb'))
header = csv_file_object.next()

# put data from the csv reader into the data array
data = []
for row in csv_file_object:
	data.append(row)
data = np.array(data)

n_passengers =  np.size(data[0::,0].astype(np.float))
n_survived = np.sum(data[0::,0].astype(np.float))
proportion_survivors = n_survived / n_passengers

women_data = data[0::,3] == "female"
men_data = data[0::,3] != "female"

n_men_survive = np.sum(data[men_data,0].astype(np.float))\
	 / np.size(data[men_data,0].astype(np.float))
n_women_survive = np.sum(data[women_data,0].astype(np.float))\
	 / np.size(data[women_data,0].astype(np.float))
print 'Proportion of women who survive is %s' %n_women_survive
print 'Proportion of men who survive is %s' %n_men_survive

#determine way to bin groups as necessary


