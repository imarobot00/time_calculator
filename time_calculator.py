def add_time(a, b):
    flag=0
    a=a.split()
    if(a[1]=='PM'):
        hrs=int(a[0][:a[0].find(":")])
        hrs=hrs+12
        mins=int(a[0][(a[0].find(":"))+1:])
    else:
         hrs=int(a[0][:a[0].find(":")])
         mins=int(a[0][(a[0].find(":"))+1:])
    hours=int(b[:b.find(":")])
    minutes=int(b[(b.find(":"))+1:])
    h=hrs+hours
    m=mins+minutes
    if m>=60:
        m=m-60
        h=h+1
    hour_next=h
    day = 0
    if h>=24:
        day = int(h/24)
        hour_next= int(h%24)
        if hour_next>=12:
            flag = 1
            hour_next=hour_next%12
        if flag==1:
            meridian="PM"
            hour_next=str(hour_next)
            m=str(m)
            if day>=1:
                if day>1:
                    print(hour_next+":"+m+" "+meridian+", "+str(day)+" days later")
                else:
                    print(hour_next+":"+m+" "+meridian+", "+" next day")    
        else:
            meridian="AM"
            hour_next=str(hour_next)
            m=str(m)
            if day>=1:
                if day>1:
                    print(hour_next+":"+m+" "+meridian+", "+str(day)+" days later")
                else:
                    print(hour_next+":"+m+" "+meridian+", "+" next day")    
    else:
        if(hour_next>=12):
            meridian="PM"
            hour_next=hour_next-12
            print(str(hour_next)+":"+str(m)+" "+meridian)
        else:
            print(str(hour_next)+":"+str(m)+" "+meridian)
               
add_time("10:10 PM", "3:30")
add_time("6:30 PM", "212:12")
add_time("3:00 PM", "3:10")
