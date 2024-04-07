import leap
import time

#Listens for if the user's thumb and index fingers are pinched together
class PinchListener(leap.Listener):
    def on_tracking_event(self, event):
        if event.tracking_frame_id % 5 == 0:
            activeHands = event.hands
            for hand in activeHands:
                print(hand.pinch_strength ==1)

def main():
    my_listener = PinchListener()

    connection = leap.Connection()
    connection.add_listener(my_listener)

    with connection.open():
        while True:
            time.sleep(1)


if __name__ == "__main__":
    main()
