import sqlite3
import numpy as np
import json
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

database = '/home/amrita95/Desktop/Cap8_DS_Challenge_V1/sqlite.db'

db = sqlite3.connect(database)
cursor = db.cursor()

#fetching depth,ts data from Table Exec
cursor.execute('''SELECT depth,ts FROM exec''')
data = cursor.fetchall()
array= np.array(data)
depth = []
ts = []
for column in array:
    depth.append(column[0])
    ts.append(column[1])
ts = np.reshape(ts,[2503,-1])
depth = np.reshape(depth,[2503,-1])

#fetching rates from Table Exec
cursor.execute('''SELECT rates FROM exec''')
data = cursor.fetchall()
array = np.array(data)
rate1 =[]
rate5 =[]
for column in array:
    rate1.append(json.loads(column[0])['1'])
    rate5.append(json.loads(column[0])['5'])

#Plots and Histograms of the data
#plt.figure(num=1,figsize=(30,30))
plt.suptitle('Container exec metrics')
gridspec.GridSpec(3,4)

plt.subplot2grid((3,4), (0,0), colspan=3, rowspan=1)
plt.plot(ts,depth,'ro',markersize = 2)
plt.ylabel('exec_depth')

plt.subplot2grid((3,4), (0,3))
plt.hist(depth,bins ='auto')

plt.subplot2grid((3,4), (1,0), colspan=3, rowspan=1)
plt.plot(ts,rate1,'ro',markersize = 2)
plt.ylabel('exec_rate1s')

plt.subplot2grid((3,4), (1,3))
plt.hist(rate1,bins= 'auto')

plt.subplot2grid((3,4), (2,0), colspan=3, rowspan=1)
plt.plot(ts,rate5,'ro',markersize = 2)
plt.ylabel('exec_rate2s')

plt.subplot2grid((3,4), (2,3))
plt.hist(rate5,bins='auto')


#fetching rx,tx,dur,ts data from Table tcpfile
cursor.execute('''SELECT rx,tx,dur,ts FROM tcplife''')
data2 = cursor.fetchall()
array2= np.array(data2)
rx = []
tx =[]
dur = []
ts2 = []
for column in array2:
    rx.append(column[0])
    tx.append(column[1])
    dur.append(column[2])
    ts2.append(column[3])
ts2 = np.reshape(ts2,[944,-1])
rx = np.reshape(rx,[944,-1])
tx = np.reshape(tx,[944,-1])
#dur = np.reshape(dur,[944,-1])

#fetching lport,rport from Table tcpfile
cursor.execute('''SELECT lport,rport FROM tcplife''')
data2 = cursor.fetchall()
array2 = np.array(data2)
lport = []
rport = []
for column in array2:
    lport.append(json.loads(column[0]))
    rport.append(json.loads(column[1]))

lport = np.reshape(lport,[944,-1])
rport = np.reshape(rport,[944,-1])

#plt.figure(num=2,figsize=(30,30))
plt.suptitle('Tcpfile entries')
gridspec.GridSpec(5,4)

plt.subplot2grid((5,4), (0,0), colspan=3, rowspan=1)
plt.plot(ts2,tx,'ro',markersize = 2)
plt.ylabel('tx')

plt.subplot2grid((5,4), (0,3))
plt.hist(tx,bins = 20)

plt.subplot2grid((5,4), (1,0), colspan=3, rowspan=1)
plt.plot(ts2,rx,'ro',markersize = 2)
plt.ylabel('rx')

plt.subplot2grid((5,4), (1,3))
plt.hist(rx,bins= 'auto')

plt.subplot2grid((5,4), (2,0), colspan=3, rowspan=1)
plt.plot(ts2,dur,markersize = 2)
plt.ylabel('dur')

plt.subplot2grid((5,4), (2,3))
plt.hist(dur,bins='auto')

plt.subplot2grid((5,4), (3,0), colspan=3, rowspan=1)
plt.plot(ts2,lport,'ro',markersize = 2)
plt.ylabel('lport')

plt.subplot2grid((5,4), (3,3))
plt.hist(lport,bins='auto')

plt.subplot2grid((5,4), (4,0), colspan=3, rowspan=1)
plt.plot(ts2,rport,'ro',markersize = 2)
plt.ylabel('rport')

plt.subplot2grid((5,4), (4,3))
plt.hist(rport,bins=10)

plt.show()
