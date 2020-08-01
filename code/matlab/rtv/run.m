img=imread('input.png');
output = tsmooth(img,0.015,3);
imwrite(output, 'output.png');
