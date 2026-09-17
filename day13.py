a="Bilal??????"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("?"))
print(a.replace("Bilal","Haris"))
#Practies
print(a.rstrip("?").replace("Bilal","Haris"))#yhe haris ke age se bhi question mark hata de ga
#split
b="!!! Bilal !!!"
print(len(b.split(" ")))
#Capitalize Methode
c="my name is bilal"
print(c.capitalize())

#Center
d="Welcome to my python project"
print(d.center(60))

#Count
e="Bilal #$% BILAL %^&& BILAL"
print(e.count("BILAL"))

#True Yha Flase mai answer
f="BILAL @@"
print(f.endswith("@@"))

f1="Welcome to my console"
print(f1.endswith("m",4,10))

#Find Method
g="He's name is bilal"
print(g.find('is'))

#Isalnum
h="WelcomeToTheConsole"
print(h.isalnum())#Space na hu is ma is number bhi lik sak te hai
#Isalpha
h1="WEcomeToThConsol"
print(h1.isalpha())#is mai number nhi likho warna false aye ga srif string
#Islower
h2="hi bilal"
print(h2.islower())#yhe small mai hia ishiliyhe true aya hai
#isupper
h2="HI"
print(h2.isupper())#yhe CAPITAL hai is hilyhe true ayha hai
#isprintable
h2='My Name is Bilal2'
print(h2.isprintable())#Yhe sab string or number ko isprintable kahte haiishilyhe true show huga
#isspace
h2='      '
print(h2.isspace())#Is mai space hai haa hai space tu ture huga
#istitle
h2='Hellow Wolrd Nm'
print(h2.istitle())#yhe Isalnum is hi ki trar kamm karta hai
h2="Python"
print(h2.startswith("Python"))