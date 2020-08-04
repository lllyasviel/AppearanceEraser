img=imread('input.png');
mask=imread('mask.png');
output=L0Smoothing(img,mask,0.01);
imwrite(output, 'output.png');
