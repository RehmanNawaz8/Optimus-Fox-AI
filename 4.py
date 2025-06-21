import time
timestamp= time.strftime('%H,%M,%S')
print(timestamp)
rectime=int(time.strftime('%H'))
print(rectime)
if rectime>=6 and rectime <= 12:
    print("Good Morning Sir")
elif rectime >=12 and rectime <=18:
    print("Good Afternoon Sir")
else:   
    print("Good Night Sir")


