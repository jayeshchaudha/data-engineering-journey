# ================================
# Project  : Media Downloader - Audio Fix
# Author   : Jayesh Chaudhari
# Date     : 16-06-2026
# Topic    : Fix missing audio in downloaded MP4 files
#            Downloads audio-only and merges with existing video
# ================================

import yt_dlp
import subprocess
import os
import re
from rich.console import Console
from rich.panel import Panel

console = Console()

PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLNcg_FV9n7qZY_2eAtUzEUulNjTJREhQe"
VIDEO_DIR    = "/mnt/d/Videos/SQL Ultimate Course"
TEMP_AUDIO   = "/tmp/yt_audio_temp"


# ── check if file already has audio ──────────────────────────────────────────
def has_audio(filepath):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_streams", "-select_streams", "a",
         "-of", "default=noprint_wrappers=1", filepath],
        capture_output=True, text=True
    )
    return bool(result.stdout.strip())


# ── clean title for fuzzy matching ────────────────────────────────────────────
def clean_title(title):
    title = title.lower()
    title = re.sub(r'[｜|#\-\(\)\[\],.\'\":!?：]', ' ', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title


# ── match playlist title to local filename ────────────────────────────────────
def find_matching_file(yt_title, local_files):
    yt_clean   = clean_title(yt_title)
    best_match = None
    best_score = 0

    for filename in local_files:
        name = os.path.splitext(filename)[0]
        if ' - ' in name:
            name = name.split(' - ', 1)[1]
        file_clean = clean_title(name)

        yt_words   = set(yt_clean.split())
        file_words = set(file_clean.split())
        common     = yt_words & file_words
        score      = len(common) / max(len(yt_words), 1)

        if score > best_score:
            best_score = score
            best_match = filename

    return best_match if best_score > 0.5 else None


# ── download audio only ───────────────────────────────────────────────────────
def download_audio(url):
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


# ── merge audio into existing video ──────────────────────────────────────────
def merge_audio(video_path, audio_path, output_path):
    result = subprocess.run([
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-map", "0:v:0",
        "-map", "1:a:0",
        output_path
    ], capture_output=True, text=True)
    return result.returncode == 0


# ── Main ──────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold yellow]🔧  Audio Fix Tool — SQL Ultimate Course[/]",
    subtitle="[dim]by Jayesh Chaudhari[/]",
    border_style="cyan"
))

local_files = [f for f in os.listdir(VIDEO_DIR) if f.endswith(".mp4")]
console.print(f"[dim]Found {len(local_files)} MP4 files in folder[/]\n")

console.print("[cyan]Fetching playlist info from YouTube...[/]")
with yt_dlp.YoutubeDL({"quiet": True, "extract_flat": True, "yes_playlist": True}) as ydl:
    playlist = ydl.extract_info(PLAYLIST_URL, download=False)

entries = playlist.get("entries", [])
console.print(f"[dim]Playlist has {len(entries)} videos[/]\n")

fixed = skipped = failed = no_match = 0

for i, entry in enumerate(entries, 1):
    yt_title = entry.get("title", "")
    yt_url   = f"https://www.youtube.com/watch?v={entry.get('id', '')}"

    console.print(f"\n[bold white][{i}/{len(entries)}][/] {yt_title[:75]}")

    match = find_matching_file(yt_title, local_files)
    if not match:
        console.print(f"  [yellow]⚠  No matching local file — skipping[/]")
        no_match += 1
        continue

    video_path = os.path.join(VIDEO_DIR, match)

    if has_audio(video_path):
        console.print(f"  [green]✅ Already has audio — skipping[/]")
        skipped += 1
        continue

    console.print(f"  [cyan]↳ File : {match[:65]}[/]")
    console.print(f"  [magenta]⬇  Downloading audio...[/]", end=" ")

    try:
        audio_path = download_audio(yt_url)
        if not audio_path or not os.path.exists(audio_path):
            raise Exception("Audio file not found after download")
        console.print("[green]done[/]")
    except Exception as e:
        console.print(f"[red]FAILED — {e}[/]")
        failed += 1
        continue

    temp_output = video_path.replace(".mp4", "_FIXED.mp4")
    console.print(f"  [yellow]🔀 Merging...[/]", end=" ")

    if merge_audio(video_path, audio_path, temp_output):
        os.replace(temp_output, video_path)
        os.remove(audio_path)
        console.print("[green]done ✅[/]")
        fixed += 1
    else:
        console.print("[red]FAILED[/]")
        if os.path.exists(temp_output):
            os.remove(temp_output)
        if os.path.exists(audio_path):
            os.remove(audio_path)
        failed += 1

console.print(f"""
[bold green]═══════════════════════════════[/]
[bold]  DONE![/]
[bold green]═══════════════════════════════[/]
  ✅ Fixed    : {fixed} videos
  ⏭  Skipped  : {skipped} (already had audio)
  ⚠  No match : {no_match}
  ❌ Failed   : {failed}
""")
