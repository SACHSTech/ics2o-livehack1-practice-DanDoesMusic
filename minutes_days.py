minutes = float(input("number of minutes: "))
days = minutes // 1440
spare_minute = minutes % 1440
hours = spare_minute // 60 
extra_minutes = spare_minute % 60 
print ("the amount of days is: " + str(days) +"the amount of minutes is: " + str(extra_minutes) + "the ammount of hours is : " + str(hours))
