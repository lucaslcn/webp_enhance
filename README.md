# WebP Sticker Upscaler

A Python script that upscales WebP images (including animated ones) to WhatsApp sticker size (512x512) while preserving transparency and animation frames.

## Features

- Upscales WebP images to 512x512 pixels
- Preserves transparency (RGBA)
- Maintains animation frames and timing
- Uses high-quality Lanczos resampling
- Batch processing support
- Optimized for WhatsApp stickers

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone this repository
2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install requirements:
```bash
pip install Pillow
```

## Usage

1. Place your WebP files in the `input_images` directory
2. Run the script:
```bash
python upscale.py
```
3. Find the upscaled images in the `upscaled_images` directory

## Project Structure

```
web_project/
├── input_images/     # Place original WebP files here
├── upscaled_images/ # Upscaled images will be saved here
├── upscale.py      # Main script
├── README.md       # This file
└── requirements.txt # Project dependencies
```

## License

MIT License - feel free to use and modify as needed.
