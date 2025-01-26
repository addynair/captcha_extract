from PIL import Image
import pytesseract


image_path = 'exp3.png'  
img = Image.open(image_path)


extracted_text = pytesseract.image_to_string(img)
print(f"Extracted Expression: '{extracted_text.strip()}'")


try:
    result = eval(extracted_text.strip())
    print(f"The result of the expression '{extracted_text.strip()}' is: {result}")
except Exception as e:
    print(f"Error evaluating expression: {e}")
