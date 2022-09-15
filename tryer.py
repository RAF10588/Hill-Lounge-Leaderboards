def check_file():
	elos1=open("elos1.py", "r")
	for line in elos1.readlines():
		if "full" in line:
			return "elos1.py"
	elos2=open("elos2.py", "r")
	for line in elos2.readlines():
		if "full" in line:
			return "elos2.py"
def other_file():
	if check_file()=="elos1.py":
		return "elos2.py"
	else:
		return "elos1.py"
def line_search(user,file):
	line_num = 0
	f = open(file, "r")
	for line in f.readlines():
		line_num+=1
		if user in line:
			return line_num
def rewrite(first, second):
	old_file=open(full_file, "r")
	new_file=open(empty_file, "a")
	content = old_file.readlines()
	for line in range(0, line_search(first,full_file)-1):
		new_file.write(content[line])
	new_file.write(first+"="+w_new_rating+"\n")
	for line in range(line_search(first,full_file), line_search(second,full_file)-1):
		new_file.write(content[line])
	new_file.write(second+"="+l_new_rating+"\n")
	for line in range(line_search(second,full_file)+1, len(content)):
		new_file.write(content[line])
	old_file.close()
	new_file.close()
	erase=open(full_file, "w")
	erase.close()

winner="strethewey"
loser="rdawson"
w_new_rating=str(505)
l_new_rating=str(1050)

full_file=check_file()
empty_file=other_file()

if line_search(winner,full_file)<line_search(loser,full_file):
	first=winner
	second=loser
else:
	first=loser
	second=winner
rewrite(first, second)

def get_exp_score_a(rating_a, rating_b):
    return 1.0 /(1 + 10**((rating_b - rating_a)/400.0))
def rating_adj(rating, exp_score, score, k=32):
    return rating + k * (score - exp_score)
class Player(object):
    def __init__(self, name, rating):
        self.rating = rating
        self.name = name
    def match(self, other, result):

        exp_score_a = get_exp_score_a(self.rating, other.rating)

        if result == self.name:
            self.rating = rating_adj(self.rating, exp_score_a, 1)
            other.rating = rating_adj(other.rating, 1 - exp_score_a, 0)
        elif result == other.name:
            self.rating = rating_adj(self.rating, exp_score_a, 0)
            other.rating = rating_adj(other.rating, 1 - exp_score_a, 1)
        elif result == 'Draw':
            self.rating = rating_adj(self.rating, exp_score_a, 0.5)
            other.rating = rating_adj(other.rating, 1 - exp_score_a, 0.5)

'''
"full"
rkoontz=1072
strethewey=1005
rdawson=1048
skanoy=1055
aparker=987
aelrod=985
syeh=973
krobinson=875
'''
'''
"full"
rkoontz=505
strethewey=505
rdawson=1050
aparker=987
aelrod=985
syeh=973
krobinson=1050
'''
