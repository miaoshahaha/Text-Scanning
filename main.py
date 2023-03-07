from PIL import Image
import pytesseract

def main():
    img_chinese = Image.open('test_chi.jpeg')
    img_english = Image.open('test_eng.png')
    text_chinese = pytesseract.image_to_string(img_chinese, lang="chi_tra")
    text_english = pytesseract.image_to_string(img_english, lang="eng")

    print(text_chinese)

if __name__ == '__main__':
    main()