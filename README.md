# 📸 Photo Slideshow App

## 📌 Project Description

This is a simple **Photo Slideshow Application** built using **Python Tkinter**.
The application displays images in a slideshow format with a fixed time interval.

It provides a basic graphical user interface (GUI) where users can click a button to start viewing images one by one.

---

## 🚀 Features

* 🖼️ Display multiple images in slideshow
* ⏱️ Automatic image transition (every 2 seconds)
* 🧩 Simple and user-friendly GUI
* 🐍 Built using Python and Tkinter
* 📁 Supports local image files

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* Pillow (PIL - Python Imaging Library)

---

## 📂 Project Structure

```
photo-album/
│
├── photoalbum.py        # Main Python file
├── animal_photo.jpg     # Image 1
├── images.jpg           # Image 2
├── README.md            # Project documentation
```

---

## ▶️ How to Run the Project

### Step 1: Install Python (if not installed)

Download from: https://www.python.org/

### Step 2: Install Required Library

Open terminal and run:

```
pip install pillow
```

### Step 3: Run the Project

```
python photoalbum.py
```

---

## ⚠️ Important Note

Make sure all image files are in the same folder as the Python file and use relative paths like:

```
"animal_photo.jpg"
```

instead of absolute paths.

---

## 📸 How It Works

* Images are loaded using Pillow
* Converted into Tkinter-compatible format
* Displayed using Label widget
* Slideshow runs using a loop with time delay

---

## 🎯 Future Improvements

* Add Next/Previous buttons
* Add Pause/Resume feature
* Select folder dynamically
* Add image transition effects
* Add full-screen slideshow mode

---

## 👩‍💻 Author

**Bhavanshi Choyal**

---

## ⭐ Acknowledgment

This project is created for learning Python GUI development and improving programming skills.
