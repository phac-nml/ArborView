Test data is located: W:\Projects\DAAD\GSP_Datasets\ComparisonWindowVisualization\CC1

Deployed as a static page at http://daad.pages.cscscience.ca/ArborView/

Contains a library for converting SVG files to PNG files
https://gist.github.com/rokotyan/0556f8facbaf344507cdc45dc3622177


Technical Note:
The popup menu was previously not working in fullscreen mode due to the #top-layer tag being on top of it. However appending the menu to the div that was on the toplayer has solved the issue. Secondary note when positioning divs with absolute values it is better to use the offset{X,Y} cords as they correspond to the view box you are in .