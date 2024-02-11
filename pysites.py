import youtube_dl
import pyfiglet
import os
import time
import colorama



X = '\033[1;33m'  # Yellow
Z = '\033[2;31m'  # Red, second shade
F = '\033[2;32m'  # Green
A = '\033[2;34m'  # Blue
C = '\033[2;35m'  # Pink
B = '\033[2;36m'  # Cyan
Y = '\033[1;34m'  # Light blue


# Function to clear the console screen
def clear_screen():
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to download a video
def download_video(url, output_path='.'):
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        # No need for 'ffmpeg_location' as imageio[ffmpeg] is installed
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            ydl.download([url])
            print("\nDownload completed successfully.")
        except youtube_dl.utils.DownloadError as e:
            print(f"\nAn error occurred during download: {e}")

# Function to ask user for the next action
def ask_user():
    while True:
        result = pyfiglet.figlet_format("PySites") 
        print(result)
        
        choice = input("[1] download Another Video\n[2] Exit\n")

        if choice == '1':
            video_url = input("\nEnter the video URL: ")
            download_video(video_url)
            clear_screen()  # Clear the console after download
        elif choice == '2':
            print("\nExiting the program. Goodbye!")
            break  # Fixed indentation and added break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    # Display the PySites ASCII art
    result = pyfiglet.figlet_format("PySites") 
    print(result)

    # Initial download
    video_url = input("\nEnter the video URL: ")
    download_video(video_url)
    clear_screen()  # Clear the console after the initial download

    # Ask the user for the next action
    ask_user()
