#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from datetime import datetime
import yt_dlp


def download_x_video(url, output_dir="Twitter_Download"):
    """
    Downloads a video from X (formerly Twitter) in the best available quality.
    
    Args:
        url: Link to the X post containing the video
        output_dir: Target directory where the video will be saved
    
    Returns:
        Path to the downloaded file or None in case of an error
    """
    # Check if the target directory exists, create it if it doesn't
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Filename format: date_time_post_ID.mp4
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    
    # Download options configuration
    ydl_opts = {
        'format': 'best',  # Best quality
        'outtmpl': os.path.join(output_dir, f'{timestamp}_%(id)s.%(ext)s'),
        'verbose': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info)
            print(f"Video has been downloaded to: {video_path}")
            return video_path
    except Exception as e:
        print(f"Error during download: {e}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(description='Download videos from X (formerly Twitter) in the best quality')
    parser.add_argument('url', help='Link to an X post containing a video')
    parser.add_argument('-o', '--output', default='Twitter_Download',
                        help='Target directory for downloaded videos (default: Twitter_Download)')
    args = parser.parse_args()
    
    download_x_video(args.url, args.output)


if __name__ == "__main__":
    main()