import cv2
import numpy as np

capture = cv2.VideoCapture('soccer.mp4')
fps = capture.get(cv2.CAP_PROP_FPS)

# 抓整部影片的最後一幀
frame_index_end = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1
frame_index_start = capture.get(cv2.CAP_PROP_POS_FRAMES)

# 演算法壓縮
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
output = cv2.VideoWriter('score_resverse.mp4', fourcc, int(fps), (360, 240), True)

while capture.isOpened() and frame_index_start<=frame_index_end:

    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index_start)

    ret, frame = capture.read()

    if ret is True:
        frame = cv2.resize(frame, (360, 240))
        # Decrement the index to read next frame:
        frame_index_start +=3
        text = f"StartIndex:{str(frame_index_start)}"
        cv2.putText(frame,text,(20,30),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2)

        cv2.imshow('Original frame', frame)
        output.write(frame)
        # Press q on keyboard to exit the program:
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break
# 影片倒轉
while capture.isOpened() and frame_index_end >= 0:
    # 設定一下起始位置
    # cv2.CAP_PROP_POS_FRAMES：從0開始索引幀，幀位置。
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index_end)

    ret, frame = capture.read()

    if ret is True:

        frame = cv2.resize(frame, (360, 240))
        # Decrement the index to read next frame:
        frame_index_end -= 3
        text = f"ReverseIndex:{str(frame_index_end)}"
        cv2.putText(frame,text,(20,30),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)

        cv2.imshow('reverse frame', frame)
        output.write(frame)
        # Press q on keyboard to exit the program:
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

capture.release()
cv2.destroyAllWindows()