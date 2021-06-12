#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import psutil
from time import sleep
import threading


def main():
    genislik = Pencere.winfo_screenwidth()
    yukseklik = Pencere.winfo_screenheight()
    px = 370  # pencere yüksekliği
    py = 250  # # pencere genişliği
    w = int((genislik / 2) - (px / 2))
    h = int((yukseklik / 2) - (py / 2))
    # penceremiz 370*550 boyutunda ve w ile h konumunda açılacak.
    ekran = "{}x{}+{}+{}".format(px, py, w, h)
    sayac = threading.Thread(target=degerler)
    sayac.start()
    Pencere.geometry(ekran)
    Pencere.mainloop()


def degerler():
    sleep(1)
    while 1:
        global STOP
        if STOP:
            break
        else:
            cpu_count = psutil.cpu_count()
            cpu_freqq = psutil.cpu_freq()
            load_avg = psutil.getloadavg()
            cpu_label2.config(text=cpu_freqq)
            load_label2.config(text=load_avg)
            count_label2.config(text=cpu_count)
            sleep(1)


def destroy_me():
    msg = messagebox.askyesno("Çıkış", "Çıkmak İstiyor musunuz?")
    # print(msg)  # msg true ise yes değilse no
    if msg:
        global STOP
        STOP = True
        Pencere.destroy()
        # .destroy pencereyi ve bekleyen işlemleri sonlandırıcak,
        # sonlandırmadan evvel bekleyen işlemlerin kapanmasını veya bitmesini beklemekte fayda var
    else:
        pass


# genel tanımlar pencere boyutu başlık vs.
Pencere = Tk()
Pencere.title("PyProc")
Pencere.resizable(False, False)
# Pencere kapatılırken, destroy_me adlı fonksiyonu çağır.
Pencere.protocol('WM_DELETE_WINDOW', destroy_me)

cpu_label = Label(Pencere, text="CPU Freq\t:")
cpu_label.place(x=10, y=10)

cpu_label2 = Label(Pencere, text="1")
cpu_label2.place(x=100, y=10)

load_label = Label(Pencere, text="Load Avg\t:")
load_label.place(x=10, y=30)

load_label2 = Label(Pencere, text="2")
load_label2.place(x=100, y=30)

count_label = Label(Pencere, text="Çekirdek\t:")
count_label.place(x=10, y=50)

count_label2 = Label(Pencere, text="3")
count_label2.place(x=100, y=50)

# çalışan kanalın işlemini sonlandırmak için kontrol edebileceğimiz global bir değişken
STOP = False

if __name__ == '__main__':
    main()
