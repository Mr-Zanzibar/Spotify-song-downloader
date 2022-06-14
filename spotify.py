import os

song = input("URl: ")
os.system(f"spotdl {song}")
os.remove(".spotdl-cache")
