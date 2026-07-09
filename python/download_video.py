# ================================
# Project  : Media Downloader
# Author   : Jayesh Chaudhari
# Date     : 28-05-2026
# Topic    : Video + Audio Downloader (Height Only Check)
# ================================

import yt_dlp
from rich.console import Console
from rich.progress import (
    Progress, BarColumn, DownloadColumn,
    TransferSpeedColumn, TimeRemainingColumn, TextColumn
)
from rich.panel import Panel

console = Console()
OUTPUT = "/mnt/d/Videos/%(title)s.%(ext)s"


def download_video(url):

    with Progress(
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(bar_width=38),
        DownloadColumn(),                   # shows  45.2 MB / 1.2 GB
        TextColumn("[dim]•[/]"),
        TransferSpeedColumn(),              # shows  3.4 MB/s
        TextColumn("[dim]•[/]"),
        TimeRemainingColumn(),              # shows  eta 0:02:14
        console=console,
    ) as progress:

        task = progress.add_task("[cyan]Fetching info...", total=None)
        phase_index = [0]   # 0 = video stream, 1 = audio stream

        def hook(d):
            if d["status"] == "downloading":
                downloaded = d.get("downloaded_bytes", 0)
                total = d.get("total_bytes") or d.get(
                    "total_bytes_estimate", 0)
                label = "Video" if phase_index[0] == 0 else "Audio"
                progress.update(
                    task,
                    completed=downloaded,
                    total=total if total > 0 else None,
                    description=f"[cyan]Downloading {label}...",
                )

            elif d["status"] == "finished":
                if phase_index[0] == 0:               # video done → now audio
                    phase_index[0] = 1
                    progress.reset(task)
                    progress.update(
                        task, description="[magenta]Downloading Audio...")
                else:                                  # audio done → merging
                    progress.update(
                        task, description="[yellow]Merging streams...")

        ydl_opts = {
            "format": "bestvideo[height>=1080]+bestaudio",
            "merge_output_format": "mkv",
            "noplaylist": True,
            "outtmpl": OUTPUT,
            "progress_hooks": [hook],
            "quiet": True,
            "no_warnings": True,
            "no_check_certificate": True,
            "extractor_args": {"global": {"age_verify": True}},

            # Subtitle options
            "writesubtitles": True,          # download manual subtitles if available
            # fallback to auto-generated subs if manual don't exist
            "writeautomaticsub": True,
            "subtitleslangs": ["en"],        # language preference (English)
            "embedsubtitles": True,          # embed subtitles into the final MKV file
            "subtitlesformat": "srt/best",    # prefer SRT format, fall back to best available
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get("title", "Unknown")
                width = info.get('width')
                height = info.get('height')
                res = f"{width if width else '?'}(w) x {height if height else '?'}(h)"
                dur = info.get("duration_string", "N/A")

            progress.update(task, description="[bold green]✅ Completed!")
            console.print(f"\n[bold green]✅ Downloaded:[/] [yellow]{title}[/]")
            console.print(f"   [dim]Resolution : {res}[/]")
            console.print(f"   [dim]Duration   : {dur}[/]")
            console.print(f"   [dim]Saved to   : D:\\Videos\\[/]\n")

        except Exception as e:
            progress.update(task, description="[bold red]❌ Cancelled")

            if "Requested format is not available" in str(e):
                console.print(
                    "\n[bold red]❌ Error: Video is not available in high quality![/]")
                console.print(
                    "[yellow]⚠  The link does not provide 1080p, 1440p, 4K, or 8K streams. Download aborted.[/]\n")
            else:
                console.print(f"\n[bold red]❌ Error:[/] {e}\n")


# ─── Main ────────────────────────────────────────────────────────────────────

console.print(Panel(
    "[bold yellow]🎬  YouTube Video + Audio Downloader[/]",
    subtitle="[dim]by Jayesh Chaudhari[/]",
    border_style="cyan",
))
console.print("[dim]  Enter a URL to download  •  T to terminate[/]\n")

while True:
    url = console.input(
        "[bold green]▶ URL[/] (or [bold red]T[/] to stop): ").strip()

    if url.upper() == "T":
        console.print("\n[bold cyan]Downloader terminated. Bye Jayesh! 👋[/]\n")
        break

    if url == "":
        console.print("[yellow]⚠  No URL entered. Try again![/]")
        continue

    download_video(url)