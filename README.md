# Smart Document Scanner & Text Extractor (OCR)\

A docoument scanner and text editor project built using Python and OpenCV

The gole of this project is to performs automatic edge detection, 4-point perspective transformation to "flatten" skewed documents, image cleaning (adaptive thresholding), and optical character recognition

## Current Progress

--> Load input image.

--> Resize the original image for faster processing.

--> Convert image to greyscale : This is important edge detection is    mathematically calculated by measuring how rapid the pixel intensity     changes from one pixel to the next.

--> Applying Gaussian Blur : Gaussian blur is important as it blends away the tiny surface patterns,such as the wood grain, scratches on a desk, or paper texture,so the edge detector does not treat every tiny texture line as a border.



## Technologies used

-- Python
-- OpenCV


## Project status

Currently in development(starting phase)
