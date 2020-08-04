img=imread('input.png');
mask=imread('mask.png');
output = tsmooth(img,mask,0.015,3);
imwrite(output, 'output.png');
