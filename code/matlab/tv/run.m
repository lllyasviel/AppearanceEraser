img=imread('input.png');
output=TVL1denoise(img, 1.0, 100);
imwrite(output, 'output.png');
