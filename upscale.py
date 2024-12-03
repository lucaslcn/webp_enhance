from PIL import Image
import os
from pathlib import Path

def upscale_animated_webp(input_dir, output_dir, target_size=(512, 512)):
    """
    Upscale WebP images to WhatsApp sticker size while preserving animation.
    
    Args:
        input_dir (str): Directory containing WebP images
        output_dir (str): Directory where upscaled images will be saved
        target_size (tuple): WhatsApp recommended size (512x512)
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    webp_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.webp')]
    total_files = len(webp_files)
    
    print(f"Found {total_files} WebP files to process...")
    
    for index, filename in enumerate(webp_files, 1):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        try:
            # Open the image
            with Image.open(input_path) as img:
                print(f"\nProcessing ({index}/{total_files}): {filename}")
                print(f"Original size: {img.size}")
                
                # Check if image is animated
                is_animated = hasattr(img, 'n_frames') and img.n_frames > 1
                
                if is_animated:
                    print(f"Animated WebP detected with {img.n_frames} frames")
                    frames = []
                    durations = []
                    
                    # Process each frame
                    for frame in range(img.n_frames):
                        img.seek(frame)
                        # Convert to RGBA and resize
                        new_frame = img.convert('RGBA').resize(target_size, Image.Resampling.LANCZOS)
                        frames.append(new_frame)
                        durations.append(img.info.get('duration', 100))  # Default to 100ms if not specified
                    
                    # Save animated WebP
                    frames[0].save(
                        output_path,
                        'WEBP',
                        save_all=True,
                        append_images=frames[1:],
                        duration=durations,
                        loop=0,
                        quality=100,
                        method=6
                    )
                else:
                    # Handle static images as before
                    upscaled_img = img.convert('RGBA').resize(target_size, Image.Resampling.LANCZOS)
                    upscaled_img.save(output_path, 'WEBP', quality=100, method=6)
                
                print(f"New size: {target_size}")
                print(f"Saved to: {output_path}")
                print(f"Animation preserved: {'Yes' if is_animated else 'No'}")
                
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    input_dir = os.path.join(current_dir, "input_images")
    output_dir = os.path.join(current_dir, "upscaled_images")
    
    upscale_animated_webp(input_dir, output_dir)
    print("\nProcessing complete! Check the upscaled_images directory for your animated stickers.")