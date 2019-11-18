=========
Changelog
=========

This document records all notable changes to 
`CRIkit2 <https://github.com/CCampJr/CRIkit2>`_.

This project adheres to `PEP 440 -- Version Identification 
and Dependency Specification <https://www.python.org/dev/peps/pep-0440/>`_.

0.2.2 ()
--------

- Added a calculate Anscombe parameters function (calc_anscombe_parameters) to crikit.preprocess.standardize
    -   Added an associated GUI dialog for calculating based on NRB and Dark spectra (Preprocess>Standardize submenu)
    -   Note: you will need to perform Dark subtraction before performing the Anscombe transform (though the calculation of parameters can handle either scenario)
    -   Added unittest for calculation function (not the GUI itself)
    -   Added Jupyter Notebook (Calculating Anscombe Parameters.ipynb) to demonstrate use of calc_anscombe_parameters

0.2.1 (19-09-17)
------------------

-   New toolbar ribbon setup scheme and default
-   New kkrelation and hilbertfft function
    -   Select axis
    -   Performs on N-dimensional arrays (not limited to 1- or 2D)
    -   Removed pyFFTW support
    -   Set min values
    -   Set value to set Inf's and NaN's
    -   Note: Does consume more RAM during computation (user may iteratively apply)

-   New KramersKronig incorporating new kkrelation/hilbertfft features
    -   Does not iterate through data, which can require a lot more memory
    
-   New padding function pad_edge_mean
    -   Pads along specified axis with edge values
    -   Edge values can be a mean of n neighboring values as well
    -   Now the default padding function for hilbert and kkrelation

-   Tweaks and bug fixes
    -   Fixed sign error in PhaseErrorCorrectALS that mainly affected real part of spectra

0.2.0 (19-05-23)
----------------

-   Initial version