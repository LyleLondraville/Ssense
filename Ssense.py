## Ssense scraper developed by @SoleWingSneaks
## if you do not want to outwite to a textfile then simply put in '' for the file paramiter and the program will not outwrite

import requests, json, time, smtplib
from threading import Thread 


def message(email, emailPass, toEmail, toPhone, text):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email, emailPass)
	 
	server.sendmail(email, toEmail, text)
	server.sendmail(email, toPhone, text)
	server.quit()

def scrape(start, stop) :

	while start <= stop:
		try :
			h = requests.get('https://www.ssense.com/en-us/editorial/queryProduct/%s' % start)
			if h.status_code == 200 :
				JSONdict = json.loads(h.text)
				item = str(start) + '\n' + json.dumps(JSONdict['name']) + '\n' + json.dumps(JSONdict['price']) + '\n' + ('https://www.ssense.com/en-us/men/product/%s/%s/%s' % ((((json.dumps(JSONdict['brandName'])).replace(' ','-').replace('"', ''))), ((((json.dumps(JSONdict['name'])).replace('\u0027', '')).replace(' ','-')).replace('"', '')), start)) 
				message('', "", '', '', item)
				print item 
			
			else :
				print start
			
			start += 1

		except :
			print 'Error, sleaping for 200 seconds'
			time.sleep(200)


def cook():

	t1 = Thread(target = scrape, args = (2059347, 2063412, 'Ssense1.txt'))
	t2 = Thread(target = scrape, args = (2063412, 2067477, 'Ssense2.txt'))
	t3 = Thread(target = scrape, args = (2067477, 2071542, 'Ssense3.txt'))
	t4 = Thread(target = scrape, args = (2071542, 2075607, 'Ssense4.txt'))
	t5 = Thread(target = scrape, args = (2075607, 2079672, 'Ssense5.txt'))
	t6 = Thread(target = scrape, args = (2079672, 2083737, 'Ssense6.txt'))
	t7 = Thread(target = scrape, args = (2083737, 2087802, 'Ssense7.txt'))
	t8 = Thread(target = scrape, args = (2087802, 2091867, 'Ssense8.txt'))

	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()
	t7.start()
	t8.start()

t = time.time()
scrape(1803304, 1803403)
print time.time() - t



























