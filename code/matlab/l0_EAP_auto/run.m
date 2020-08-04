img=imread('input.png');
output=eap(img, 0.1, @(a, b)L0Smoothing(a,b,0.01));
imwrite(output, 'output.png');
