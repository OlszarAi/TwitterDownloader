#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from datetime import datetime
import yt_dlp


def download_x_video(url, output_dir="znalezione_filmy"):
    """
    Pobiera film z X (dawniej Twitter) w najlepszej dostępnej jakości.
    
    Args:
        url: Link do posta na X zawierającego film
        output_dir: Katalog docelowy, do którego zostanie zapisany film
    
    Returns:
        Ścieżka do pobranego pliku lub None w przypadku błędu
    """
    # Sprawdź czy katalog docelowy istnieje, jeśli nie - utwórz go
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Format nazwy pliku: data_godzina_ID_posta.mp4
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    
    # Konfiguracja opcji pobierania
    ydl_opts = {
        'format': 'best',  # Najlepsza jakość
        'outtmpl': os.path.join(output_dir, f'{timestamp}_%(id)s.%(ext)s'),
        'verbose': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info)
            print(f"Film został pobrany do: {video_path}")
            return video_path
    except Exception as e:
        print(f"Błąd podczas pobierania: {e}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(description='Pobieranie filmów z X (dawniej Twitter) w najlepszej jakości')
    parser.add_argument('url', help='Link do posta na X zawierającego film')
    parser.add_argument('-o', '--output', default='znalezione_filmy',
                        help='Katalog docelowy dla pobranych filmów (domyślnie: znalezione_filmy)')
    args = parser.parse_args()
    
    download_x_video(args.url, args.output)


if __name__ == "__main__":
    main()