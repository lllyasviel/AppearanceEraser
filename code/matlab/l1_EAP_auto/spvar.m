function [M] = spvar(image, label)
% [M] = spvariation(image)
% Usage:
%   - For each superpixel, get a pixel that is closet to it in color
%     construct a matrix to calculate the total variation of these pixels
% Input:
%   - image: original image
%   - label: super-pixel label for each pixel
% Output:
%   - M: generated matrix (sparse)

image = double(image);
width = size(image, 2); height = size(image, 1); pixel_num = height * width;

sp_num = length(unique(label));
r = image(:,:,1); g = image(:,:,2); b = image(:,:,3);
rep_index = zeros(sp_num, 1);

for i = 1 : sp_num
    index = find(label == i);
    index_color = [r(index) g(index) b(index)];
    avg_color = mean(index_color, 1);
    index_color = [r(index) - avg_color(1) g(index) - avg_color(2) b(index) - avg_color(3)];
    temp = sum(index_color.^2.0, 2);
    [~, min_index] = min(temp);
    rep_index(i) = index(min_index);
end

pair = nchoosek(rep_index, 2);
temp_1 = pair(:,1)'; temp_2 = pair(:,2)'; pair_num = length(temp_1);
row = [1:pair_num 1:pair_num]; col = [temp_1 temp_2];
val = [ones(1, pair_num) -1 * ones(1,pair_num)];

row_1 = row + length(row) / 2; col_1 = col + pixel_num;
row_2 = row_1 + length(row) / 2; col_2 = col_1 + pixel_num;

final_row = [row;row_1;row_2];
final_col = [col;col_1;col_2];
final_val = [val;val;val];

M = sparse(final_row, final_col, final_val, length(row) / 2 * 3, pixel_num*3);



