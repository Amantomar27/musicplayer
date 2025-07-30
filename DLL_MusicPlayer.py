
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os

# ------------------------
# Doubly Linked List Node
# ------------------------
class SongNode:
    def __init__(self, path):
        self.path = path
        self.title = os.path.basename(path)
        self.prev = None
        self.next = None

# ------------------------
# Music Player Class
# ------------------------
class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("🎵 Doubly Linked List Music Player")
        self.master.geometry("500x300")

        mixer.init()
        self.head = self.tail = self.current = None

        # UI Elements
        self.label = tk.Label(master, text="No song playing", font=("Arial", 16))
        self.label.pack(pady=20)

        btn_frame = tk.Frame(master)
        btn_frame.pack()

        tk.Button(btn_frame, text="⏮ Prev", command=self.play_previous).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="▶️ Play", command=self.play_current).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="⏭ Next", command=self.play_next).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="➕ Add Songs", command=self.add_songs).grid(row=1, column=0, columnspan=3, pady=10)

        self.playlist_box = tk.Listbox(master, width=50)
        self.playlist_box.pack()

    def add_songs(self):
        files = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        for path in files:
            self.add_song(path)

    def add_song(self, path):
        new_node = SongNode(path)
        if not self.head:
            self.head = self.tail = self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.playlist_box.insert(tk.END, new_node.title)

    def play_current(self):
        if self.current:
            mixer.music.load(self.current.path)
            mixer.music.play()
            self.label.config(text=f"Now Playing: {self.current.title}")
        else:
            self.label.config(text="No song selected")

    def play_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play_current()
        else:
            self.label.config(text="No next song")

    def play_previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.play_current()
        else:
            self.label.config(text="No previous song")

# ------------------------
# Run the GUI
# ------------------------
root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
