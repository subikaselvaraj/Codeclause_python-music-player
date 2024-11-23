import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize pygame mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")
        self.root.config(bg="Black")
        
        # Current playing file
        self.current_file = None
        
        # UI Components
        self.title_label = tk.Label(self.root, text="No file selected", wraplength=300, justify="center")
        self.title_label.pack(pady=20)
        
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music, state=tk.DISABLED)
        self.play_button.pack(pady=10)
        
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music, state=tk.DISABLED)
        self.pause_button.pack(pady=10)
        
        self.resume_button = tk.Button(self.root, text="Resume", command=self.resume_music, state=tk.DISABLED)
        self.resume_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        
        self.load_button = tk.Button(self.root, text="Load Music", command=self.load_music)
        self.load_button.pack(pady=20)
    
    def load_music(self):
        # Open file dialog to select a music file
        file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
        if file:
            self.current_file = file
            self.title_label.config(text=f"Loaded: {file.split('/')[-1]}")
            self.play_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.NORMAL)
            self.resume_button.config(state=tk.NORMAL)
    
    def play_music(self):
        if self.current_file:
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()
    
    def pause_music(self):
        pygame.mixer.music.pause()
    
    def resume_music(self):
        pygame.mixer.music.unpause()
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_file = None
        self.title_label.config(text="No file selected")
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
player = MusicPlayer(root)
root.mainloop()
