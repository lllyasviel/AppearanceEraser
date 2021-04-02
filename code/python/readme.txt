# Erasing Appearance Preserving (EAP) Implementation

Here we provide a very readable implementation of EAP using TV smoothing as an example.
Though it only uses TV, its results are pretty good and comparable to some advanced methods like RTV and L0.
The package is also well organized so that anyone can directly obtain visualized results under different configurations within one run.
This code also visualizes all results during iterations.
Finally, this implementation reproduces the P/N position set visualization figures as in main paper.

There are many explanations in the code to help readers understanding.

All required libraries are tested using many different versions. See also 'requirements.txt' for required libraries.

# Basic Usage

Directly run:

    Python3 main.py

This will smooth the sample image using many different configurations.
Please see also the code if you need to custom your own configurations.

# More details

Please refer to line-by-line notes in main.py as well as other files.
