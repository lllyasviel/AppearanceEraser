img=imread('input.png');
output=eap(img, 0.1, @(a, b)tsmooth(a, b, 0.015, 3));
imwrite(output, 'output.png');
