# ================================
# Project  : Media Downloader - Fix Remaining 6 Files
# Author   : Jayesh Chaudhari
# Date     : 16-06-2026
# Topic    : Fix 1 MP4 (no audio) + 5 WEBM (no audio → convert to MP4)
# ================================

import yt_dlp
import subprocess
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

VIDEO_DIR  = "/mnt/d/Videos/SQL Ultimate Course"
TEMP_AUDIO = "/tmp/yt_audio_temp"

FIXES = [
    {
        "file"  : "04 - Install SQL Server & SSMS 2026 ｜ Create Your First Database (Beginner Guide) ｜ #SQL Course 3.webm",
        "yt_id" : "Cr58jAj_YAc",
        "action": "webm_to_mp4",
    },
    {
        "file"  : "14 - SQL String Functions (Visually Explained) ｜ A Detailed Guide ｜ #SQL Course 13.webm",
        "yt_id" : "NOTWx5s-s1o",
        "action": "webm_to_mp4",
    },
    {
        "file"  : "17 - SQL Date & Time Functions (Visually Explained) ｜ FORMAT, CONVERT, CAST ｜ #SQL Course 16.webm",
        "yt_id" : "U7WMMzxvwT4",
        "action": "webm_to_mp4",
    },
    {
        "file"  : "35 - SQL Columnstore Index (Visually Explained) ｜ Columnstore vs Rowstore ｜ #SQL Course 36.webm",
        "yt_id" : "k9DpO91W76o",
        "action": "webm_to_mp4",
    },
    {
        "file"  : "50 - Design Data Architecture for Your Data Warehouse ｜ Data Engineer Portfolio Project ｜ #SQL Project 5.mp4",
        "yt_id" : "shUMovyA1cs",
        "action": "add_audio",
    },
    {
        "file"  : "54 - Building The Gold Layer： Star Schema Modeling ｜ Data Engineer Portfolio Project ｜ #SQL Project 9.webm",
        "yt_id" : "9bxTdAwuStI",
        "action": "webm_to_mp4",
    },
]


def download_audio(yt_id):
    # clean up any leftover temp files first
    for ext in ["m4a", "aac", "opus", "webm", "mp4"]:
        p = f"{TEMP_AUDIO}.{ext}"
        if os.path.exists(p):
            os.remove(p)

    url = f"https://www.youtube.com/watch?v={yt_id}"
    ydl_opts = {
        "format"         : "bestaudio",
        "outtmpl"        : TEMP_AUDIO + ".%(ext)s",
        "quiet"          : True,
        "no_warnings"    : True,
        "postprocessors" : [{
            "key"             : "FFmpegExtractAudio",
            "preferredcodec"  : "m4a",
            "preferredquality": "192",
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for ext in ["m4a", "aac", "opus", "webm", "mp4"]:
        path = f"{TEMP_AUDIO}.{ext}"
        if os.path.exists(path):
            return path
    return None


def merge_to_mp4(video_path, audio_path, output_path):
    result = subprocess.run([
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",     # copy video — no re-encoding, no quality loss
        "-c:a", "aac",      # encode audio to AAC
        "-map", "0:v:0",
        "-map", "1:a:0",
        output_path
    ], capture_output=True, text=True)
    return result.returncode == 0, result.stderr


# ── Main ──────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold yellow]🔧  Fix Remaining 6 Files[/]",
    subtitle="[dim]by Jayesh Chaudhari[/]",
    border_style="cyan"
))

fixed = 0
failed = 0

for i, item in enumerate(FIXES, 1):
    filename   = item["file"]
    yt_id      = item["yt_id"]
    action     = item["action"]
    video_path = os.path.join(VIDEO_DIR, filename)

    console.print(f"\n[bold white][{i}/6][/] {filename[:70]}")
    console.print(f"  [dim]Action : {'WEBM → MP4 + audio' if action == 'webm_to_mp4' else 'Add audio to MP4'}[/]")

    if not os.path.exists(video_path):
        console.print(f"  [red]❌ File not found on disk — skipping[/]")
        failed += 1
        continue

    # output is always MP4
    mp4_path    = os.path.join(VIDEO_DIR, os.path.splitext(filename)[0] + ".mp4")
    temp_output = mp4_path.replace(".mp4", "_FIXED.mp4")

    console.print(f"  [magenta]⬇  Downloading audio (yt_id: {yt_id})...[/]", end=" ")
    try:
        audio_path = download_audio(yt_id)
        if not audio_path or not os.path.exists(audio_path):
            raise Exception("Audio file not found after download")
        console.print("[green]done[/]")
    except Exception as e:
        console.print(f"[red]FAILED — {e}[/]")
        failed += 1
        continue

    console.print(f"  [yellow]🔀 Merging + converting to MP4...[/]", end=" ")
    ok, err = merge_to_mp4(video_path, audio_path, temp_output)

    if ok:
        os.replace(temp_output, mp4_path)
        if action == "webm_to_mp4" and os.path.exists(video_path):
            os.remove(video_path)           # delete original WEBM
        if os.path.exists(audio_path):
            os.remove(audio_path)
        console.print("[green]done ✅[/]")
        if action == "webm_to_mp4":
            console.print(f"  [dim]WEBM deleted → saved as MP4[/]")
        fixed += 1
    else:
        console.print(f"[red]FAILED[/]")
        console.print(f"  [dim red]{err[-300:]}[/]")
        if os.path.exists(temp_output):
            os.remove(temp_output)
        if os.path.exists(audio_path):
            os.remove(audio_path)
        failed += 1

console.print(f"""
[bold green]═══════════════════════════════[/]
[bold]  DONE![/]
[bold green]═══════════════════════════════[/]
  ✅ Fixed  : {fixed} / 6
  ❌ Failed : {failed} / 6
""")
