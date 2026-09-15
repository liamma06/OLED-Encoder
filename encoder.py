import pigpio
from encoder_decode import decode
from display import show_num
import time

CLK_PIN = 17
DT_PIN = 27
SW_PIN = 22

encoder = pigpio.pi()

encoder.set_mode(CLK_PIN, pigpio.INPUT)
encoder.set_mode(DT_PIN, pigpio.INPUT)
encoder.set_mode(SW_PIN, pigpio.INPUT)

#bounce avoid
encoder.set_glitch_filter(SW_PIN, 300)
encoder.set_pull_up_down(SW_PIN, pigpio.PUD_UP)



#rotate callback func (level-> change in val of pin, tick -> time of change)
prev_clk = 1
prev_dt = 1
current_value = 0

def on_pin_change(gpio, level, tick):
    global prev_clk, prev_dt, current_value

    clk = encoder.read(CLK_PIN)
    dt = encoder.read(DT_PIN)

    direction = decode(prev_clk, prev_dt, clk, dt)

    prev_clk = clk
    prev_dt = dt

    #increase in proper direction 
    if direction != 0:
        current_value += direction
        show_num(current_value)

encoder.callback(CLK_PIN, pigpio.EITHER_EDGE, on_pin_change)
encoder.callback(DT_PIN, pigpio.EITHER_EDGE, on_pin_change)



#button callback func
def on_button_press(gpio, level, tick):
    global current_value
    current_value = 0 #reset
    show_num(current_value)

encoder.callback(SW_PIN, pigpio.FALLING_EDGE, on_button_press)



#loop checking 
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    encoder.stop()
    print("exiting")
