#Execute the following in the python terminal one after the other
import sumo

#Execute the below if sumo is struck or cannot take any arguments/commands
cnt = sumo.SumoController('MyCtrl')

cnt.connect()

#Speed ranges from 0-100 and till -100 for reverse
cnt.move(10)

#for turns first arg is speed and second is the turn speed
cnt.move(10,45)

#jump from 0-1 (decimal format)
cnt.jump(0.5)

#posture from 0-2 (decimal/int format)
cnt.posture(0.5)

