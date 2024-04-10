from tkinter import *
import speedtest

def speed_test():
    sp=speedtest.Speedtest()
    sp.get_best_server()

    download=str(round(sp.download()/(10**6),3))+"Mbps"
    upload=str(round(sp.upload()/(10**6),3))+"Mbps"
    download_label.config(text=download)
    upload_label.config(text=upload)
    
sp=Tk()
sp.title=("Internet Speed Tets")
sp.geometry("500x550")
sp.config(bg="Cyan")

label = Label(sp,text="Internet Speed Test",font=("Times New Roman",30,"bold"),bg="Cyan",fg="Red")
label.place(x=70,y=40)

label=Label(sp,text="Download Speed",font=("Times New Roman",20,"bold"))
label.place(x=70,y=110,height=50,width=360)

download_label=Label(sp,text="00",font=("Times New Roman",20,"bold"))
download_label.place(x=70,y=180,height=50,width=360)

label=Label(sp,text="Upload Speed",font=("Times New Roman",20,"bold"))
label.place(x=70,y=250,height=50,width=360)

upload_label=Label(sp,text="00",font=("Times New Roman",20,"bold"))
upload_label.place(x=70,y=320,height=50,width=360)

button=Button(sp,text="Test",font=("Times New Roman",20,"bold"),relief="raised",fg="Red",command=speed_test)
button.place(x=70,y=420,height=50,width=360)



sp.mainloop()