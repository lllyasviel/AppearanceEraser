img=imread('input.png');
output=L0Smoothing(img,0.01);
imwrite(output, 'output.png');
