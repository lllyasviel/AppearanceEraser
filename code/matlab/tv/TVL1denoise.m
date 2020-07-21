% TVL1denoise - TV-L1 image denoising with the primal-dual algorithm.
%
% Function denoises an image using the TV-L1 model optimized with a primal-dual
% algorithm; this works best for impulse noise. For more details, see
%   A. Mordvintsev: ROF and TV-L1 denoising with Primal-Dual algorithm,
%   http://znah.net/rof-and-tv-l1-denoising-with-primal-dual-algorithm.html
% and
%   Chambolle et al. An introduction to Total Variation for Image Analysis, 2009. <hal-00437581>
%   https://hal.archives-ouvertes.fr/hal-00437581/document
%
% Usage:
%    newim = TVL1denoise(im, lambda, niter)
%
% Arguments:
%    im          -  Image to be processed
%    lambda      -  Regularization parameter controlling the amount
%                   of denoising; smaller values imply more aggressive
%                   denoising which tends to produce more smoothed results.
%    niter       -  Number of iterations. If omitted or empty defaults
%                   to 100
%
% Returns:
%    newim       -  Denoised image with pixel values in [0 1].

% Copyright (c) 2016 Manolis Lourakis (lourakis **at** ics forth gr)
% Institute of Computer Science,
% Foundation for Research & Technology - Hellas
% Heraklion, Crete, Greece.
% http://www.ics.forth.gr/
%
% Permission is hereby granted, free of charge, to any person obtaining a copy
% of this software and associated documentation files (the "Software"), to deal
% in the Software without restriction, subject to the following conditions:
%
% The above copyright notice and this permission notice shall be included in
% all copies or substantial portions of the Software.
%
% The Software is provided "as is", without warranty of any kind.
%
% Modified by ToS2P (the Team of Style2Paints).
% for non-commercial ussage only.
%

function newim = TVL1denoise(im, lambda, niter)

  if(nargin<3) || isempty(niter)
    niter=100;
  end

  L2=8.0;
  tau=0.02;
  sigma=1.0/(L2*tau);
  theta=1.0;
  lt=lambda*tau;

  [height, width, channel]=size(im); 
  unew=zeros(height, width, channel);
  p=zeros(height, width, channel, 2);
  d=zeros(height, width, channel);
  ux=zeros(height, width, channel);
  uy=zeros(height, width, channel);
  
  mx=max(im(:));
  nim=double(im)/double(mx);
  u=nim;

  p(:, :, :, 1)=u(:, [2:width, width], :) - u;
  p(:, :, :, 2)=u([2:height, height], :, :) - u;

  for k=1:niter
    ux=u(:, [2:width, width], :) - u;
    uy=u([2:height, height], :, :) - u;
    p=p + sigma*cat(4, ux, uy);
    normep=max(1, sqrt(p(:, :, :, 1).^2 + p(:, :, :, 2).^2)); 
    p(:, :, :, 1)=p(:, :, :, 1)./normep;
    p(:, :, :, 2)=p(:, :, :, 2)./normep;
    div=[p([1:height-1], :, :, 2); zeros(1, width, channel)] - [zeros(1, width, channel); p([1:height-1], :, :, 2)];
    div=[p(:, [1:width-1], :, 1)  zeros(height, 1, channel)] - [zeros(height, 1, channel)  p(:, [1:width-1], :, 1)] + div;
    v=u + tau*div;
    unew=(v-lt).*(v-nim>lt) + (v+lt).*(v-nim<-lt) + nim.*(abs(v-nim)<=lt);
    u=unew + theta*(unew-u);
  end

  newim=u;
