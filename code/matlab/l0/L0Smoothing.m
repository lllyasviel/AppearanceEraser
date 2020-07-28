%   Distribution code Version 1.0 -- 09/23/2011 by Jiaya Jia Copyright 2011, The Chinese University of Hong Kong.
%
%   The Code is created based on the method described in the following paper 
%   [1] "Image Smoothing via L0 Gradient Minimization", Li Xu, Cewu Lu, Yi Xu, Jiaya Jia, ACM Transactions on Graphics, 
%   (SIGGRAPH Asia 2011), 2011. 
%
%   Modified by the ToS2P (the Team of Style2Paints).
%   for non-commercial ussage only.
%


function S = L0Smoothing(Im, lambda, kappa)

if ~exist('kappa','var')
    kappa = 2.0;
end
if ~exist('lambda','var')
    lambda = 2e-2;
end
S = im2double(Im);
betamax = 1e5;
fx = [1, -1];
fy = [1; -1];
[N,M,D] = size(Im);
sizeI2D = [N,M];
otfFx = psf2otf(fx,sizeI2D);
otfFy = psf2otf(fy,sizeI2D);
Normin1 = fft2(S);
Denormin2 = abs(otfFx).^2 + abs(otfFy ).^2;
if D>1
    Denormin2 = repmat(Denormin2,[1,1,D]);
end
beta = 2*lambda;
while beta < betamax
    Denormin   = 1 + beta*Denormin2;
    h = [diff(S,1,2), S(:,1,:) - S(:,end,:)];
    v = [diff(S,1,1); S(1,:,:) - S(end,:,:)];
    if D==1
        t = (h.^2+v.^2)<lambda/beta;
    else
        t = sum((h.^2+v.^2),3)<lambda/beta;
        t = repmat(t,[1,1,D]);
    end
    h(t)=0; v(t)=0;
    Normin2 = [h(:,end,:) - h(:, 1,:), -diff(h,1,2)];
    Normin2 = Normin2 + [v(end,:,:) - v(1, :,:); -diff(v,1,1)];
    FS = (Normin1 + beta*fft2(Normin2))./Denormin;
    S = real(ifft2(FS));
    beta = beta*kappa;
    fprintf('.');
end
fprintf('\n');
end
