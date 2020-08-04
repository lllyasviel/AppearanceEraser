#include <cstdio>
#include <cstdlib>
#include <image.h>
#include <misc.h>
#include <pnmfile.h>
#include "segment-image.h"
#include "mex.h"

void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[]){
    double* input_image = (double*)(mxGetData(prhs[0]));
    const mwSize* image_size = mxGetDimensions(prhs[0]);
    size_t height = image_size[0];
    size_t width = image_size[1];
    size_t dims = mxGetNumberOfDimensions(prhs[0]);

    double sigma = mxGetScalar(prhs[1]);
    double min_size = mxGetScalar(prhs[2]);
    double sp_num = mxGetScalar(prhs[3]);

    int max_pixel_number = (height * width) / (double)sp_num + 20; 

    image<int>* region= new image<int>(width, height);
    region->init(0);
    if(nrhs == 5){
        double * input_region = (double*)(mxGetData(prhs[4]));
        for(int i = 0;i < height;i++){
            for(int j = 0;j < width;j++){
                region->access[i][j] = input_region[i + height * j];
            }
        }
    }


    image<rgb>* new_image = new image<rgb>(width, height);
    for(size_t i = 0;i < height;i++){
        for(size_t j = 0;j < width;j++){
            rgb color;
            color.r = input_image[i + height * (j + width * 0)];
            color.g = input_image[i + height * (j + width * 1)];
            color.b = input_image[i + height * (j + width * 2)];
            new_image->access[i][j] = color;
        }
    }

    int num_ccs; 
    // image<int>* pixel_label = new image<int>(width,height);    
    plhs[0] = mxCreateDoubleMatrix(height,width,mxREAL);
    double* pixel_label = (double*)mxGetPr(plhs[0]);
    segment_image(new_image, sigma, sp_num, min_size, &num_ccs, pixel_label, region, max_pixel_number);
}