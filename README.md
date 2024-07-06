# Face Recognition Attendance System

Welcome to the Face Recognition Attendance System! This project automates attendance tracking using face recognition technology. The system is developed in Python, leveraging OpenCV and face_recognition libraries.

## Features

- Real-time face recognition for attendance tracking.
- Training the system with a diverse dataset for accurate recognition.
- Automated logging of attendance data with timestamps.
- Compatibility with various environments and lighting conditions.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- face_recognition
- Other dependencies (Install using `pip install -r requirements.txt`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/meetgupta7388/face-recognition-attendance.git
   cd face-recognition-attendance
2. **Create a virtual environment (optional but recommended)**:

'''bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**:

'''bash
pip install -r requirements.txt

### Usage

1. **Prepare the dataset**:
   
- Create a folder named dataset in the project directory.
- Inside the dataset folder, create subfolders for each person with the person's name as the folder name.
- Add multiple images of each person in their respective subfolders.

2. **Train the model**:

'''bash
python train_model.py

3. **Run the attendance system**:

'''bash
python recognize.py

### How It Works

1. **Data Preparation**:

The system uses a dataset of images for training. Each person's images are stored in separate subfolders named after the person.
2. **Model Training**:

The training script processes the images and trains the face recognition model.

3. **Real-Time Recognition**:

The recognition script captures video from the webcam, detects faces, and matches them with the trained dataset to log attendance.

### Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements, bug fixes, or features.   
