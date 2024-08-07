import random as r
import time 
print('Welcome To Our Game Of Raja Mantri Chor Sipahi')
def countdown(t): 
	
	while t: 
		mins, secs = divmod(t, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		time.sleep(1) 
		t -= 1
	
	 

t = 2 
countdown(int(t)) 

def assign_roles(players):
    roles = ['RAJA', 'MANTRI', 'CHOR', 'SIPAHI']
    r.shuffle(roles)
    return dict(zip(players, roles))

def find_chor(mantri, players_roles):
    mantri_role = players_roles[mantri]
    if mantri_role != 'MANTRI':
        print(f'{mantri} is not the MANTRI')
        return False
    chor = input(f'{mantri}, who is the CHOR? ')
    if players_roles[chor] == 'CHOR':
        print('Right Answer')
        return True
    else:
        print('Wrong Answer')
        return False

p1 = input('Enter Player One Name: ')
p2 = input('Enter Player Two Name: ')
p3 = input('Enter Player Three Name: ')
p4 = input('Enter Player Four Name: ')

players = [p1, p2, p3, p4]

scores = {p1: 0, p2: 0, p3: 0, p4: 0}

play_again = 'y'

while play_again == 'y':
    roles = assign_roles(players)
    raja = [player for player, role in roles.items() if role == 'RAJA'][0]
    mantri = [player for player, role in roles.items() if role == 'MANTRI'][0]
    sipahi = [player for player, role in roles.items() if role == 'SIPAHI'][0]

    print(f'{raja} is RAJA')
    print('Who is the CHOR, MANTRI ji?')

    if find_chor(mantri, roles):
        scores[mantri] += 500
        scores[raja] += 100
        scores[sipahi] += 100
    else:
        chor = [player for player, role in roles.items() if role == 'CHOR'][0]
        scores[chor] += 500

    scores[raja] += 1000

    play_again = input('Do you want to play again? (y/n): ')

print(f'The total score of {p1} is {scores[p1]}')
print(f'The total score of {p2} is {scores[p2]}')
print(f'The total score of {p3} is {scores[p3]}')
print(f'The total score of {p4} is {scores[p4]}')
