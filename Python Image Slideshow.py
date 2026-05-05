import tkinter as tk
from PIL import ImageTk, Image
#===Window Create===
root=tk.Tk()
root.geometry("600x400")
root.title("Image Slideshow")
#===Images List===
images=[
     r"C:\Users\User\Pictures\Screenshots\Screenshot 2026-04-27 224904.png",
     r"C:\Users\User\Pictures\Screenshots\Screenshot 2026-02-08 213655.png",
     r"C:\Users\User\Pictures\Screenshots\Screenshot 2026-02-20 223358.png"
]
index=0
#===Label for image===
label=tk.Label(root)
label.pack(expand=True)
#===Function to show Image===
def show_image():
    global index
    img=Image.open(images[index])
    img=img.resize((600,400))
    img=ImageTk.PhotoImage(img)
    label.configure(image=img)
    label.image = img
def next_image():
    global index
    index=(index+1)%len(images)
    show_image()
def prev_image():
    global index
    index=(index-1)%len(images)
    show_image()

#===Button===
btn_next=tk.Button(root,text="Next",command=next_image)
btn_next.pack(side="right",padx=20)
btn_prev=tk.Button(root,text="Previous",command=prev_image)
btn_prev.pack(side="left",padx=20)
show_image()
root.mainloop()
