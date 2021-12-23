from datetime import datetime
# Step 1 - Data 
a = {
0: {'Mosque' : 'North Austin Muslim Community Center', 'Time': '12:15'},
1: {'Mosque' : 'Islamic Center of Round Rock', 'Time':	'12:30'},
2: {'Mosque' : 'Islamic Center of Brushy Creek (ICBC)', 'Time': '12:30'},
3: {'Mosque' : 'Muslim Space(Virtual)', 'Time': '12:30'},
4: {'Mosque' : 'Islamic Center of Pflugerville', 'Time': '12:45'},
5: {'Mosque' : 'Masjid Ibrahim', 'Time': '13:00'},
6: {'Mosque' : 'Nueces Mosque', 'Time': '13:05'},
7: {'Mosque' : 'Islamic Center of Greater Austin', 'Time': '13:15'},
8: {'Mosque' : 'Islamic Center of Lake Travis', 'Time':	'13:30'},
9: {'Mosque' : 'North Austin Muslim Community Center', 'Time': '13:30'},
10: {'Mosque' : 'Islamic Center of Brushy Creek (ICBC)', 'Time': '13:30'},
11: {'Mosque' : 'Islamic Center of Round Rock', 'Time':	'13:40'},
12: {'Mosque' : 'Islamic Center of Pflugerville', 'Time': '13:45'},
13: {'Mosque' : 'Masjid Al-Noor', 'Time': '13:45'},
14: {'Mosque' : 'Nueces Mosque', 'Time': '14:05'},
15: {'Mosque' : 'Islamic Center of Greater Austin', 'Time': '14:15'},
16: {'Mosque' : 'North Austin Muslim Community Center', 'Time': '14:30'},
17: {'Mosque' : 'Islamic Center of Brushy Creek (ICBC)', 'Time': '14:30'},
18: {'Mosque' : 'Nueces Mosque', 'Time': '14:45'}
}

# Step 2
z = []

def get_values(d):
    for v in d.values():
        if isinstance(v, dict):
            yield from get_values(v)
        else:
            yield v

t = list(get_values(a))

# Step 3
for i in range(len(t)):
	if i % 2 != 0:
#		print(i, t[i])
		z.append(t[i])

# Step 4 
l = []

for row in range(len(z)):
    timestamp = datetime.strptime(z[row], '%H:%M')
#    print("timestamp", timestamp)
    l.append(timestamp)

#step 5
c = []
b = [] 
now = datetime.now()
current_time = now.strftime("%H:%M")
#c = ['13:56'] # Inserting static time for testing
c.append(current_time)
for row in range(len(c)):
    timestamp = datetime.strptime(c[row], '%H:%M')
#    print("timestamp", timestamp)
    b.append(timestamp)

#Step 6 - Running if statement for each entry. Running a for loop can replace this. 
def check_time2(x):
	if l[0] >= b[0]:
		print(t[0], " starts at ", l[0])	
	if l[1] >= b[0]:
		print(t[2], " starts at ", l[1])	
	if l[2] >= b[0]:
		print(t[4], " starts at ", l[2])		
	if l[3] >= b[0]:
		print(t[6], " starts at ", l[3])
	if l[4] >= b[0]:
		print(t[8], " starts at ", l[4])			
	if l[5] >= b[0]:
		print(t[10], " starts at ", l[5])			
	if l[6] >= b[0]:
		print(t[12], " starts at ", l[6])			
	if l[7] >= b[0]:
		print(t[14], " starts at ", l[7])			
	if l[8] >= b[0]:
		print(t[16], " starts at ", l[8])			
	if l[9] >= b[0]:
		print(t[18], " starts at ", l[9])			
	if l[10] >= b[0]:
		print(t[20], " starts at ", l[10])			
	if l[11] >= b[0]:
		print(t[22], " starts at ", l[11])					
	if l[12] >= b[0]:
		print(t[24], " starts at ", l[12])				
	if l[13] >= b[0]:
		print(t[26], " starts at ", l[13])					
	if l[14] >= b[0]:
		print(t[28], " starts at ", l[14])					
	if l[15] >= b[0]:
		print(t[30], " starts at ", l[15])					
	if l[16] >= b[0]:
		print(t[32], " starts at ", l[16])					
	if l[17] >= b[0]:
		print(t[34], " starts at ", l[17])					
	if l[18] >= b[0]:
		print(t[36], " starts at ", l[18])
check_time2(b)