#!/usr/bin/env python3

# Copyright (C) 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os

lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"

if not os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nThis module is shutting down...")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

def module_exit():
    exit("\nThis module is shutting down...\nModül kapatılıyor...")

bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile("/usr/local/bin/metterxp/settings/theme/0.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#03035B"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/1.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/2.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/3.txt"):
    bg="#808080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#808080"
    a_button_bg="#808080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/4.txt"):
    bg="#FF0000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FF0000"
    a_button_bg="#FF0000"
    a_button_fg="#FFFFFF"     
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/5.txt"):
    bg="#FFA500"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FFA500"
    a_button_bg="#FFA500"
    a_button_fg="#FFFFFF" 
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/6.txt"):
    bg="#008000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#008000"
    a_button_bg="#008000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/7.txt"):
    bg="#0000FF"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#0000FF"
    a_button_bg="#0000FF"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/8.txt"):
    bg="#000080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000080"
    a_button_bg="#000080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/9.txt"):
    bg="#800080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#800080"
    a_button_bg="#800080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/10.txt"):
    bg="#FFC0CB"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFC0CB"
    a_button_bg="#FFC0CB"
    a_button_fg="#000000"
else:
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#03035B"
    a_button_fg="#FFFFFF"
def cr_dir():
    if os.path.isdir("/usr/local/bin/metterxp/settings"):
        pass
    else:
        os.system("cd /usr/local/bin/metterxp/ ; mkdir settings")
    if os.path.isdir("/usr/local/bin/metterxp/settings/theme"):
        pass
    else:
        os.system("cd /usr/local/bin/metterxp/settings ; mkdir theme")
if os.path.isdir("/usr/local/bin/metterxp/settings/theme"):
    pass
else:
    cr_dir()

def main():
    def mxp_uninstall():
        window.destroy()
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_uninstall.py")
        exit()
    def mxp_update():
        window.destroy()
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_update.py")
        exit()

    def preview():
        if os.path.isfile(lang_en):
            messagebox.showinfo("Information","I am definitely the best information window. :)")
        elif os.path.isfile(lang_tr):
            messagebox.showinfo("Bilgilendirme","Ben kesinlikle en iyi bilgi penceresiyim. :)")

    def theme0():
        def theme0_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 0.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Bilgilendirme","Theme applied! When you are click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("MetterXP Classic preview | MetterXP ")
            window2.config(background="#000000")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#000000", foreground="#FFFFFF", text="I'm here to preview.")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#000000", activebackground="#03035B", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Click!", command=preview)
            space01=Label(window2, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#000000", activebackground="#03035B", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Apply MetterXP classic theme", command=theme0_set)
        elif os.path.isfile(lang_tr):
            window2=Tk()
            window2.title("MetterXP Klasik önizleme | MetterXP ")
            window2.config(background="#000000")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#000000", foreground="#FFFFFF", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#000000", activebackground="#03035B", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#000000", activebackground="#03035B", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="metterxp Klasik temasını uygula", command=theme0_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()
    def theme1():
        def theme1_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 1.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Theme applied! When you click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("Black theme preview | MetterXP ")
            window2.config(background="#000000")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#000000", foreground="#FFFFFF", text="I'm here to preview.")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#000000", activebackground="#000000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Click!", command=preview)
            space01=Label(window2, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#000000", activebackground="#000000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Apply black theme", command=theme1_set)
        elif os.path.osfile(lang_tr):
            window2=Tk()
            window2.title("Siyah tema önizleme | MetterXP ")
            window2.config(background="#000000")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#000000", foreground="#FFFFFF", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#000000", activebackground="#000000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#000000", activebackground="#000000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Siyah temayı uygula", command=theme1_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()    
    def theme2():
        def theme2_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 2.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Theme applied! When you click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("White theme preview | MetterXP ")
            window2.config(background="#FFFFFF")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#FFFFFF", foreground="#000000", text="I'm here to preview!")
            preview_buton=Button(window2, background="#000000", foreground="#FFFFFF", activebackground="#FFFFFF", activeforeground="#000000", font="arial 10", cursor="hand2", borderwidth="3", text="Click", command=preview)
            space01=Label(window2, background="#FFFFFF", foreground="#000000", font="arial 3", text="\n")
            button01=Button(window2, background="#000000", foreground="#FFFFFF", activebackground="#FFFFFF", activeforeground="#000000", font="arial 10", cursor="hand2", borderwidth="3", text="Apply white theme", command=theme2_set)
        if os.path.isfile(lang_tr):
            window2=Tk()
            window2.title("Beyaz tema önizleme | MetterXP ")
            window2.config(background="#FFFFFF")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#FFFFFF", foreground="#000000", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#000000", foreground="#FFFFFF", activebackground="#FFFFFF", activeforeground="#000000", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#FFFFFF", foreground="#000000", font="arial 3", text="\n")
            button01=Button(window2, background="#000000", foreground="#FFFFFF", activebackground="#FFFFFF", activeforeground="#000000", font="arial 10", cursor="hand2", borderwidth="3", text="Beyaz temayı uygula", command=theme2_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()
    def theme3():
        def theme3_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 3.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Theme applied! When you click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("Grey theme preview | MetterXP")
            window2.config(background="#808080")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#808080", foreground="#FFFFFF", text="I'm here to preview.")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#808080", activebackground="#808080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Click!", command=preview)
            space01=Label(window2, background="#808080", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#808080", activebackground="#808080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Apply grey theme", command=theme3_set)
        elif os.path.isfile(lang_tr):
            window2=Tk()
            window2.title("Gri tema önizleme | MetterXP")
            window2.config(background="#808080")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#808080", foreground="#FFFFFF", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#808080", activebackground="#808080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#808080", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#808080", activebackground="#808080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Gri temayı uygula", command=theme3_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()
    def theme4():
        def theme4_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 4.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Theme applied! When you click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("Red theme preview | MetterXP ")
            window2.config(background="#FF0000")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#FF0000", foreground="#FFFFFF", text="I'm here to preview.")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#FF0000", activebackground="#FF0000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Click!", command=preview)
            space01=Label(window2, background="#FF0000", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#FF0000", activebackground="#FF0000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Apply red theme", command=theme4_set)
        elif os.path.isfile(lang_tr):
            window2=Tk()
            window2.title("Kırmızı tema önizleme | MetterXP ")
            window2.config(background="#FF0000")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#FF0000", foreground="#FFFFFF", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#FF0000", activebackground="#FF0000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#FF0000", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#FF0000", activebackground="#FF0000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Kırmızı temayı uygula", command=theme4_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()
    def theme5():
        def theme5_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 5.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Theme applied! When you click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("Orange theme preview | MetterXP ")
            window2.config(background="#FFA500")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#FFA500", foreground="#FFFFFF", text="I'm here to preview.")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#FFA500", activebackground="#FFA500", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Click!", command=preview)
            space01=Label(window2, background="#FFA500", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#FFA500", activebackground="#FFA500", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Apply orange theme", command=theme5_set)
        elif os.path.isfile(lang_tr):
            window2=Tk()
            window2.title("Turuncu tema önizleme | MetterXP ")
            window2.config(background="#FFA500")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#FFA500", foreground="#FFFFFF", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#FFA500", activebackground="#FFA500", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#FFA500", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#FFA500", activebackground="#FFA500", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Turuncu temayı uygula", command=theme5_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()
    def theme6():
        def theme6_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 6.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Theme applied! When you click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("Green theme preview | MetterXP ")
            window2.config(background="#008000")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#008000", foreground="#FFFFFF", text="I'm here to preview.")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#008000", activebackground="#008000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Click!", command=preview)
            space01=Label(window2, background="#008000", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#008000", activebackground="#008000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Apply green theme", command=theme6_set)
        elif os.path.isfile(lang_tr):
            window2=Tk()
            window2.title("Yeşil tema önizleme | MetterXP ")
            window2.config(background="#008000")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#008000", foreground="#FFFFFF", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#008000", activebackground="#008000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#008000", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#008000", activebackground="#008000", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Yeşil temayı uygula", command=theme6_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()
    def theme7():
        def theme7_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 7.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Theme applied! When you click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("Blue theme preview | MetterXP ")
            window2.config(background="#0000FF")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#0000FF", foreground="#FFFFFF", text="I'm here to preview.")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#0000FF", activebackground="#0000FF", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Click!", command=preview)
            space01=Label(window2, background="#0000FF", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#0000FF", activebackground="#0000FF", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Apply blue theme", command=theme7_set)
        elif os.path.isfile(lang_tr):
            window2=Tk()
            window2.title("Mavi tema önizleme | MetterXP ")
            window2.config(background="#0000FF")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#0000FF", foreground="#FFFFFF", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#0000FF", activebackground="#0000FF", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#0000FF", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#0000FF", activebackground="#0000FF", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Mavi temayı uygula", command=theme7_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()
    def theme8():
        def theme8_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 8.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Theme applied! When you click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("Navy blue theme preview | MetterXP ")
            window2.config(background="#000080")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#000080", foreground="#FFFFFF", text="I'm here to preview.")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#000080", activebackground="#000080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Click!", command=preview)
            space01=Label(window2, background="#000080", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#000080", activebackground="#000080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Apply navy blue theme", command=theme8_set)
        elif os.path.isfile(lang_tr):
            window2=Tk()
            window2.title("Lacivert tema önizleme | MetterXP ")
            window2.config(background="#000080")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#000080", foreground="#FFFFFF", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#000080", activebackground="#000080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#000080", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#000080", activebackground="#000080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Lacivert temayı uygula", command=theme8_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()
    def theme9():
        def theme9_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 9.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Theme applied! When you click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfle(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("Purple theme preview | MetterXP ")
            window2.config(background="#800080")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#800080", foreground="#FFFFFF", text="I'm here to preview!")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#800080", activebackground="#800080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Click", command=preview)
            space01=Label(window2, background="#800080", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#800080", activebackground="#800080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Apply purple theme", command=theme9_set)
        elif os.path.isfile(lang_tr):
            window2=Tk()
            window2.title("Mor tema önizleme | MetterXP ")
            window2.config(background="#800080")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#800080", foreground="#FFFFFF", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#FFFFFF", foreground="#800080", activebackground="#800080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#800080", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#FFFFFF", foreground="#800080", activebackground="#800080", activeforeground="#FFFFFF", font="arial 10", cursor="hand2", borderwidth="3", text="Mor temayı uygula", command=theme9_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()
    def theme10():
        def theme10_set():
            window2.destroy()
            os.system("cd /usr/local/bin/metterxp/settings/theme ; rm * ; touch 10.txt")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Theme applied! When you click 'OK', MetterXP will be closed to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İstenilen tema uygulandı! 'OK' tuşuna bastığınızda MetterXP değişikliklerin uygulanması için kapatılacak.")
            window.destroy()        
            module_exit()
        if os.path.isfile(lang_en):
            window2=Tk()
            window2.title("Pink theme preview | MetterXP ")
            window2.config(background="#FFC0CB")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#FFC0CB", foreground="#000000", text="I'm here to preview")
            preview_buton=Button(window2, background="#000000", foreground="#FFC0CB", activebackground="#FFC0CB", activeforeground="#000000", font="arial 10", cursor="hand2", borderwidth="3", text="Click!", command=preview)
            space01=Label(window2, background="#FFC0CB", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#000000", foreground="#FFC0CB", activebackground="#FFC0CB", activeforeground="#000000", font="arial 10", cursor="hand2", borderwidth="3", text="Apply pink theme", command=theme10_set)
        elif os.path.isfile(lang_tr):
            window2=Tk()
            window2.title("Pembe tema önizleme | MetterXP ")
            window2.config(background="#FFC0CB")
            window2.resizable(0, 0)
            preview_text=Label(window2, background="#FFC0CB", foreground="#000000", text="Ben önizlenmek için buradayım!")
            preview_buton=Button(window2, background="#000000", foreground="#FFC0CB", activebackground="#FFC0CB", activeforeground="#000000", font="arial 10", cursor="hand2", borderwidth="3", text="Bana tıkla!", command=preview)
            space01=Label(window2, background="#FFC0CB", foreground="#FFFFFF", font="arial 3", text="\n")
            button01=Button(window2, background="#000000", foreground="#FFC0CB", activebackground="#FFC0CB", activeforeground="#000000", font="arial 10", cursor="hand2", borderwidth="3", text="Pembe temayı uygula", command=theme10_set)
        preview_text.pack()
        preview_buton.pack()
        space01.pack()
        button01.pack()
    def langtr():
        print("Seçilen dil ayarlanıyor...")
        os.system("cd /usr/local/bin/metterxp/settings/lang ; rm * ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","İstenilen dil uygulandı! 'OK' tuşuna bastığınızda MetterXP kapatılacak.")
        window.destroy()
        module_exit()
    def langen():
        print("Setting choosed language...")
        os.system("cd /usr/local/bin/metterxp/settings/lang ; rm * ; touch en.txt")
        messagebox.showinfo("Information","English language applied. When you click 'OK', MetterXP will be close.")
        module_exit()
    if os.path.isfile(lang_en):
        window=Tk()
        window.title("MetterXP options | MetterXP")
        window.config(background=bg)
        window.resizable(0, 0)
        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Please select the theme you want to action on.")
        space1=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        button1=Button(window, text="MetterXP Classic (default)", command=theme0, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button2=Button(window, text="Black", command=theme1, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button3=Button(window, text="White", command=theme2, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button4=Button(window, text="Grey", command=theme3, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button5=Button(window, text="Red", command=theme4, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button6=Button(window, text="Orange", command=theme5, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button7=Button(window, text="Green", command=theme6, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button8=Button(window, text="Blue", command=theme7, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button9=Button(window, text="Navy blue", command=theme8, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
        button10=Button(window, text="Purple", command=theme9, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
        button11=Button(window, text="Pink", command=theme10, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
        space2=Label(window, background=bg, foreground=fg, font="arial 3", text="\n\n")
        text2=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="You can change your language preferences below.")
        space3=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        button12=Button(window, text="Türkçe (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button13=Button(window, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        space4=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        button14=Button(window, text="Update MetterXP", command=mxp_update, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button15=Button(window, text="Uninstall MetterXP", command=mxp_uninstall, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font =",arial 10", cursor="hand2", borderwidth="3")
        space5=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        module_exit_buton=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="Close this module\nand exit",command=module_exit)
    elif os.path.isfile(lang_tr):
        window=Tk()
        window.title("MetterXP seçenekleri | MetterXP")
        window.config(background=bg)
        window.resizable(0, 0)
        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen üzerinde işlem yapmak istediğiniz temayı seçin.")
        space1=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        button1=Button(window, text="MetterXP Klasik (varsayılan)", command=theme0, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button2=Button(window, text="Siyah", command=theme1, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button3=Button(window, text="Beyaz", command=theme2, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button4=Button(window, text="Gri", command=theme3, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button5=Button(window, text="Kırmızı", command=theme4, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button6=Button(window, text="Turuncu", command=theme5, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button7=Button(window, text="Yeşil", command=theme6, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button8=Button(window, text="Mavi", command=theme7, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button9=Button(window, text="Lacivert", command=theme8, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
        button10=Button(window, text="Mor", command=theme9, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
        button11=Button(window, text="Pembe", command=theme10, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
        space2=Label(window, background=bg, foreground=fg, font="arial 3", text="\n\n")
        text2=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Aşağıdan dil tercihlerinizi değiştirebilirsiniz.")
        space3=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        button12=Button(window, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button13=Button(window, text="Türkçe (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        space4=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        button14=Button(window, text="MetterXP'ı güncelle", command=mxp_update, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")        
        button15=Button(window, text="MetterXP'i kaldır", command=mxp_uninstall, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")        
        space5=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        module_exit_buton=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="Çık ve\nmodülü kapat",command=module_exit)
    text1.pack()
    space1.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()
    button9.pack()
    button10.pack()
    button11.pack()
    space2.pack()
    text2.pack()
    space3.pack()
    button12.pack()
    button13.pack()
    space4.pack()
    button14.pack()
    button15.pack()
    space5.pack()
    module_exit_buton.pack()        
    mainloop()
def langset():
    os.system("cd /usr/local/bin/metterxp/settings ; mkdir lang theme")
    def langen():
        print("Setting choosed language...")
        os.system("cd /usr/local/bin/metterxp/settings/lang ; rm * ; touch en.txt")
        messagebox.showinfo("Information","English language applied! When you click 'OK', MetterXP settings will open.")
        lwindow.destroy()
        main()
    def langtr():
        print("Seçilen dil ayarlanıyor...")
        os.system("cd /usr/local/bin/metterxp/settings/lang ; rm * ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","İstenilen dil uygulandı! 'OK' tuşuna bastığınızda MetterXP ayarları açılacak.")
        lwindow.destroy()
        main()
    lwindow=Tk()
    lwindow.title("Choose a language for MetterXP")
    lwindow.config(background=bg)
    lwindow.resizable(0, 0)
    text1=Label(lwindow, background=bg, foreground=fg, font="arial 10 bold", text="Please choose a language.\nLütfen bir dil seçin.")
    text1.pack()
    space1=Label(lwindow, background=bg, foreground=fg, font="arial 3", text="\n")
    space1.pack()
    button1=Button(lwindow, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
    button1.pack()
    button2=Button(lwindow, text="Türkçe (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    button2.pack()
    mainloop()
if os.path.isdir("/usr/local/bin/metterxp/settings/lang/"):
    main()
else:
    langset()