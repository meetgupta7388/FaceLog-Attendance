# Face Recognition Attendance System

This project implements a face recognition-based attendance system using Python, OpenCV, and the face_recognition library.

## Features

- Real-time face detection and recognition using webcam
- Automatic attendance marking in a CSV file
- Support for multiple users
- Full-screen webcam display

## Requirements

- Python 3.x
- OpenCV
- face_recognition
- numpy
- screeninfo

For a complete list of dependencies, see `requirements.txt`.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/meetgupta7388/Face-Recognition-Attendance-System.git

2. Install the required packages:
    ```bash
    pip install -r requirements.txt

## Usage

1. Add training images to the `Training_images` directory. Each image should be named after the person it represents (e.g., "John_Doe.jpg").

2. Run the main script:
   ```bash
   python attend.py

   
3. The webcam will open in full-screen mode. Recognized faces will be highlighted with a green box and their names displayed.

4. Attendance will be automatically marked in `Attendance.csv`.

5. Press 'q' to quit the application.

## File Structure

- `attend.py`: Main application script
- `Attendance.csv`: CSV file for storing attendance records
- `Training_images/`: Directory for storing training images
- `requirements.txt`: List of required Python packages

## How it works

1. The script loads training images and encodes known faces.
2. It captures video from the webcam and processes each frame.
3. Faces in the frame are detected and compared with known faces.
4. If a match is found, the person's name is displayed and attendance is marked.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check this project if you want to contribute.


