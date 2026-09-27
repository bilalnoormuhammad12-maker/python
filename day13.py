# String are immutable
a="Bilal"
print(len(a))

#UPPER CASE
print(a.upper())

# Lower Case
print(a.lower())

# Replace karna
print(a.replace("Bilal","Noor"))

# rstrip (ju hata ta hai )!
b="Haris!!!"
print(b.rstrip("!"))
print(b.replace("Haris","m"))

#split (list ke tara kam karta hai) 
c="Bilal hhhhh nnnnn"
print(c.split())
c1="Bilal NoorMuhammad Haris NoorMuhammad "
print(c1.split())

# Capatalize (Start ka word capital hujahai ga, Baki sab ko lower mai kar dega)
d="hi myself bilal noor muhammad"
print(d.capitalize())
d1="my brother name is Haris"
print(d1.capitalize())

# Count (Jasie ke a variable mai bilal kitne dafa hai)
a1="Bilal Bilal BILAL"
print(a1.count("BILAL"))

# endswith (Yhe True Yha False Mai Jawab Dete Hai)
g="BILAL"
print(g.endswith("L"))
str1="Welcome to the console"
print(str1.endswith("o",6,10))
s="My name is Bilal"
print(s.endswith("e",5,7))

# Find(jo list mai huga uska index bata dega or nhi huga tu -1 show kar dega)
st="He's name is Dan. he is an honest main."
print(st.find("He"))
# Index(find ketara hai yhe -1 nhi deta error deta hai)
print(st.index("is"))

# Isalnum(1.is mai gap nhi huga[2.ismai number bhi dal sakte hai] [3.small bhi husakta hai])
print(' [Isalnum]')
sg="WelcomeToTheConsole"
print(sg.isalnum())

sg="welcometotheconsole"
t=sg
print(t.isalnum())

t1="123456789010"
print(t.isalnum())

# isalpha([1.is mai gap nhi huga] [2.ismai number nhi dal sakte hai] [3.small bhi husakta hai])
print("  [ISALPHA]     ")
f="Welcomesir"
print(f.isalpha())

F1="WE123"
print(F1.isalpha())

# islower([lower hai tu true yha false])
print("  [Lower] ")
f2="my name is bilal"
print(f2.islower())

# isprinttable(ju hu pirnttable hugi tu true hu )\n yhe printable nhi hai
print('  [Printtable]')
f3="MY Name Is Bilal"
print(f3.isprintable())

# isspaces (kiya variable mai space hai tu true warna false)
print( '  [Space] ')
f4=" "
print(f4.isspace())

# istitle ([Is mai start ka word capital huna chahi])
print( " {Istitle}")
f5="My Name Is Bilal"
print(f5.istitle())

# startswith ([Matlab ke start kis word se hura hi hai])
print({'Startswith'})
f6="My Father Nmae is Noor Muhammad"
print(f6.startswith("My"))

# SwapCase ({Ju Sab Ko lower ko Capitals Kar ta hai or upper ko lower})
f7=" What is Your Name"
print(f7.swapcase())

# Title([Yhe star ke word ko Capital kar ta hai])
f8="my faviourate color is bule"
print(f8.title())
