import cv2
from matplotlib.pyplot import gray

image = cv2.imread(r"C:\Users\risha\OneDrive\Pictures\sample.jpeg")

# Resize to a manageable height for faster processing

ratio = image.shape[0]/700.0
original = image.copy()
resized_image = cv2.resize(image,(int(image.shape[1]/ratio),600))
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# convert to greyscale

grey = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image", grey)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Gaussian blur to reduce noise and improve edge detection

blurred = cv2.GaussianBlur(grey,(5,5),0)
cv2.imshow("Blurred_image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
