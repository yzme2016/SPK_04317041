ax = [{"dari":"0", "ke":"1", "jarak": 13}, #0
   	  {"dari":"0", "ke":"2", "jarak": 4},  #1
      {"dari":"1", "ke":"3", "jarak": 6},	#2
	  {"dari":"1", "ke":"2", "jarak": 2},	#3
	  {"dari":"2", "ke":"4", "jarak": 1},	#4
	  {"dari":"3", "ke":"5", "jarak": 5},	#5
	  {"dari":"4", "ke":"3", "jarak": 5},	#6
	  {"dari":"4", "ke":"5", "jarak": 13}]	#7
#temp
xA = ""
result = ""
counter = 0
jaraktotal = 0
tempJTot = 0

for i in range(0,2):
	#jika tidak dimulai dari 0, maka keluar
	if ax[i]["dari"] == "0" :
		print "\n data ke-" , i

		for y in range (i,len(ax)):		
		#jika dari nilainya nol dan data pertama
			if ax[i]["dari"] == "0" and counter == 0:
#				print ax[i]["dari"] , " " , y
#				print "------------------"
				result= "{} --> {}".format(ax[i]["dari"],ax[i]["ke"])
				xA = ax[i]["ke"]
				counter += 1
#				print "** " , result ,"betul" , xA
				jaraktotal = ax[y]["jarak"]
			elif xA == ax[y]["dari"] and ax[y]["dari"] < ax[y]["ke"]:
				xA = ax[y]["ke"]
				result += " --> {}".format(ax[y]["ke"])
				jaraktotal += ax[y]["jarak"]
#				print "data XA " , xA
#				print "result nya " , result
				if xA=="5":
					print " Jalur yang dipilih = ", result , " \n Jarak total = " , jaraktotal ,"Kilometer"
					tempJTot = jaraktotal

	xA = ""
	counter = 0 
	if jaraktotal <= tempJTot:
		tempJTot = jaraktotal
	else :
		jaraktotal = 0

print "\n Jarak Terpendek adalah", tempJTot , "kilometer"
				