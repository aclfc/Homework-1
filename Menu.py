__author__ = 'Aidan'
Fname = ""
Lname = ""
dob = ""
ssn = ""
st = ""
City = ""
zc = ""
x=""

def formatnames(s):
    ns=""
    ns+=s[0].upper()
    for i in range(1,len(s)):
        ns+=s[i].lower()
    return ns
def firstname():
    global Fname
    n=input("Input the employee's first name: ")
    if n[0] == " ":
        n=n.replace(n[0],"")
    if n[len(n)-1] == " ":
        n=n.replace(n[len(n)-1],"")
    fn=formatnames(n)
    Fname = fn
    return fn
def lastname():
    global Lname
    n=input("Input the employee's last name: ")
    if n[0] == " ":
        n=n.replace(n[0],"")
    if n[len(n)-1] == " ":
        n=n.replace(n[len(n)-1],"")
    ln=formatnames(n)
    Lname = ln
    return ln
def DOB():
    global dob
    m = input("Input the employee's birth month (1-12): ")
    if m[0] == " ":
        m=m.replace(m[0],"")
    if m[len(m)-1] == " ":
        m=m.replace(m[len(m)-1],"")
    if int(m) not in range(12):
        m = input("That is not a valid month. Enter another (1-12): ")
        if m[0] == " ":
            m=m.replace(m[0],"")
        if m[len(m)-1] == " ":
            m=m.replace(m[len(m)-1],"")
    d=input("Input the employee's birth date (1-31): ")
    if int(d) == 31:
        if (m==4) or (m==6) or (m==9) or (m==11):
            d=input("That month only has 30 days. Enter a valid date: ")
        elif m == 2:
            d=input("That month only has 28 days. Enter a valid date: ")
    if d[0] == " ":
        d=d.replace(d[0],"")
    if d[len(d)-1] == " ":
        d=d.replace(d[len(d)-1],"")
    y = input("Input the employee's birth year (1900-present): ")
    if y[0] == " ":
        y=y.replace(y[0],"")
    if y[len(y)-1] == " ":
        y=y.replace(y[len(y)-1],"")
    if int(y) not in range(1900,2014):
        y=input("That is not a valid year, enter a different one(1900-present): ")
        if y[0] == " ":
            y=y.replace(y[0],"")
        if y[len(y)-1] == " ":
            y=y.replace(y[len(y)-1],"")
    dob = m+'/'+d+'/'+y
    return m+'/'+d+'/'+y
def SS():
    global ssn
    n1 = input("First 3 digits: ")
    if n1[0] == " ":
        n1=n1.replace(n1[0],"")
    if n1[len(n1)-1] == " ":
        n1=n1.replace(n1[len(n1)-1],"")
    n2 = input("Next 2 digits: ")
    if n2[0] == " ":
        n2=n2.replace(n2[0],"")
    if n2[len(n2)-1] == " ":
        n2=n2.replace(n2[len(n2)-1],"")
    n3 = input("Last 4 digits: ")
    if n3[0] == " ":
        n3=n3.replace(n3[0],"")
    if n3[len(n3)-1] == " ":
        n3=n3.replace(n3[len(n3)-1],"")
    ssn = n1+'-'+n2+'-'+n3
    return n1+'-'+n2+'-'+n3
def street():
    global st
    n=input("Input the employee's house/apt number: ")
    if n[0] == " ":
        n=n.replace(n[0],"")
    if n[len(n)-1] == " ":
        n=n.replace(n[len(n)-1],"")
    s=input("Input the employee's street name: ")
    if s[0] == " ":
        s=s.replace(s[0],"")
    if s[len(s)-1] == " ":
        s=s.replace(s[len(s)-1],"")
    st = n+" "+s
    return n+" "+s
def city():
    global City
    n=input("Input the employee's home town: ")
    if n[0] == " ":
        n=n.replace(n[0],"")
    if n[len(n)-1] == " ":
        n=n.replace(n[len(n)-1],"")
    City = n
    return n
def zip():
    global zc
    n=input("Input the employee's 5 digit zip code: ")
    if n[0] == " ":
        n=n.replace(n[0],"")
    if n[len(n)-1] == " ":
        n=n.replace(n[len(n)-1],"")
    if len(n) != 5:
        n=input("Wrong number of digits, input a valid zip code: ")
    zc = n
    return n

def printinfo():
    print("First Name:",Fname,"\nLast Name:",Lname,"\nDoB:",dob,"\nSSN:",ssn,"\nStreet Address:",st,"\nCity:",City,"\nZip Code:",zc)

def menu():
    x=input("Which would you like to input? Employee's:\n1.First Name\n2.Last Name\n3.DoB\n4.SS#\n5.Street Address\n6.City\n7.Zip\n8.Print Employee Info\n9.Quit\n")
    while x != '9':
        if x == '1':
            firstname()
        elif x == '2':
            lastname()
        elif x == '3':
            DOB()
        elif x == '4':
            SS()
        elif x == '5':
            street()
        elif x == '6':
            city()
        elif x == '7':
            zip()
        elif x == '8':
            printinfo()
        else:
            print("That is not an option.")
        x=input("Which would you like to input? Employee's:\n1.First Name\n2.Last Name\n3.DoB\n4.SS#\n5.Street Address\n6.City\n7.Zip\n8.Print Employee Info\n9.Quit\n")
    print("Goodbye!")

menu()