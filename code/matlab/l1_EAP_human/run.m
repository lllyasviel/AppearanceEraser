addpath('./libs');
img=imread('input.png');
mask=imread('mask.png');
output = l1flattening(img, mask, struct());
imwrite(output, 'output.png');