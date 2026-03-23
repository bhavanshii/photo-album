import tkinter as tk
import time
from PIL import Image, ImageTk


#main application window code
root = tk.Tk()
root.title("Photo slideshow Album")
root.geometry("500x500")

#list of images paths 
image_paths = [
    r"C:\Users\User\Desktop\bhavanshi\animal_photo.jpg",
    
    r"C:\Users\User\Desktop\bhavanshi\images.jpg"
]
image_size=(400,400)
images=[]
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img)


#covert PIL images into tkinter compatible Image
final_images=[]
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)

#label widge to keep photuuu
image_label = tk.Label(root)
image_label.pack(pady=30) 


#slideshow function
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image= photo
        root.update()
        time.sleep(2)

#button 
play_button = tk.Button(
    root,
    text= "play the slideshow",
    command= start_slideshow
    )

play_button.pack(pady=40)
    
root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk

# root = tk.Tk()
# root.title("Photo slideshow Album")
# root.geometry("500x500")

# image_paths = [
#     r"C:\Users\User\Desktop\bhavanshi\animal_photo.jpg",
#     r"C:\Users\User\Desktop\bhavanshi\bhavanshi image.jpeg",
#     r"C:\Users\User\Desktop\bhavanshi\images.jpg"
# ]

# images = []
# for path in image_paths:
#     img = Image.open(path)
#     img = img.resize((400, 400))
#     images.append(ImageTk.PhotoImage(img))

# image_label = tk.Label(root)
# image_label.pack()

# index = 0

# def show_image():
#     global index
#     image_label.config(image=images[index])
#     index = (index + 1) % len(images)
#     root.after(2000, show_image)

# # 👇 auto start
# show_image()

# root.mainloop()






