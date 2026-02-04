import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound
import time

class Pomodoro:
    def __init__(self, root):
        self.root=root

    def work_break(self, timer):

        minutes, seconds=divmod(timer, 60)
        self.min.set(f"{minutes:02d}")
        self.sec.set(f"{seconds:02d}")
        self.root.update()
        time.sleep(1)
    
    def work(self):
        timer=25*60
        while timer>=0:
            self.work_break(timer)
            if timer==0:
                playsound("sound.mp3")
                messagebox.showinfo(
                    "Good job!", "Take a break, \
                    nClick break button")
                
            timer-=1

    def break_(self):
        timer=5*60
        while timer>=0:
            pomo.work_break(timer)
            if timer==0:
                playsound("sound.mp3")
                messagebox.showinfo(
                    "Times up!", "Get back to work, \
                        nClick Work Button")
            timer-=1

    def main(self):
        self.root.geometry("450x455")
        self.root.resizable(False, False)
        self.root.title("Pomidoro Timer")

        #label
        #frame for the timer labels
        time_frame=tk.Frame(self.root, bg="#e9edc9")
        time_frame.pack(pady=10)

        self.min=tk.StringVar(self.root)
        self.min.set("25")
        self.sec=tk.StringVar(self.root)
        self.sec.set("00")
        #minutes label
        self.min_label=tk.Label(time_frame, 
                                textvariable=self.min,
font=(

            "arial", 22, "bold"), bg="#918450", fg="#fefae0")
        self.min_label.pack(side="left")

        self.sec_label=tk.Label(time_frame,
                                textvariable=self.sec,
font=(
            "arial", 22, "bold"), bg="#918450", fg="#fefae0")
        self.sec_label.pack(side="left")

        canvas = tk.Canvas(self.root, bg="#e9edc9")
        canvas.pack(expand=True, fill="both")
        img=Image.open("pomidor.png")
        img = img.resize((850, 700), Image.LANCZOS)
        bg=ImageTk.PhotoImage(img)
        canvas.create_image(225, 20, image=bg, anchor="center")

        btn_work=tk.Button(self.root, text="Start",
                           bd=5, command=self.work, bg="#918450", fg="#fefae0", font=(
                               "arial", 15, "bold")).place(x=140, y=380)
        btn_break=tk.Button(self.root, text="Break",
                            bd=5, fg="#fefae0", command=self.break_, 
                            bg="#918450", font=(
                                "arial", 15, "bold")).place(x=240, y=380)
        self.root.mainloop()

if __name__=="__main__":
    pomo=Pomodoro(tk.Tk())
    pomo.main()                            
                           

                
    