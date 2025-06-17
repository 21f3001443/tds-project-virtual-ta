## Transforming Images

### Image Processing with PIL (Pillow)

[![Python Tutorial: Image Manipulation with Pillow (16 min)](https://i.ytimg.com/vi_webp/6Qs3wObeWwc/sddefault.webp)](https://youtu.be/6Qs3wObeWwc
<youtube_summary>This video tutorial demonstrates how to use the Python Pillow library for image manipulation tasks such as displaying, resizing, changing colors, and saving images. Pillow is particularly useful for automating batch image processing, like resizing multiple images for web thumbnails or galleries, which otherwise could be time-consuming when done manually.

The tutorial begins with installing Pillow, noting that on a Mac, additional external libraries need to be installed via Homebrew before running `pip install pillow`. After installation, the user can import Pillow modules using `from PIL import Image`.

The presenter works with sample images in the same directory as the Python script and shows how to open and display an image using `Image.open()` and `.show()`. They demonstrate saving an image in a different format (e.g., from JPEG to PNG) using the `.save()` method.

To batch convert multiple JPEG images to PNGs, the tutorial uses Python's `os` module to loop through all JPEG files in the directory, open each image, and save the converted PNG files into a newly created "pngs" folder.

Next, the tutorial covers resizing images while maintaining aspect ratio. A maximum size (e.g., 300x300 pixels) is defined, and the `.thumbnail()` method is used on each image before saving them into a "300" folder. The process is then extended to create multiple resized versions (e.g., 700 and 300 pixels) by duplicating the resizing and saving steps into separate folders.

Additional image manipulations are also shown:
- Rotating an image by 90 degrees using `.rotate(90)`
- Converting an image to black and white using `.convert('L')`
- Blurring an image with adjustable radius by importing `ImageFilter` and applying `.filter(ImageFilter.GaussianBlur(radius))`

The tutorial emphasizes the importance of consulting the Pillow documentation to learn available functions and parameters since memorizing them is impractical.

Overall, the video highlights how Pillow automates and simplifies many common image processing tasks, making it highly useful for developers managing images, such as for websites or applications. The presenter encourages viewers to explore the documentation for more advanced features and invites questions in the comments.</youtube_summary>
)

[Pillow](https://python-pillow.org/) is Python's leading library for image processing, offering powerful tools for editing, analyzing, and generating images. It handles various formats (PNG, JPEG, GIF, etc.) and provides operations from basic resizing to complex filters.

Here's a minimal example showing common operations:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["Pillow"]
# ///

from PIL import Image, ImageEnhance, ImageFilter

async def process_image(path: str) -> Image.Image:
    """Process an image with basic enhancements."""
    with Image.open(path) as img:
        # Convert to RGB to ensure compatibility
        img = img.convert('RGB')

        # Resize maintaining aspect ratio
        img.thumbnail((800, 800))

        # Apply enhancements
        img = (ImageEnhance.Contrast(img)
               .enhance(1.2))

        return img.filter(ImageFilter.SHARPEN)

if __name__ == "__main__":
    import asyncio
    img = asyncio.run(process_image("input.jpg"))
    img.save("output.jpg", quality=85)
```

Key features and techniques you'll learn:

- **Image Loading and Saving**: Handle various formats with automatic conversion
- **Basic Operations**: Resize, rotate, crop, and flip images
- **Color Manipulation**: Adjust brightness, contrast, and color balance
- **Filters and Effects**: Apply blur, sharpen, and other visual effects
- **Drawing**: Add text, shapes, and overlays to images
- **Batch Processing**: Handle multiple images efficiently
- **Memory Management**: Process large images without memory issues

### Basic Image Operations

Common operations for resizing, cropping, and rotating images:

```python
from PIL import Image

async def transform_image(
    path: str,
    size: tuple[int, int],
    rotation: float = 0
) -> Image.Image:
    """Transform image with basic operations."""
    with Image.open(path) as img:
        # Resize with anti-aliasing
        img = img.resize(size, Image.LANCZOS)

        # Rotate around center
        if rotation:
            img = img.rotate(rotation, expand=True)

        # Auto-crop empty edges
        img = img.crop(img.getbbox())

        return img
```

### Color and Enhancement

Adjust image appearance with built-in enhancement tools:

```python
from PIL import ImageEnhance, ImageOps

async def enhance_image(
    img: Image.Image,
    brightness: float = 1.0,
    contrast: float = 1.0,
    saturation: float = 1.0
) -> Image.Image:
    """Apply color enhancements to image."""
    enhancers = [
        (ImageEnhance.Brightness, brightness),
        (ImageEnhance.Contrast, contrast),
        (ImageEnhance.Color, saturation)
    ]

    for Enhancer, factor in enhancers:
        if factor != 1.0:
            img = Enhancer(img).enhance(factor)

    return img
```

### Filters and Effects

Apply visual effects and filters to images:

```python
from PIL import ImageFilter

def apply_effects(img: Image.Image) -> Image.Image:
    """Apply various filters and effects."""
    effects = {
        'blur': ImageFilter.GaussianBlur(radius=2),
        'sharpen': ImageFilter.SHARPEN,
        'edge': ImageFilter.FIND_EDGES,
        'emboss': ImageFilter.EMBOSS
    }

    return {name: img.filter(effect)
            for name, effect in effects.items()}
```

### Drawing and Text

Add text, shapes, and overlays to images:

```python
from PIL import Image, ImageDraw, ImageFont

async def add_watermark(
    img: Image.Image,
    text: str,
    font_size: int = 30
) -> Image.Image:
    """Add text watermark to image."""
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Position text at bottom-right
    x = img.width - text_width - 10
    y = img.height - text_height - 10

    # Add text with shadow
    draw.text((x+2, y+2), text, font=font, fill='black')
    draw.text((x, y), text, font=font, fill='white')

    return img
```

### Memory-Efficient Processing

Handle large images without loading them entirely into memory:

```python
from PIL import Image
import os

async def process_large_images(
    input_dir: str,
    output_dir: str,
    max_size: tuple[int, int]
) -> None:
    """Process multiple large images efficiently."""
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        with Image.open(input_path) as img:
            # Process in chunks using thumbnail
            img.thumbnail(max_size)
            img.save(output_path, optimize=True)
```

Practice with these resources:

- [Pillow Documentation](https://pillow.readthedocs.io/): Complete API reference
- [Python Image Processing Tutorial](https://realpython.com/image-processing-with-the-python-pillow-library/): In-depth guide
- [Sample Images Dataset](https://www.kaggle.com/datasets/lamsimon/celebs): Test images for practice

Watch these tutorials for hands-on demonstrations:

[![Image Processing Tutorial for beginners with Python PIL in 30 mins](https://i.ytimg.com/vi_webp/dkp4wUhCwR4/sddefault.webp)](https://youtu.be/dkp4wUhCwR4
<youtube_summary>This video tutorial provides a comprehensive guide to the Python Imaging Library, known as PIL or Pillow, which is used for image processing in Python. The key points covered include:

1. **Introduction to Pillow**: Pillow allows manipulation and processing of images, enabling changes and various image operations.

2. **Setup and Imports**: Importing essential modules such as `Image` from Pillow, `matplotlib` for displaying images within Jupyter notebooks, and `numpy`.

3. **Creating and Displaying Images**: Using `Image.open()` to create image objects and displaying images both via default OS viewers and within Jupyter using matplotlib.

4. **Image Properties**: Accessing image size (width × height), format (e.g., JPEG), and mode (e.g., RGB, HSV).

5. **Saving Images**: Saving edited images with `image.save()`.

6. **Cropping Images**: Cropping via specifying two diagonal points (left-top and right-bottom) to define the crop rectangle.

7. **Copying Images**: Making copies of images to preserve originals while applying transformations.

8. **Transposing and Rotating**: Changing image orientation through flipping left-right, top-bottom, rotating by 90°, 180°, 270°, or transposing (swapping rows and columns).

9. **Resizing Images**: Changing image dimensions using tuples (width, height) and different interpolation algorithms (nearest, box, bilinear, hamming, bicubic, and lanczos) affecting image quality.

10. **Rotation by Angle**: Rotating images by arbitrary angles using `image.rotate()`.

11. **Adding Text Watermarks**: Creating editable images with `ImageDraw.Draw()`, selecting fonts with `ImageFont.truetype()`, and adding text at specified positions with customizable color.

12. **Adding Image Watermarks**: Creating thumbnails that preserve aspect ratio, then pasting these smaller images onto base images at specified coordinates.

13. **Color Mode Conversion**: Converting images to black and white (`L` mode), HSV, and other color modes useful for computer vision and deep learning.

14. **Converting Between PIL Images and NumPy Arrays**: Using `np.array()` to convert images to arrays and `Image.fromarray()` to convert arrays back to images, noting differences in dimension ordering.

15. **Image Enhancement**: Enhancing color, contrast, brightness, and sharpness via `ImageEnhance` with adjustable factors (>1 to enhance, <1 to reduce).

16. **Alpha Blending**: Combining two images with transparency by blending them based on an alpha value between 0 and 1, requiring images to be the same size and have alpha channels.

17. **Image Transforms**: Applying affine transforms (changing perspective with a 6-value matrix) and extent transforms (cropping and zooming a section), though math details are briefly touched upon.

18. **Flipping Color Channels**: Splitting an image into RGB channels and merging them back in different orders (e.g., BGR) to suit frameworks like TensorFlow or PyTorch.

The tutorial emphasizes practical coding examples and visual demonstrations for each operation, aiming to equip viewers with a solid understanding of Pillow's capabilities for image manipulation in Python.</youtube_summary>
)

### Image Processing with ImageMagick

[ImageMagick](https://imagemagick.org/) is a powerful command-line tool for image manipulation, offering features beyond what's possible with Python libraries. It's particularly useful for:

- Batch processing large image collections
- Complex image transformations
- High-quality format conversion
- Creating image thumbnails
- Adding text and watermarks

Basic Operations:

```bash
# Format conversion
convert input.png output.jpg

# Resize image (maintains aspect ratio)
convert input.jpg -resize 800x600 output.jpg

# Compress image quality
convert input.jpg -quality 85 output.jpg

# Rotate image
convert input.jpg -rotate 90 output.jpg
```

Common Data Science Tasks:

```bash
# Create thumbnails for dataset preview
convert input.jpg -thumbnail 200x200^ -gravity center -extent 200x200 thumb.jpg

# Normalize image for ML training
convert input.jpg -normalize -strip output.jpg

# Extract dominant colors
convert input.jpg -colors 5 -unique-colors txt:

# Generate image statistics
identify -verbose input.jpg | grep -E "Mean|Standard|Kurtosis"
```

Batch Processing:

```bash
# Convert all images in a directory
mogrify -format jpg *.png

# Resize multiple images
mogrify -resize 800x600 -path output/ *.jpg

# Add watermark to images
for f in *.jpg; do
    convert "$f" -gravity southeast -draw "text 10,10 'Copyright'" "watermarked/$f"
done
```

Advanced Features:

```bash
# Apply image effects
convert input.jpg -blur 0x3 blurred.jpg
convert input.jpg -sharpen 0x3 sharp.jpg
convert input.jpg -edge 1 edges.jpg

# Create image montage
montage *.jpg -geometry 200x200+2+2 montage.jpg

# Extract image channels
convert input.jpg -separate channels_%d.jpg

# Composite images
composite overlay.png -gravity center base.jpg output.jpg
```

Watch this ImageMagick tutorial (16 min):

[![ImageMagick Introduction (16 min)](https://i.ytimg.com/vi_webp/wjcBOoReYc0/sddefault.webp)](https://youtu.be/wjcBOoReYc0
<youtube_summary>This video provides an introductory overview of ImageMagick, a versatile command-line tool for image manipulation. The presenter explains that ImageMagick supports numerous image-related operations and has extensive documentation. They note that they are using ImageMagick version 6, which remains widely supported despite the existence of version 7.

The video begins by demonstrating the "identify" command, which outputs detailed information about an image, such as file type, dimensions, color space, and pixel statistics. Next, the presenter covers basic image conversion using the "convert" command, showing how to change a JPEG image to PNG format. The "convert" command also allows opening images directly within ImageMagick.

Resizing images is then explored, illustrating how specifying dimensions like "1000x1000" maintains the aspect ratio by default, resulting in one dimension being smaller. Adding an exclamation mark forces the image to resize to exact dimensions, potentially distorting it. Alternatively, resizing by percentage (e.g., 50%) is shown.

The video concludes with a more advanced example combining multiple ImageMagick commands to create a "model village" effect on a photo. This involves three steps: applying sigmoidal contrast to enhance color pop, adjusting brightness with "modulate," generating a blur map using sparse color barycentric and polynomial functions to create a gradient blur effect from center to edges, and finally compositing the contrast and blur map images to produce the final stylized image. The presenter explains how these steps manipulate contrast, brightness, and selective blurring to achieve the effect.

Overall, the video introduces simple to complex ImageMagick operations, demonstrating its power for batch image processing and creative effects from the command line.</youtube_summary>
)

Tools:

- [Fred's ImageMagick Scripts](http://www.fmwconcepts.com/imagemagick/): Useful script collection
- [ImageMagick Online Studio](https://magickstudio.imagemagick.org/): Visual command builder

Tips:

1. Use `-strip` to remove metadata and reduce file size
2. Monitor memory usage with `-limit memory 1GB`
3. Use `-define` for format-specific options
4. Process in parallel with `-parallel`
5. Use `-monitor` to track progress

Error Handling:

```bash
# Check image validity
identify -regard-warnings input.jpg

# Get detailed error information
convert input.jpg output.jpg 2>&1 | grep -i "error"

# Set resource limits
convert -limit memory 1GB -limit map 2GB input.jpg output.jpg
```

For Python integration:

```python
# /// script
# requires-python = ">=3.9"
# dependencies = ["Wand"]
# ///

from wand.image import Image

async def process_image(path: str) -> None:
    """Process image with ImageMagick via Wand."""
    with Image(filename=path) as img:
        # Basic operations
        img.resize(800, 600)
        img.normalize()

        # Apply effects
        img.sharpen(radius=0, sigma=3)

        # Save with compression
        img.save(filename='output.jpg')
```

Note: Always install ImageMagick before using the Wand Python binding.
