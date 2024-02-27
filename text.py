
"""
1.If Tesseract OCR is not installed on your system, you need to install it separately
2.pip install pillow
3.pip install pillow pytesseract
4.Upload high resolution images only in .jpg formate
"""
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

def convert_image_to_text(file_path):
    try:
        img = Image.open(file_path)

        img.thumbnail((400, 400))  
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo 

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)

        # Display the extracted text in the GUI
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, text)

    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e}")

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg")])
    if file_path:
        convert_image_to_text(file_path)


root = tk.Tk()
root.title("Image to Text Converter")


browse_button = tk.Button(root, text="Browse Image", command=browse_image)
result_text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
image_label = tk.Label(root)

browse_button.pack(pady=10)
image_label.pack(pady=10)
result_text.pack(padx=10, pady=10)

root.mainloop()
