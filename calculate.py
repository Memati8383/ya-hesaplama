import tkinter as tk
from tkinter import messagebox
import time
from calendar import isleap

class AgeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")

        self.label_name = tk.Label(root, text="Adınızı Girin:")
        self.label_name.pack()

        self.entry_name = tk.Entry(root)
        self.entry_name.pack()

        self.label_birthdate = tk.Label(root, text="Doğum Tarihinizi Girin (GG.AA.YYYY):")
        self.label_birthdate.pack()

        self.entry_birthdate = tk.Entry(root)
        self.entry_birthdate.pack()

        self.calculate_button = tk.Button(root, text="Hesapla", command=self.calculate_age)
        self.calculate_button.pack()

    def calculate_age(self):
        name = self.entry_name.get()
        birthdate = self.entry_birthdate.get()
        birthdate_parts = birthdate.split('.')
        
        if len(birthdate_parts) != 3:
            messagebox.showerror("Hata", "Geçersiz tarih formatı. GG.AA.YYYY şeklinde girin.")
            return
        
        try:
            birth_day = int(birthdate_parts[0])
            birth_month = int(birthdate_parts[1])
            birth_year = int(birthdate_parts[2])
            
            current_time = time.localtime()
            current_day = current_time.tm_mday
            current_month = current_time.tm_mon
            current_year = current_time.tm_year
            
            years = current_year - birth_year
            months = current_month - birth_month
            days = current_day - birth_day
            
            if days < 0:
                months -= 1
                days += self.month_days(current_month - 1, current_year)
            
            if months < 0:
                years -= 1
                months += 12
            
            result = f"{name}, doğalı {years} yıl, {months} ay ve {days} gün olmuş."
            messagebox.showinfo("Sonuç", result)
            
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz tarih veya sayı formatı.")

    def month_days(self, month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2 and self.judge_leap_year(year):
            return 29
        else:
            return 28

    def judge_leap_year(self, year):
        if isleap(year):
            return True
        else:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculatorApp(root)
    root.mainloop()
