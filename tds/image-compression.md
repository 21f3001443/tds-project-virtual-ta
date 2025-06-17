## Images: Compression

Image compression is essential when deploying apps. Often, pages have dozens of images. Image analysis runs over thousands of images. The cost of storage and bandwidth can grow over time.

Here are things you should know when you're compressing images:

- **Image dimensions** are the width and height of the image in pixels. This impacts image size a lot
- **Lossless** compression (PNG, WebP) preserves exact data
- **Lossy** compression (JPEG, WebP) removes some data for smaller files
- **Vector** formats (SVG) scale without quality loss
- **WebP** is the modern standard, supporting both lossy and lossless

Here's a rule of thumb you can use as of 2025.

- Use SVG if you can (i.e. if it's vector graphics or you can convert it to one)
- Else, reduce the image to as small as you can, and save as (lossy or lossless) WebP

Common operations with Python:

```python
from pathlib import Path
from PIL import Image
import io

async def compress_image(input_path: Path, output_path: Path, quality: int = 85) -> None:
    """Compress an image while maintaining reasonable quality."""
    with Image.open(input_path) as img:
        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        # Optimize for web
        img.save(output_path, 'WEBP', quality=quality, optimize=True)

# Batch process images
paths = Path('images').glob('*.jpg')
for p in paths:
    await compress_image(p, p.with_suffix('.webp'))
```

Command line tools include [cwebp](https://developers.google.com/speed/webp/docs/cwebp), [pngquant](https://pngquant.org/), [jpegoptim](https://github.com/tjko/jpegoptim), and [ImageMagick](https://imagemagick.org/).

```bash
# Convert to WebP
cwebp -q 85 input.png -o output.webp

# Optimize PNG
pngquant --quality=65-80 image.png

# Optimize JPEG
jpegoptim --strip-all --all-progressive --max=85 image.jpg

# Convert and resize
convert input.jpg -resize 800x600 output.jpg

# Batch convert
mogrify -format webp -quality 85 *.jpg
```

Watch this video on modern image formats and optimization (15 min):

[![Modern Image Optimization (15 min)](https://i.ytimg.com/vi_webp/F1kYBnY6mwg/sddefault.webp)](https://youtu.be/F1kYBnY6mwg
<youtube_summary>In this discussion, Jake Archibald and Surma explore image compression, emphasizing its importance as images make up about 50% of webpage data. They note that many web images can be significantly compressed without losing visual fidelity by choosing better formats, encoders, or settings.

They categorize image formats into lossy (JPEG, WebP) and lossless (PNG, GIF, WebP), clarifying that GIF is lossless but limited to 256 colors. For digital drawings, SVG is ideal due to scalability, but complex drawings with gradients might compress better in lossy or lossless raster formats depending on the content.

Jake explains how lossy compression struggles with sharp edges and small details in low-detail areas, while lossless compression is challenged by unpredictable color changes and the total number of colors. Vector formats depend on shape complexity, which can affect CPU usage.

They demonstrate chroma subsampling in lossy codecs, which reduces color resolution more than brightness since human eyes are more sensitive to brightness changes, leading to significant data savings with minimal perceived quality loss. They also discuss how lossy codecs use an 8x8 block-based frequency transform (e.g., Discrete Cosine Transform) to represent images, allowing compression by zeroing out less important frequency components, which humans often cannot detect.

WebP is highlighted as a superior format to JPEG, offering variable block sizes, better compression strategies, arithmetic compression, and alpha transparency support. However, JPEG remains necessary due to Safari's lack of WebP support. They recommend using the picture element to serve WebP to supporting browsers and JPEG as fallback.

Using tools like Squoosh.app, they show practical image compression workflows, advising to resize images to actual display size (accounting for screen density), then adjust quality settings to just before noticeable degradation, cautioning against zooming in too much when evaluating quality. They discuss advanced WebP settings like filtering and spatial noise shaping (SNS), which redistribute bits to areas needing more detail, improving visual quality at the cost of encoding time.

For lossless compression, they explain prediction-based methods that encode pixel differences relative to neighbors and strategies to optimize this. WebP lossless supports 2D blocks and multiple prediction strategies, improving compression over PNG. Palette reduction (reducing number of colors) can drastically reduce file size in images with limited colors, though dithering may be needed to reduce banding at the cost of larger files.

They strongly advise against using GIF due to its inefficiency.

They also compare SVG with raster formats for complex vector images, noting SVG's high CPU cost during rendering and resizing, which can cause jank even on high-end devices. Sometimes, a lossy WebP version is preferable for performance despite slightly larger file size.

Their key takeaway is to understand how codecs work and choose compression strategies based on image content and codec strengths rather than rigid rules. They encourage experimenting with different formats and settings to optimize image size and performance, ultimately improving web page load times and user experience.</youtube_summary>
)

Tools for image optimization:

- [squoosh.app](https://squoosh.app/): Browser-based compression
- [ImageOptim](https://imageoptim.com/): GUI tool for Mac
- [sharp](https://sharp.pixelplumbing.com/): Node.js image processing
- [Pillow](https://python-pillow.org/): Python imaging library
