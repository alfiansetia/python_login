# import pytesseract
# import requests
# from PIL import Image, ImageEnhance, ImageFilter
# from io import BytesIO

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# image_path = "captcha_downloaded.png"
# img = Image.open(image_path)

# text = pytesseract.image_to_string(img)

# print("Hasil CAPTCHA:", text)



# import cv2
# import numpy as np
# import easyocr

# # Load gambar
# image_path = "captcha_downloaded.png"
# img = cv2.imread(image_path, cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Terapkan GaussianBlur untuk mengurangi noise
# gray = cv2.GaussianBlur(gray, (3, 3), 0)

# # Gunakan threshold untuk meningkatkan kontras
# _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# # Hapus garis dengan deteksi kontur
# contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     aspect_ratio = w / h
#     if aspect_ratio > 5:  # Anggap sebagai garis jika sangat lebar
#         cv2.drawContours(thresh, [cnt], -1, (0, 0, 0), thickness=cv2.FILLED)

# # Simpan hasil preprocessing
# cv2.imwrite("processed_captcha.png", thresh)

# # Gunakan EasyOCR dengan konfigurasi tambahan
# reader = easyocr.Reader(['en'])
# result = reader.readtext(thresh, detail=0)

# # Gabungkan teks hasil OCR
# captcha_text = "".join(result)
# print("Hasil CAPTCHA:", captcha_text)



from PIL import Image, ImageFilter
from scipy.ndimage import gaussian_filter
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def solve_captcha(filename):
    # Thresholds and blurring sigma
    th1 = 140
    th2 = 140  
    sig = 1.5  

    # Load and save the original image
    original = Image.open(filename)
    # Convert to black and white
    black_and_white = original.convert("L")
    black_and_white.save("black_and_white.png")

    # Apply the first threshold
    first_threshold = black_and_white.point(lambda p: p > th1 and 255)
    first_threshold.save("first_threshold.png")

    # Apply Gaussian blur
    blur = np.array(first_threshold)  # Create an image array
    blurred = gaussian_filter(blur, sigma=sig)
    blurred = Image.fromarray(blurred)
    blurred.save("blurred.png")

    # Apply the final threshold
    final = blurred.point(lambda p: p > th2 and 255)
    final = final.filter(ImageFilter.EDGE_ENHANCE_MORE)
    final = final.filter(ImageFilter.SHARPEN)
    final.save("final.png")

    # Perform OCR using Tesseract
    result = pytesseract.image_to_string(final, lang='eng', config='--psm 7')

    # Print the result
    print(f"Captured CAPTCHA: {result}")
    return result

# Example usage
result = solve_captcha('captcha_downloaded.png')
