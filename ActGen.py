import requests 

def create(start, stop, email, host, psw):

	for i in range(start, stop+1):

		data = {
			'email':(email + '+' + str(i) +'@'+host),
			'password':psw,
			'confirmpassword':psw,
			'gender':'Men',
			'source':'SSENSE_EN_SIGNUP'
		}

		r = requests.post('https://www.ssense.com/en-us/account/register', data=data)

		print (email + '+' + str(i) +'@'+host)


create(20, 35, '', '', '')