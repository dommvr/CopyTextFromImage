from pynput.mouse import Listener as MouseListener
from PIL import ImageGrab, ImageTk
from pytesseract import pytesseract
import pyperclip
import tkinter as tk

root = tk.Tk()

start_x = None
start_y = None

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract

def get_curr_screen_geometry():
    f_root = tk.Tk()
    f_root.update_idletasks()
    f_root.attributes('-fullscreen', True)
    f_root.state('iconic')
    geometry = f_root.winfo_geometry()
    f_root.destroy()
    return geometry

def on_click(x, y, button, pressed):
    global start_x, start_y
    if button.name == 'left':
        if pressed:
            start_x = x
            start_y = y
        else:
            canvas.create_rectangle(start_x, start_y, x, y, outline='red', width=3)
            canvas.pack()
            try:
                img = ImageGrab.grab(bbox=(start_x, start_y, x, y))
                text = pytesseract.image_to_string(img)
                pyperclip.copy(text)
            except:
                pass
            root.quit()

    if not pressed:
        return False

root.geometry(get_curr_screen_geometry())
root.configure(bg='')
root.attributes('-fullscreen', True)
root.attributes('-topmost',True)

canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.config(cursor='cross')
c_img = ImageGrab.grab(bbox=None)
c_img = ImageTk.PhotoImage(c_img)
canvas.create_image(root.winfo_screenwidth()/2, root.winfo_screenheight()/2, image=c_img)
canvas.pack()

if __name__ == '__main__':
    with MouseListener(on_click=on_click) as listener:
        root.mainloop()
        listener.join()