addpath('./libs');
img=imread('input.png');
output = l1flattening(img, struct());
imwrite(output, 'output.png');