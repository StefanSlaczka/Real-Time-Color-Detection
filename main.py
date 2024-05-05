import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error opening webcam")
    exit()

def get_dominant_color(frame):
    # Convert frame to HSV color space (better for color detection)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define ranges for red, green, and blue colors in HSV
    red_lower = np.array([170, 100, 100], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    green_lower = np.array([40, 50, 50], np.uint8)
    green_upper = np.array([80, 255, 255], np.uint8)
    blue_lower = np.array([100, 100, 100], np.uint8)
    blue_upper = np.array([140, 255, 255], np.uint8)

    # Create masks for each color
    mask_red = cv2.inRange(hsv, red_lower, red_upper)
    mask_green = cv2.inRange(hsv, green_lower, green_upper)
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

    # Count pixels in each mask
    red_count = cv2.countNonZero(mask_red)
    green_count = cv2.countNonZero(mask_green)
    blue_count = cv2.countNonZero(mask_blue)

    # Find dominant color
    dominant_color = "Black"  # Default

    if red_count > green_count and red_count > blue_count:
        dominant_color = "Red"
    elif green_count > red_count and green_count > blue_count:
        dominant_color = "Green"
    elif blue_count > red_count and blue_count > green_count:
        dominant_color = "Blue"

    return dominant_color

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Get dominant color
    dominant_color = get_dominant_color(frame)

    # Display the resulting frame with text
    cv2.putText(frame, "Dominant Color: " + dominant_color, (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Color Detection', frame)

    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture
cap.release()
cv2.destroyAllWindows()

