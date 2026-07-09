# ================================
# Project  : Media Downloader
# Author   : Jayesh Chaudhari
# Date     : 28-05-2026
# Topic    : Audio Only Downloader
# ================================

import os

OUTPUT = "/mnt/d/Videos/%(title)s.%(ext)s"

print("=" * 45)
print("      YouTube Audio Downloader")
print("=" * 45)
print("Type URL to download or T to terminate")
print("=" * 45)

while True:
    url = input("\nEnter YouTube URL (or T to stop): ").strip()

    if url.upper() == "T":
        print("\nDownloader terminated. Bye Jayesh! 👋")
        break

    if url == "":
        print("No URL entered. Try again!")
        continue

    print(f"\nDownloading audio: {url}")
    cmd = f'yt-dlp -f "bestaudio" --extract-audio --audio-format mp3 -o "{OUTPUT}" "{url}"'
    os.system(cmd)
    print("\n✅ Done! Saved to D:\\Videos\\")