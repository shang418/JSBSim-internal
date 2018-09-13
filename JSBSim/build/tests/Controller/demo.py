from FlightGear import FlightGear
import time

def main():
    fg = FlightGear('localhost', 5500)

    # Wait five seconds for simulator to settle down
    while 1:
        if fg['/sim/time/elapsed-sec'] > 5:
            break
        time.sleep(1.0)
        print(fg['/sim/time/elapsed-sec'])



    heading = fg['/orientation/heading-deg']

    # Switch to external view for for 'walk around'.
    fg.view_next()

    fg['/sim/current-view/goal-heading-offset-deg'] = 180.0
    #fg.wait_for_prop_eq('/sim/current-view/heading-offset-deg', 180.0)

    fg['/sim/current-view/goal-heading-offset-deg'] = 90.0
    #fg.wait_for_prop_eq('/sim/current-view/heading-offset-deg', 90.0)

    fg['/sim/current-view/goal-heading-offset-deg'] = 0.0
    #fg.wait_for_prop_eq('/sim/current-view/heading-offset-deg', 0.0)

    time.sleep(2.0)

    # Switch back to cockpit view
    fg.view_prev()

    time.sleep(2.0)

    # Flaps to take off position
    fg['/controls/flaps'] = 0.34
    #fg.wait_for_prop_eq('/surface-positions/flap-pos-norm', 0.34)

    print(fg['/sim/position/altitude-agl-ft'])
    
    print('Initializing aircraft at desired Lat, Lon and Alt')
    fg['/sim/aircraft'] = 'Cessna 172P'
    fg['/position/longitude-deg'] =	'-70.9993'
    fg['/position/latitude-deg'] =	'42.3769'
    fg['/position/altitude-ft ']=	'2200'
    fg['/devices/status/keyboard/event/key ']=	'112'
    fg['/devices/status/keyboard/event/pressed ']=	'true'
    time.sleep(2.0)

    print('Aircraft Simulation initialized')
    print(fg['/sim/position/altitude-ft'])
    fg.quit()

if __name__ == '__main__':
    main()
