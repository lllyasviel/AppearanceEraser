function [cluster_image] = showregion(r_label)
% assign same color to pixels with the same label
% Input:
%	r_label:	  [M * N, REQ] labels for each pixel
% Output:
% cluster_image:  [M * N * 3] generated color image
temp = unique(r_label);
cluster_num = length(temp);

color = randi(255, cluster_num, 3);

r = zeros(size(r_label));
g = zeros(size(r_label));
b = zeros(size(r_label));

label = zeros(size(r_label));
cluster_color = zeros(cluster_num, 2);

for i = 1 : cluster_num
	index = find(r_label == temp(i));
	r(index) = color(i, 1);
	g(index) = color(i, 2);
	b(index) = color(i, 3);
	label(index) = i;
end

cluster_image = zeros(size(label,1), size(label,2), 3);
cluster_image(:,:,1) = r;
cluster_image(:,:,2) = g;
cluster_image(:,:,3) = b;
cluster_image = uint8(cluster_image);
figure;
imshow(cluster_image);