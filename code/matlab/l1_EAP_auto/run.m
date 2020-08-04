img=imread('input.png');
output=eap(img, 0.1, @(a, b)l1flattening(a, b, struct()));
imwrite(output, 'output.png');
