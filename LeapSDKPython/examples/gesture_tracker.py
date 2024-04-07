import leap
import time
import cv2

def camera():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("pic")  # name of pic

    pic_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed")
            break
        
        cv2.imshow("pic", frame)
        pic_name = "pic_{}.png".format(pic_counter)
        cv2.imwrite(pic_name,frame)
        pic_counter += 1
        break

    cam.release()

    cv2.destroyAllWindows()

    return pic_name

#Listens for if one of the user's thumb and index fingers are pinched together
class PinchListener(leap.Listener):
    def on_tracking_event(self, event):
        if event.tracking_frame_id % 5 == 0:
            activeHands = event.hands
            for hand in activeHands:
                print(hand.pinch_strength ==1)      #pinch_strength equals 1 if fingers are fully pinched
                camera()
                
#Listens for if the user has only index finger extended, not caring about the thumb
class IndexListener(leap.Listener):
    def on_tracking_event(self, event):
        if event.tracking_frame_id % 5 == 0:
            THUMB = 0
            INDEX = 1
            activeHands = event.hands
            for hand in activeHands:
                pointing = True                             # make a false value if
                for finger in hand.digits:                  # only one hand is pointing: defined by if
                    if finger.finger_id == INDEX:
                        pointing &= finger.is_extended      # index finger is extended and
                    elif finger.finger_id != THUMB:
                        pointing &= not finger.is_extended  # all others (except thumb) are not
                print(pointing)
                camera()

def main():
    my_listener = PinchListener()

    connection = leap.Connection()
    connection.add_listener(my_listener)

    my_listener = IndexListener()
    connection.add_listener(my_listener)

    with connection.open():
        while True:
            time.sleep(1)


if __name__ == "__main__":
    main()
