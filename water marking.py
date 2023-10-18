import cv2
import numpy as np
image_path = 'img.jpg'  
image = cv2.imread(image_path)

watermark_text = 'Your Watermark'
position = (50, 50)  


font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2

color = (0, 0, 255) 


watermarked_image = image.copy()
cv2.putText(watermarked_image, watermark_text, position, font, font_scale, color, font_thickness, cv2.LINE_AA)


cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


output_path = 'img.jpg'  
cv2.imwrite(output_path, watermarked_image)

