# Dynamic-Threshold-With-Python

Thresholding usually chooses the foreground as the foreground if the pixel value is greater than the threshold, and the background if it is less than the threshold for images with gray channels, and serves to split the image into parts. If the values such as light and shadow values in the picture differ, dynamic thresholding should be made for different parts of the picture instead of the same global thresholding for each pixel. 

When global thresholding (such as otsu) gives poor results local thresholding methods should be used.

## Method 1
In the desired picture, thresholding is circulated inside a square picture in the shape of n x n and the values of n x n pixels in this square are summed and divided into n x n. Thus, the average value of the pixels in the square is found. Then this value is accepted as the threshold value for this square and the constant value C is subtracted from the threshold value. Finally, binarization is done. This frame is circulated throughout the rest of the picture, these processes are repeated.

## Method 2
If the light to be accepted as the background in the picture is dispersed in different proportions or there are shadows, the object in the picture, which is accepted as the foreground, is erased from the picture with the morphological transformation (dilation, erosion) and the background of the picture is obtained.
When the matrix of the picture is divided by the matrix of this background, a homogeneous light adjustment is obtained. After this step, normalization and binarization process is applied for the matrix that takes values between [0,1].
(Original Image) / (Closed Image) = Foreground
The threshold value for binarization can be selected as static (127, global), otsu (global), method1 (local). The pre-binarization part of this method is applied to the picture below.

## Closing Operation and removing background
![closing ornek](https://user-images.githubusercontent.com/24410744/118506672-3299f680-b736-11eb-95dd-692754646629.png)

## Results
Top left image is original image, second and third one are otsu and static 127 threshold last image is the result of Method 1
### Example 1
<img src="https://user-images.githubusercontent.com/24410744/118508510-ef408780-b737-11eb-8b19-63346a9df32d.png" width="50%" height="50%">

### Example 2
<img src="https://user-images.githubusercontent.com/24410744/118508677-11d2a080-b738-11eb-9265-595166727f8e.png" width="50%" height="50%">
