# The EAP Image Smoothing Toolkit

The EAP Toolkit is a set of image smoothing tools developed by the Team of Style2Paints (ToS2P), aimed at finding a solution to decompose texture or illumination from images.

The uniqueness of EAP is that it dynamically finds a set of "erasing" positions to help better pattern decompostion. Please refer to our [Project Page](https://lllyasviel.github.io/AppearanceEraser/) for more details.

The codes are written in Matlab. I have spent one and a half months to convert those codes to python but finally failed. **It is impossible to implement these tools in python.** This is mainly because the *sparse optimization* in python is very weak.

# Tools

## Naive total variation smoothing

Input files:

    ./code/matlab/tv/input.png

Output files:

    ./code/matlab/tv/output.png

Command:

    matlab ./code/matlab/tv/run.m

## Total variation smoothing with human erasing mask

Input files:

    ./code/matlab/tv_EAP_human/input.png
    ./code/matlab/tv_EAP_human/mask.png

Output files:

    ./code/matlab/tv_EAP_human/output.png

Command:

    matlab ./code/matlab/tv_EAP_human/run.m

## Total variation smoothing with EAP automatic erasing

Input files:

    ./code/matlab/tv_EAP_auto/input.png

Output files:

    ./code/matlab/tv_EAP_auto/output.png
    ./code/matlab/tv_EAP_auto/mask.png

Command:

    matlab ./code/matlab/tv_EAP_auto/run.m

## Relative total variation smoothing

Input files:

    ./code/matlab/rtv/input.png

Output files:

    ./code/matlab/rtv/output.png

Command:

    matlab ./code/matlab/rtv/run.m

## Relative total variation smoothing with human erasing mask

Input files:

    ./code/matlab/rtv_EAP_human/input.png
    ./code/matlab/rtv_EAP_human/mask.png

Output files:

    ./code/matlab/rtv_EAP_human/output.png

Command:

    matlab ./code/matlab/rtv_EAP_human/run.m

## Relative total variation smoothing with EAP automatic erasing

Input files:

    ./code/matlab/rtv_EAP_auto/input.png

Output files:

    ./code/matlab/rtv_EAP_auto/output.png
    ./code/matlab/rtv_EAP_auto/mask.png

Command:

    matlab ./code/matlab/rtv_EAP_auto/run.m

## L0 smoothing

Input files:

    ./code/matlab/l0/input.png

Output files:

    ./code/matlab/l0/output.png

Command:

    matlab ./code/matlab/l0/run.m

## L0 smoothing with human erasing mask

Input files:

    ./code/matlab/l0_EAP_human/input.png
    ./code/matlab/l0_EAP_human/mask.png

Output files:

    ./code/matlab/l0_EAP_human/output.png

Command:

    matlab ./code/matlab/l0_EAP_human/run.m

## L0 smoothing with EAP automatic erasing

Input files:

    ./code/matlab/l0_EAP_auto/input.png

Output files:

    ./code/matlab/l0_EAP_auto/output.png
    ./code/matlab/l0_EAP_auto/mask.png

Command:

    matlab ./code/matlab/l0_EAP_auto/run.m

## L1 smoothing

Input files:

    ./code/matlab/L1/input.png

Output files:

    ./code/matlab/L1/output.png

Command:

    matlab ./code/matlab/L1/run.m

## L1 smoothing with human erasing mask

Input files:

    ./code/matlab/L1_EAP_human/input.png
    ./code/matlab/L1_EAP_human/mask.png

Output files:

    ./code/matlab/L1_EAP_human/output.png

Command:

    matlab ./code/matlab/L1_EAP_human/run.m

## L1 smoothing with EAP automatic erasing

Input files:

    ./code/matlab/L1_EAP_auto/input.png

Output files:

    ./code/matlab/L1_EAP_auto/output.png
    ./code/matlab/L1_EAP_auto/mask.png

Command:

    matlab ./code/matlab/L1_EAP_auto/run.m

# Application

Our applications are from many third-party projects. Please refer to their original sites for more details.

## Illumination editing

    Illumination decomposition for material recoloring with consistent interreflections
    http://graphics.berkeley.edu/papers/Carroll-IDM-2011-08/index.html

## Texture editing

    Structure Extraction from Texture via Relative Total Variation
    http://www.cse.cuhk.edu.hk/~leojia/projects/texturesep/

## Color editing

    Decomposing Images into Layers via RGB-space Geometry
    https://cragl.cs.gmu.edu/singleimage/

# Citation

If you use this code for your research, please cite our paper:

    @InProceedings{EAP2020,
    author={Lvmin Zhang, Chengze Li, Yi JI, Chunping Liu, and Tien-tsin Wong}, 
    booktitle={European Conference on Computer Vision (ECCV)}, 
    title={Erasing Appearance Preservation in Optimization-based Smoothing}, 
    year={2020}, 
    }

# 中文社区

我们有一个除了技术什么东西都聊的以技术交流为主的宇宙超一流二次元相关技术交流吹水群“纸片协会”。如果你一次加群失败，可以多次尝试。

    纸片协会总舵：184467946
