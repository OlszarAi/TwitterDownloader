# X (Twitter) Video Downloader

A simple Python utility to download videos from X (formerly Twitter) in the highest possible quality.

## Features

- Downloads videos from X (Twitter) with a single command
- Saves videos in the best available quality
- Automatically creates custom filenames with timestamps
- Allows specifying a custom download directory

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone this repository or download the source code.

2. Install the required dependencies:

```bash
pip install yt-dlp
```

## Usage

### Basic Usage

Run the script with a URL to an X post containing a video:

```bash
python twitter_downloader.py https://x.com/username/status/123456789
```

This will download the video and save it to the default `Twitter_Download` directory.

### Advanced Options

To specify a custom output directory:

```bash
python twitter_downloader.py https://x.com/username/status/123456789 -o custom_folder
```

### Command-Line Arguments

- `url`: The URL of the X post containing the video (required)
- `-o, --output`: Custom output directory (optional, defaults to "Twitter_Download")

## Output Format

Downloaded videos are saved with filenames in the following format:

```
YYYYMMDD_HHMMSS_POST_ID.mp4
```

For example:
```
20250414_221320_1911851074211766272.mp4
```

## Troubleshooting

If you encounter issues downloading videos:

1. Make sure the URL is correct and the post contains a video
2. Update the yt-dlp library: `pip install --upgrade yt-dlp`
3. Check if the X API has changed, which may require an update to the script

## License

This project is available for free use under the MIT license.
