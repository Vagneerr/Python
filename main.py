from djitellopy import Tello
import time

tello=Tello()
tello.connect()
print(tello.get_battery())
tello.set_mission_pad_detection_direction(2)
pad = 0
tello.get_mission_pad_id()
tello.takeoff()
while pad != 5:
    pad = tello.get_mission_pad_id()
    tello.move_forward(20)
    time.sleep(1)
print(tello.get_mission_pad_id())
tello.go_xyz_speed_mid(0,0,20,30,5)

tello.land()
tello.end()