import youtube_dl
import pyfiglet
import os
import time
import colorama

colorama.init(autoreset=True)

X = colorama.Fore.YELLOW
Z = colorama.Fore.RED
F = colorama.Fore.GREEN
A = colorama.Fore.BLUE
C = colorama.Fore.MAGENTA
B = colorama.Fore.CYAN
Y = colorama.Fore.LIGHTBLUE_EX

# Function to clear the console screen
def clear_screen():
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to download a video with quality selection and specified output path
def download_video(url, output_path='/storage/emulated/0/Download', quality='best'):
    options = {
        'format': f'{quality}+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        # No need for 'ffmpeg_location' as imageio[ffmpeg] is installed
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            ydl.download([url])
            print(f"\n{F}Download completed successfully.{colorama.Style.RESET_ALL}")
        except youtube_dl.utils.DownloadError as e:
            print(f"\n{Z}An error occurred during download: {e}{colorama.Style.RESET_ALL}")

# Function to ask user for video URL, quality, and output path
def ask_user():
    while True:
        result = pyfiglet.figlet_format("PySites")
        colored_result = f"{B}{result}{colorama.Style.RESET_ALL}"
        print(colored_result)

        video_url = input("\nEnter the video URL: ")
        
        # Ask for quality
        print("\nSelect the video quality:")
        print("[1] Best Quality")
        print("[2] 720p")
        print("[3] 480p")
        print("[4] 360p")
        print("[5] 240p")
        print("[6] 144p")
        
        quality_choice = input("Enter the number corresponding to your choice (default is Best Quality): ")
        
        if quality_choice == '2':
            quality = '720p'
        elif quality_choice == '3':
            quality = '480p'
        elif quality_choice == '4':
            quality = '360p'
        elif quality_choice == '5':
            quality = '240p'
        elif quality_choice == '6':
            quality = '144p'
        else:
            quality = 'best'

        # Ask for output path
        output_path = input("\nEnter the output path to save the video (default is /storage/emulated/0/Download): ").strip()
        if not output_path:
            output_path = '/storage/emulated/0/Download'

        download_video(video_url, quality=quality, output_path=output_path)
        clear_screen()  # Clear the console after download

        choice = input("[1] Download Another Video\n[2] Exit\n")

        if choice == '2':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    # Ask the user for the next action
    ask_user()
    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            ydl.download([url])
            print(f"\n{F}Download completed successfully.{colorama.Style.RESET_ALL}")
        except youtube_dl.utils.DownloadError as e:
            print(f"\n{Z}An error occurred during download: {e}{colorama.Style.RESET_ALL}")

# Function to ask user for video URL, quality, and output path
def ask_user():
    while True:
        result = pyfiglet.figlet_format("PySites")
        colored_result = f"{B}{result}{colorama.Style.RESET_ALL}"
        print(colored_result)

        video_url = input("\nEnter the video URL: ")
        
        # Ask for quality
        print("\nSelect the video quality:")
        print("[1] Best Quality")
        print("[2] 720p")
        print("[3] 480p")
        print("[4] 360p")
        print("[5] 240p")
        print("[6] 144p")
        
        quality_choice = input("Enter the number corresponding to your choice (default is Best Quality): ")
        
        if quality_choice == '2':
            quality = '720p'
        elif quality_choice == '3':
            quality = '480p'
        elif quality_choice == '4':
            quality = '360p'
        elif quality_choice == '5':
            quality = '240p'
        elif quality_choice == '6':
            quality = '144p'
        else:
            quality = 'best'

        # Ask for output path
        output_path = input("\nEnter the output path to save the video (default is /storage/emulated/0/Download): ").strip()
        if not output_path:
            output_path = '/storage/emulated/0/Download'

        download_video(video_url, quality=quality, output_path=output_path)
        clear_screen()  # Clear the console after download

        choice = input("[1] Download Another Video\n[2] Exit\n")

        if choice == '2':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    # Ask the user for the next action
    ask_user()
