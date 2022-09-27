from firebase import firebase
firebase = firebase.FirebaseApplication("https://primeirotest-fb6c0.firebaseio.com/", None)

mensa = firebase.get('/msg','')
user = input('Usuario:')
for a in mensa:
	print(f'{a[0]}:{a[1]}')
	
um = []			
data = []

while True:
	men = input('\nMensagem:')
	if men == '0':
		novamen = firebase.get('/msg','')
		if len(novamen) > len(mensa):
			for v in novamen:
				if v in mensa:
					pass
				else:
					if v[0] != user:
						print(f'{v[0]}:{v[1]}')
					else:
						print('Sem novas mensagens....')
			mensa = novamen
		else:
			print('Sem novas mensagens....')
	else:
		data = [user, men]
		a = firebase.get('/msg','')
		a.append(data)
		data = []
		firebase.put('/msg', '/', a)
