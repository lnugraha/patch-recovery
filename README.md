# Reverse Patch
Finding the top left coordinate position of an image patch from its original full size image

## Provided Information ##
1. An image patch in 8-bit grayscale format
2. A full size image where the image patch is cropped

## Index Conversion ##
1. Convert 2D index (x, y) to 1D global index (idx):
<br /><p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=\LARGE&space;idx&space;=&space;y*cols&space;&plus;&space;x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\LARGE&space;idx&space;=&space;y*cols&space;&plus;&space;x" title="\LARGE idx = y*cols + x" /></a></p>

2. Convert 1D global index (idx) back to 2D index (x, y):
<br /><p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=\LARGE&space;x&space;=&space;idx&space;%&space;cols" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\LARGE&space;x&space;=&space;idx&space;%&space;cols" title="\LARGE x = idx % cols" /></a></p>
<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=\LARGE&space;y&space;=&space;floor(\frac{idx-x}{cols})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\LARGE&space;y&space;=&space;floor(\frac{idx-x}{cols})" title="\LARGE y = floor(\frac{idx-x}{cols})" /></a></p>

## Minimizing Errors ## 

## Illustration ##
