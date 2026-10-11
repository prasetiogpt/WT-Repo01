#!/bin/bash
# Sync .md itinerary + Wisata.html dari repo Git ke folder Google Drive (Mac)
# Versi Mac dari sync-from-git-to-drive.bat

set -uo pipefail

REPO="$HOME/git-repos/wt-repo01"
DRIVE_ITIN="$HOME/Library/CloudStorage/GoogleDrive-prasetiogpt@gmail.com/My Drive/Travelling/China/Itinerary"
DRIVE_HTML="$HOME/Library/CloudStorage/GoogleDrive-prasetiogpt@gmail.com/My Drive/Travelling/HTML Wisata"
LOG="$REPO/wisata/china/sync.log"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting wisata git sync..." >> "$LOG"

cd "$REPO" || { echo "[X] Folder repo tidak ditemukan: $REPO" | tee -a "$LOG"; exit 1; }
git pull origin main >> "$LOG" 2>&1

if [ -d "$DRIVE_ITIN" ]; then
  cp -f "$REPO/wisata/china/Itinerary/"*.md "$DRIVE_ITIN/" >> "$LOG" 2>&1
  echo "  - Itinerary .md copied to Drive" >> "$LOG"
else
  echo "  - SKIPPED: Drive Itinerary folder not found (mount offline? cek path di script ini)" >> "$LOG"
fi

if [ -d "$DRIVE_HTML" ]; then
  cp -f "$REPO/wisata/china/Wisata.html" "$DRIVE_HTML/" >> "$LOG" 2>&1
  echo "  - Wisata.html copied to Drive (viewing only - generate/edit from the repo, not here)" >> "$LOG"
else
  echo "  - SKIPPED: Drive HTML Wisata folder not found (mount offline? cek path di script ini)" >> "$LOG"
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Sync done." >> "$LOG"
echo "" >> "$LOG"
