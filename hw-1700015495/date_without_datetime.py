#date
dtstr=input('Enter the datetime:(20170228):')
datekey={1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
datekeyr={1:0,2:31,3:60,4:91,5:121,6:152,7:182,8:213,9:244,10:274,11:305,12:335}
year=int(dtstr[:4])
month=int(dtstr[4:6])
day=int(dtstr[6:])
if year%4==0:
    if year%100==0 and year%400!=0:
        count=datekey[month]+day
    else:
        count=datekeyr[month]+day
else:
    count=datekey[month]+day
print(count)