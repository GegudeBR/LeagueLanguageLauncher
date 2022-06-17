from os import path
from tkinter import *
import tkinter as tk
from tkinter import ttk
import Main, Language

Langs = {
    "Chinese": Language.Language.CHINESE_SIMPLIFIED,
    "Czech": Language.Language.CZECH_CZECH_REPUBLIC,
    "English (Australia)": Language.Language.ENGLISH_AUSTRALIA,
    "English (United Kingdom)": Language.Language.ENGLISH_UNITED_KINGDOM,
    "English (United States)": Language.Language.ENGLISH_UNITED_STATES,
    "French": Language.Language.FRENCH_FRANCE,
    "German": Language.Language.GERMAN_GERMANY,
    "Greek": Language.Language.GREEK_GREECE,
    "Hungarian": Language.Language.HUNGARIAN_HUNGARY,
    "Italian": Language.Language.ITALIAN_ITALY,
    "Japanese": Language.Language.JAPANESE_JAPAN,
    "Korean": Language.Language.KOREAN_KOREA,
    "Polish": Language.Language.POLISH_POLAND,
    "Portuguese (Brazil)": Language.Language.PORTUGUESE_BRAZIL,
    "Romanian": Language.Language.ROMANIAN_ROMANIA,
    "Russian": Language.Language.RUSSIAN_RUSSIA,
    "Spanish (Mexico)": Language.Language.SPANISH_MEXICO,
    "Spanish (Spain)": Language.Language.SPANISH_SPAIN,
    "Turkish": Language.Language.TURKISH_TURKEY

}
    

class App(tk.Frame):
  def __init__(self):
    self.root = Tk()  
    self.root.title("LoL Language Selector")
    self.root.iconbitmap(Main.resource_path(relative="icon.ico"))
    self.root.geometry("350x100")
    self.root.eval('tk::PlaceWindow . center')
    self.root.call()
    self.root.resizable(False, False)
    # Applying Themes
    self.root.tk.call("source", Main.resource_path("libs/forest-dark.tcl"))
    ttk.Style().theme_use('forest-dark')

    self.language_label = ttk.Label(self.root, text="Language: ")
    self.language_selector = ttk.Combobox(self.root,values=(), state="readonly")
    for l in Langs:
      self.language_selector['values'] = (*self.language_selector['values'], l)
    self.language_selector.set("English (United States)")

    self.launch_button = ttk.Button(self.root, text="Launch", command=self.start)


    #self.language_label.place(relx=0.1, rely=0.1, anchor=NW)
    self.language_selector.place(relx=0.5, rely=0.1, anchor=N)
    self.launch_button.place(relx=0.5, rely=0.6, anchor=CENTER)


    self.root.mainloop()

  def start(self):
    if not path.exists(Main.base_path):
      tk.messagebox.showerror("Error", "League of Legends not found. Please select the path to League of Legends.")
      Main.base_path = tk.filedialog.askdirectory(title="Select League of Legends path")

    Main.open_client(Langs[self.language_selector.get()])
    self.root.destroy()