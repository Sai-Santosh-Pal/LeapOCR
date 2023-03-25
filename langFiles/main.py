import PIL.Image
import pytesseract as pt
import os
from tkinter import messagebox
custom_config = r'-l eng+hin+mal+ben+guj+kan+ori+pan+sat+tam+tel --psm 6'
pt.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def main(path):  
    try:    
        text = pt.image_to_string(path, config=custom_config) 
    except Exception as e:
        messagebox.showerror("Install Pytesseract", "Please install pytesseract properly. Please view this video for reference. The link is opened in your browser.")
        print(e)
        import webbrowser
        webbrowser.open("https://drive.google.com/u/0/uc?id=1STaN0yqHLAmjeemthxWpcCayh9JbWA_S&export=download&confirm=t&uuid=d884e58c-9ce9-478a-b614-8f07ac917e8e&at=ALgDtsyUE6fOddSd3a4v2HwSDXf7:1679410861717")
        print("https://drive.google.com/u/0/uc?id=1STaN0yqHLAmjeemthxWpcCayh9JbWA_S&export=download&confirm=t&uuid=d884e58c-9ce9-478a-b614-8f07ac917e8e&at=ALgDtsyUE6fOddSd3a4v2HwSDXf7:1679410861717")
        import cv2
        cap = cv2.VideoCapture(r"../resources/installation_video.mp4")
        ret, frame = cap.read()
        while(1):
            ret, frame = cap.read()
            font = cv2.FONT_HERSHEY_SIMPLEX

            cv2.putText(frame, 
                        'Press "q" to QUIT', 
                        (50, 50), 
                        font, 1, 
                        (0, 255, 255), 
                        2, 
                        cv2.LINE_4)
        
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
                cap.release()
                cv2.destroyAllWindows()
                break
            cv2.imshow('Installation',frame)
    
    imageName = path[0:-4]
    fullTempPath = imageName + ".txt"
    messagebox.showinfo("Success", "File saved at " + fullTempPath)
    file1 = open(fullTempPath, "w", encoding='utf-8') 
    file1.write(text) 
    file1.close()  
from tkinter import *
from tkinter import filedialog  
def browseFiles():
    from tkinter import filedialog as fd
    filename = fd.askopenfilename(title="Open Image", filetypes=(('PNG Files', "*.png"), ('JPG Files', "*.jpg")))

    main("" + filename + "")

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Project Udaan")
window.geometry("450x550")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 550,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    225.0,
    275.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=browseFiles,
    relief="flat"
)
button_1.place(
    x=63.0,
    y=224.0,
    width=294.0,
    height=44.0
)
window.resizable(False, False)
window.mainloop()
                                          
        