img=imread('input.png');
mask=imread('mask.png');
output=TVL1denoise(img, mask, 1.0, 100);
imwrite(output, 'output.png');
