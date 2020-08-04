img=imread('input.png');
output=eap(img, 0.1, @(a, b)TVL1denoise(a, b, 1.0, 100));
imwrite(output, 'output.png');
