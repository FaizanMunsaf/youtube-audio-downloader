# import GUI
import random
import re
import tkinter as tk
from tkinter import messagebox
# import non-windows XP looking windows, looks nicer
import customtkinter
# import ability to access Youtube
from pytube import YouTube
import os

# from pytube.cipher

# re.compile(r"^\$*\w+\W")
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# ------------------------------- Public Path -----------------------------------------
PUBLIC_STORAGE_FOLDER = "storage"

if not os.path.exists(PUBLIC_STORAGE_FOLDER):
    os.makedirs(PUBLIC_STORAGE_FOLDER)  

# ----------------------------------- Download Now ----------------------------------------------------------------
def download():
    try:
        print()
        pytube_url = (url_entry.get()).strip()
        var_regex = re.compile(r"^\w+\W")

        # Create a YouTube object
        yt = YouTube(pytube_url)

        # Get the audio stream
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

        # Download the audio
        audio_stream.download(output_path='./storage', filename=f'audio.mp4')

        url_entry.delete(0, "end")
        print("Download Successfully!")  
    except Exception as e:
        print(f"Error {e}")  
    
#================================
# Main function
#================================
if __name__ == "__main__":
    try:
        
        # app = App()
        root = customtkinter.CTk()
        # configure window
        root.title("Betty's Downloader")
        root.geometry(f"{600}x{300}")

        # configure grid layout (4x4)
        root.grid_columnconfigure((0), weight=1)
        root.grid_rowconfigure((0,1,2,3), weight=1)

        # Add lable here
        main_lbl = customtkinter.CTkLabel(root, text="Let's Download the Youtube Video at Betty's Downloader")
        main_lbl.grid(row=0, column=0, padx=20,pady=(10,0), sticky="nwe")
        

        url_label = customtkinter.CTkLabel(root, text="Enter The Youtube URL")
        url_label.grid(row=1, column=0, sticky="w", padx=20,pady=(10,0))
        url_entry = customtkinter.CTkEntry(root, placeholder_text="Paste URL of video")
        url_entry.grid(row=2, column=0,sticky="ew", padx=20, pady=(0,10))

        download_btn = customtkinter.CTkButton(root,  text="Download" , command=download)
        download_btn.grid(row=3, column=0, sticky="ew", padx=20, pady=(0,10))

        root.mainloop()

    except Exception as e:
        print(f"Error : {e}")
