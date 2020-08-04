#include "mex.h"
#include <cmath>

inline int sub_to_index(int x, int y, int h){
	int index = x * h + y;
	return x * h  + y;
}

inline void swap(float& x1, float& x2){
	float temp = x1;
	x1 = x2;
	x2 = temp;
}

double MaxGrad(float x1, float y1, float x2, float y2, double* grad_matrix, int h, int w)
{
  const bool steep = (fabs(y2 - y1) > fabs(x2 - x1));
  double max_grad = -1e7;
  if(steep)
  {
    swap(x1, y1);
    swap(x2, y2);
  }
 
  if(x1 > x2)
  {
    swap(x1, x2);
    swap(y1, y2);
  }
 
  const float dx = x2 - x1;
  const float dy = fabs(y2 - y1);
 
  float error = dx / 2.0f;
  const int ystep = (y1 < y2) ? 1 : -1;
  int y = (int)y1;
 
  const int maxX = (int)x2;
 
  for(int x=(int)x1; x<maxX; x++)
  {
    if(steep)
    {
        float grad = grad_matrix[sub_to_index(y, x, h)];
        max_grad = max_grad > fabs(grad) ? max_grad : fabs(grad);
    }
    else
    {
        float grad = grad_matrix[sub_to_index(x,y,h)];
        max_grad = max_grad > fabs(grad) ? max_grad : fabs(grad);
    }
 
    error -= dy;
    if(error < 0)
    {
        y += ystep;
        error += dx;
    }
  }
  return max_grad;
}

void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[]){
	// M = wingrad(grad, pair_1, pair_2)
	double* grad = (double*)(mxGetData(prhs[0]));
	size_t grad_cols = mxGetN(prhs[0]);
	size_t grad_rows = mxGetM(prhs[0]);
	double* pair_1 = (double*)(mxGetData(prhs[1]));
	double* pair_2 = (double*)(mxGetData(prhs[2]));
	size_t pair_cols = mxGetN(prhs[1]);
	double * val = new double[pair_cols];
	plhs[0] = mxCreateDoubleMatrix(pair_cols,1,mxREAL);
	double* outMatrix = (double*)mxGetPr(plhs[0]);
	for(int i = 0;i < pair_cols;i++){
		int x1 = (int)pair_1[i] / grad_rows;
		int y1 = (int)pair_1[i] % grad_rows;
		int x2 = (int)pair_2[i] / grad_rows;
		int y2 = (int)pair_2[i] % grad_rows;
		outMatrix[i] = MaxGrad(x1, y1, x2, y2, grad, grad_rows, grad_cols);
	}
}

