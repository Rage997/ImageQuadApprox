# ImageQuadApprox

Approximate images using quadtree i.e. by recursively subdividing the image into four quadrants if some conditions are met. In this case, the split is done whether the image and its mean colour differ in some tolerance.

# References
1. https://estebanhufstedler.com/2020/05/05/image-quadrangulation/
2. https://ieeexplore.ieee.org/document/544569

# TODO
[ ] Solve bug when trying to split an image that can't be splitted
[ ] Visualise the quadtree