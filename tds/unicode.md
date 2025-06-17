## Unicode

Ever noticed when you copy-paste some text and get garbage symbols? Or see garbage when you load a CSV file? This video explains why. It covers how computers store text (called character encoding) and why it sometimes goes wonky.

Learn about ASCII (the original 7-bit encoding system that could only handle 128 characters), why that wasn't enough for global languages, and how modern solutions like Unicode save the day by letting us use any character from any language.

Some programs try to guess encodings (sometimes badly!). A signature called BOM (Byte Order Mark)helps computers know exactly how to read text files correctly.

Learn how Unicode, UTF-8 and character encoding works. This is a common gotcha when building apps that handle international text - something bootcamps often skip but developers and data scientists regularly face in the real world.

Unicode is fundamental for data scientists working with international data. Here are key concepts you need to understand:

- **Character Encodings**: Different ways to represent text in computers
  - ASCII (7-bit): Limited to 128 characters, English-only
  - UTF-8: Variable-width encoding, backwards compatible with ASCII
  - UTF-16: Fixed-width encoding, used in Windows and Java
  - UTF-32: Fixed-width encoding, memory inefficient but simple

Common encoding issues you'll encounter:

```python
# Reading files with explicit encoding
with open('file.txt', encoding='utf-8') as f:
    text = f.read()

# Handling encoding errors
import pandas as pd
df = pd.read_csv('data.csv', encoding='utf-8', errors='replace')

# Detecting file encoding
import chardet
with open('unknown.txt', 'rb') as f:
    result = chardet.detect(f.read())
print(result['encoding'])
```

[![Code Pages, Character Encoding, Unicode, UTF-8 and the BOM - Computer Stuff They Didn't Teach You #2 (17 min)](https://i.ytimg.com/vi_webp/jeIBNn5Y5fI/sddefault.webp)](https://youtu.be/jeIBNn5Y5fI
<youtube_summary>Scott Hanselman presents a video titled "Things They Didn't Teach You," aimed at sharing useful programming knowledge that might be overlooked or forgotten. In this episode, he focuses on character encoding, explaining challenges programmers face when handling text files with various characters, especially non-Latin ones. He revisits ASCII, noting it uses 7 bits to represent 128 characters, and demonstrates through a C# console app how bytes from 0 to 127 correspond to ASCII codes.

Hanselman then explores extending to 256 bytes, highlighting that values above 127 depend on the "code page" or character encoding, which varies (e.g., Windows code pages 1250, 437, ISO 8859-1). Different code pages assign different meanings to bytes above 127, affecting how characters display. He points out that text editors like Notepad guess encodings, sometimes incorrectly, leading to garbled text.

He discusses Unicode and UTF encodings, explaining the importance of the Byte Order Mark (BOM)—a special sequence of bytes at the file start that indicates encoding and byte order—helping software correctly interpret text. Hanselman shows how saving files with or without BOM affects character display, especially for complex characters like Chinese symbols. He demonstrates using Windows char map to find and insert Unicode characters.

Finally, he emphasizes the critical need to understand character encoding when handling strings since without knowledge of encoding, software must guess, which can cause errors. BOM helps but is not always present. He invites viewers to comment with questions or video suggestions and encourages subscribing.</youtube_summary>
)
