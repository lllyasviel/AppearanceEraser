function output = eap(imgr,u,func)
img = double(imgr);
[height, width, ~]=size(img); 
mask = rand(height, width);
mask(mask < 0.5) = 0;
mask(mask > 0) = 255;
eps_weight = 1.0;
for k=1:5
    disp(k);
    output=func(img, repmat(mask, [1, 1, 3]));
    imwrite(mask, 'mask.png');
    imwrite(output, 'output.png');
    value = sum((output - img).^2,3);
    weight = sum((output - imboxfilt(output,3)).^2,3);
    knapsack = value./(weight + eps_weight);
    thre = sort(knapsack(:));
    thre = thre(int64(double(height*width)*(1.0 - double(k) * u / 5.0)));
    knapsack = knapsack./thre;
    mask = ones(height, width);
    alpha = double(5 - k)./4.0;
    mask(rand(height, width).*alpha +1.0-alpha<knapsack) = 255;
    mask(mask < 255) = 0;
end
end

