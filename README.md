# Padded Image Resizer

This library can resize image while keeping the aspect ratio as it is and will add padding to reach the target size. This library is mainly designed to used fro data preprocessing tool for deep leanrning algorithms, due to images obtained from online sources will have diferent aspect ratio and size.

## Implimentation
clone/download the repository to your working/local directory
```
git clone https://github.com/chekoduadarsh/Padded-Image-Resizer
```
### Bulk Resize
```python3
from padded_image_resizer import bulk_resizer
bulk_resizer(input_path="path/to/input/image/directory",output_path="path/to/output/directory",desired_size=32,color=[0,0,0],rename = True)
```
This will resize and convert all the image files in the given dirctory to given size in `desired_size` with a padding color given in `color` given as [B,G,R]. If `rename` is enabled this will rename all the files in non repeating whole number series

### Resize
```python3
from padded_image_resizer import resizer
resizer(im_pth="path/to/input/image/directory/image.png",output_path="path/to/output/directory",desired_size=32,color=[0,0,0],rename = True)
```
This is similar to bulk resize, rather than input folder path we will be giving image path in `im_pth` and  `rename` will rename the file to 0
