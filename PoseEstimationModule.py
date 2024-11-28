class Pose_Estimation:
    def __init__(self,video):
        self.video=video
    def draw(self):
        import mediapipe as mp
        import cv2
        import time
        video= cv2.VideoCapture(self.video)
        pTime = 0
        mpPose = mp.solutions.pose
        pose = mpPose.Pose()
        mpDraw = mp.solutions.drawing_utils
        while True:
            ret, frame = video.read()
            if not ret:
                break
            frame=cv2.flip(frame,1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame)
            # drawing key points and landmarks
            if results.pose_landmarks:
                mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    h, w, c = frame.shape
                    print(id, lm)
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(frame, (cx, cy), 3, (255, 0,), cv2.FILLED)

            frame = cv2.resize(frame, (800, 600))
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2)

            cv2.imshow("frame", frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()
x1=Pose_Estimation(1)
x1.draw()