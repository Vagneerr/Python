from djitellopy import Tello
##Code dohavelog
tello=Tello()
tello.connect()

tello.takeoff()
tello.move_forward(20)
tello.land()
tello.end()