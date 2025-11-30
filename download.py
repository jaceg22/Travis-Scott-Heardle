import os
import subprocess

SONG_FILE = "songs.txt"
OUTPUT_FOLDER = "new-songs"

def download_soundcloud(url, output_folder):
    print(f"[SC] Downloading: {url}")
    command = [
        "scdl",
        "-l", url,
        "--onlymp3",
        "--path", output_folder
    ]
    subprocess.run(command)
    print("[SC] Done.\n")

def download_youtube(url, output_folder):
    print(f"[YT] Downloading: {url}")
    command = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "-o", f"{output_folder}/%(title)s.%(ext)s",
        url
    ]
    subprocess.run(command)
    print("[YT] Done.\n")

def process_urls():
    if not os.path.exists(SONG_FILE):
        print("❌ songs.txt not found.")
        return

    # Create output folder if missing
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Read URLs from songs.txt
    with open(SONG_FILE, "r") as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]

    print(f"Found {len(urls)} URL(s). Starting downloads...\n")

    for url in urls:
        if "soundcloud.com" in url:
            download_soundcloud(url, OUTPUT_FOLDER)
        elif "youtube.com" in url or "youtu.be" in url:
            download_youtube(url, OUTPUT_FOLDER)
        else:
            print(f"❌ Unsupported URL: {url}\n")

    print("🎵 All downloads complete!")

if __name__ == "__main__":
    process_urls()
