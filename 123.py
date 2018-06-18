from PIL import Image
import pytesseract
Image=Image.open('2.png')
text=pytesseract.image_to_string(Image,lang='chi_sim')
print(text)
def save(filename, text):
  fh = open(filename, 'w',encoding='utf8',)
  fh.write(text)
  fh.close()
save('file.name', text)