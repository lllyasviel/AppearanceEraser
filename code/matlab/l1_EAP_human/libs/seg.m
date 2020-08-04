function label = seg(image, sigma, min_size, K, varargin)
% Segment given image into super-pixels.
% Input:
%   image:     [M * N * 3, REQ] images to be segmented
%   sigma:     [REQ] standard deviation of Gaussian smooth kernel
%   min_size:  [REQ] minimum number of pixels in super-pixels
%   K:         [REQ] number of super-pixels
%   varargin:
%       - region [] not used here.
% Output:
%   label:     [M * N] super-pixel label for each pixel
if(length(varargin) == 0)
    label = segment(double(image), sigma, min_size, K);
else
    region = varargin{1};
    label = segment(double(image), sigma, min_size, K, region);
end

