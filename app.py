import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Set the path to the directory containing training images
dataset_path = 'C:\\Users\\Hp\\.vscode\\extensions\\face_recognition\\Training_images'
images = []
class_names = []

# List the contents of the directory
dataset_list = os.listdir(dataset_path)
print(dataset_list)

# Iterate through each file in the directory
for class_name in dataset_list:
    # Read each image and append it to the images list
    current_image = cv2.imread(f'{dataset_path}/{class_name}')
    images.append(current_image)
    
    # Append the class name (without file extension) to the class_names list
    class_names.append(os.path.splitext(class_name)[0])

# Print the list of class names
print(class_names)


# Function to find face encodings for a list of images
def find_encodings(images):
    encode_list = []

    for img in images:
        # Convert image to RGB format
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Find face encoding and append to the list
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)

    return encode_list


# Function to mark attendance in a CSV file
def mark_attendance(name):
    now = datetime.now()
    
    # Read existing content from the attendance CSV file
    with open('C:\\Users\\Hp\\.vscode\\extensions\\face_recognition\\Attendance.csv', 'r') as file:
        data_list = file.readlines()

    # Append a new entry with name, time, and date in separate columns
    with open('C:\\Users\\Hp\\.vscode\\extensions\\face_recognition\\Attendance.csv', 'a') as file:
        # Extract existing names from the file
        name_list = [entry.split(',')[0] for entry in data_list]
        
        # Check if the name is not already in the file
        if name not in name_list:
            # Write name, time, and date in separate columns
            file.writelines(f'\n{name},{now.strftime("%H:%M:%S")},{now.strftime("%d-%m-%Y")}')


# Find face encodings for the training images
encode_list_known = find_encodings(images)
print('Encoding Complete')

# Get the screen info for display of web cam
from screeninfo import get_monitors

# Get the primary monitor (assuming a single monitor setup)
primary_monitor = get_monitors()[0]

# Print the screen width and height
screen_width = primary_monitor.width
screen_height = primary_monitor.height

print(f"Screen Width: {screen_width}, Screen Height: {screen_height}")

# Open a connection to the default camera
video = cv2.VideoCapture(0)

# Create a named window
cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)

# Set window size to the screen resolution
cv2.resizeWindow('Webcam', screen_width, screen_height)

# Infinite loop to process frames from the camera
while True:
    # Read a frame from the camera
    success, img = video.read()
    
    # Resize the frame to 25% of its original size and convert to RGB format
    img_s = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img_s = cv2.cvtColor(img_s, cv2.COLOR_BGR2RGB)

    # Find face locations and encodings in the current frame
    faces_cur_frame = face_recognition.face_locations(img_s)
    encodes_cur_frame = face_recognition.face_encodings(img_s, faces_cur_frame)

    # Iterate through each face in the current frame
    for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
        # Compare face encodings with known face encodings
        matches = face_recognition.compare_faces(encode_list_known, encode_face)
        face_dis = face_recognition.face_distance(encode_list_known, encode_face)
        match_index = np.argmin(face_dis)

        # If a match is found, extract the class name, mark attendance, and draw a rectangle around the face
        if matches[match_index]:
            name = class_names[match_index].upper()
            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            
            # Call the function to mark attendance
            mark_attendance(name)

    # Display the processed frame
    cv2.imshow('Webcam', img)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
