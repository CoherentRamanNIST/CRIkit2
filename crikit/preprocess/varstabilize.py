# -*- coding: utf-8 -*-
"""
Variance Stabilization Utilities (CRIKIT.utils.varstabil)
=======================================================

    gen_anscombe_forward : generalized forward Anscombe transformation

    gen_anscombe_inverse_closed_form : closed-form approximation of the
        exact unbiased inverse of Generalized Anscombe variance-stabilizing
        transformation

    gen_anscombe_exact_unbiased : exact unbiased inverse of Generalized
        Anscombe variance-stabilizing

Notes
-----
This software is a direct translation (with minor alterations) of the
original MATLAB software created by Alessandro Foi and Markku Mäkitalo
(Tampere University of Technology - 2011-2012). Please cite the references
below if using this software. http://www.cs.tut.fi/~foi/

Citation Refs
------------------
[1] M. Mäkitalo and A. Foi, "Optimal inversion of the generalized Anscombe
    transformation for Poisson-Gaussian noise", IEEE Trans. Image Process.,
    doi:10.1109/TIP.2012.2202675

[2] J.L. Starck, F. Murtagh, and A. Bijaoui, Image  Processing  and  Data
    Analysis, Cambridge University Press, Cambridge, 1998)

Software Info
--------------

Original Python branch: Feb 16 2015\n
\n
@author: ("Charles H Camp Jr")\n
@email: ("charles.camp@nist.gov")\n
@date: Tue Sep  1 15:55:41 2015\n
@version: ("1.1")\n
"""

import numpy as _np
import numexpr as _ne
import sys as _sys
import os as _os

RESOURCE_DIR = './'

if _os.path.exists((_os.path.abspath('./maths/resources/'))):
    resource_dir = './maths/resources/'
elif _os.path.exists((_os.path.abspath('./process/maths/resources/'))):
    resource_dir = './process/maths/resources/'
elif _os.path.exists((_os.path.abspath('./crikit/process/maths/resources/'))):
    resource_dir = './crikit/process/maths/resources/'
elif _os.path.exists((_os.path.abspath('../crikit/process/maths/resources/'))):
    resource_dir = '../crikit/process/maths/resources/'
elif _os.path.exists(_os.path.abspath('../process/maths/resources/')):
    resource_dir = '../process/maths/resources/'
elif _os.path.exists((_os.path.abspath(RESOURCE_DIR))):
    resource_dir = RESOURCE_DIR
else:
    print('Cannot find resource directory')

def gen_anscombe_forward(signal, gauss_std, gauss_mean = 0, poisson_multi = 1):
    """
    Applies the generalized Anscombe variance-stabilization transform
    assuming a mixed Poisson-Gaussian noise model as:

    signal = poisson_multi*Poisson{signal0} + Gauss{gauss_mean, gauss_std},

    where Poisson{} and Gauss{} are generalized descriptions of Poisson and
    Gaussian noise.

    Parameters
    ----------
    signal : ndarray
        Noisy signal (1-,2-,3D)

    gauss_std : float, int
        Standard deviation of Gaussian noise

    (poisson_multi) : float, int (default = 1)
        Effectively a multiplier that scales the effect of the Poisson
        noise

    (gauss_mean) : float, int (default = 0)
        Mean Gaussian noise level

    Returns
    -------
    fsignal : ndarray (matched to signal shape)
        "Anscombe-transformed" signal with an approximate unity
        standard deviation/variance (~ 1)

    Note
    ----
    This software is a direct translation (with minor alterations) of the
    original MATLAB software created by Alessandro Foi and Markku Mäkitalo
    (Tampere University of Technology - 2011-2012). Please cite the references
    below if using this software. http://www.cs.tut.fi/~foi/

    References
    ----------
    [1] J.L. Starck, F. Murtagh, and A. Bijaoui, Image  Processing  and
    Data Analysis, Cambridge University Press, Cambridge, 1998)

    Software Info
    --------------
    Original Python branch: Feb 16 2015

    @author: ("Charles H Camp Jr")\n
    @email: ("charles.camp@nist.gov")\n
    @date: ("Sep 2 2015")\n
    @version: ("1.1")\n
    """

    SMALL_VAL = 1

#    fsignal = 2/poisson_multi * _np.sqrt(_np.fmax(SMALL_VAL,poisson_multi*signal +
#                                    (3/8)*poisson_multi**2 +
#                                    gauss_std**2 -
#                                    poisson_multi*gauss_mean))
    fsignal = _ne.evaluate('2/poisson_multi * sqrt(where(poisson_multi*signal + (3/8)*poisson_multi**2 +\
                            gauss_std**2 - poisson_multi*gauss_mean > SMALL_VAL,\
                            poisson_multi*signal + (3/8)*poisson_multi**2 +\
                            gauss_std**2 - poisson_multi*gauss_mean, SMALL_VAL))')
    #fsignal = 2/poisson_multi * _np.sqrt(_np.fmax(SMALL_VAL,fsignal))
    return fsignal

def gen_anscombe_inverse_closed_form(fsignal, gauss_std, gauss_mean = 0,
                                     poisson_multi = 1):
    """
    Applies a closed-form approximation of the exact unbiased inverse of the
    generalized Anscombe variance-stabilizing transformation assuming a
    mixed Poisson-Gaussian noise model as:

    signal = poisson_multi*Poisson{signal0} + Gauss{gauss_mean, gauss_std},

    where Poisson{} and Gauss{} are generalized descriptions of Poisson and
    Gaussian noise.

    Parameters
    ----------
    fsignal : ndarray
        Forward Anscombe-transformed noisy signal (1-,2-,3D)

    gauss_std : float, int
        Standard deviation of Gaussian noise

    (poisson_multi) : float, int (default = 1)
        Effectively a multiplier that scales the effect of the Poisson
        noise

    (gauss_mean) : float, int (default = 0)
        Mean Gaussian noise level

    Returns
    -------
    signal : ndarray (matched to signal shape)
        Inverse Anscombe-transformed signal with mixed Gaussian-Poisson
        noise

    Note
    ----
    This software is a direct translation (with minor alterations) of the
    original MATLAB software created by Alessandro Foi and Markku Mäkitalo
    (Tampere University of Technology - 2011-2012). Please cite the references
    below if using this software. http://www.cs.tut.fi/~foi/

    References
    ------------------
    [1] M. Mäkitalo and A. Foi, "Optimal inversion of the generalized Anscombe
    transformation for Poisson-Gaussian noise", IEEE Trans. Image Process.,
    doi:10.1109/TIP.2012.2202675

    [2] J.L. Starck, F. Murtagh, and A. Bijaoui, Image  Processing  and  Data
    Analysis, Cambridge University Press, Cambridge, 1998)

    Software Info
    --------------
    Original Python branch: Feb 16 2015

    @author: ("Charles H Camp Jr")\n
    @email: ("charles.camp@nist.gov")\n
    @date: ("Sep 2 2015")\n
    @version: ("1.1")\n
    """

    SMALL_VAL = 0

    gauss_std = gauss_std/poisson_multi

    signal = _ne.evaluate('poisson_multi*where((fsignal/2)**2 + 1/4*sqrt(3/2)*fsignal**-1 -\
                    (11/8)*fsignal**-2 + 5/8*sqrt(3/2)*fsignal**-3 -\
                    (1/8) - gauss_std**2 > SMALL_VAL, (fsignal/2)**2 + 1/4*sqrt(3/2)*fsignal**-1 -\
                    (11/8)*fsignal**-2 + 5/8*sqrt(3/2)*fsignal**-3 -\
                    (1/8) - gauss_std**2, SMALL_VAL) + gauss_mean')

#    signal = (fsignal/2)**2 + 1/4*_np.sqrt(3/2)*fsignal**-1 -\
#                    (11/8)*fsignal**-2 + 5/8*_np.sqrt(3/2)*fsignal**-3 -\
#                    (1/8) - gauss_std**2

    #signal = _np.fmax(_np.zeros(signal.shape)+SMALL_VAL,signal)

#    signal=signal*poisson_multi

#    signal=signal+gauss_mean
    return signal

def gen_anscombe_inverse_exact_unbiased(fsignal, gauss_std, gauss_mean = 0,
                                        poisson_multi = 1):
    """
    Applies an exact, unbiased inverse of the generalized Anscombe
    variance-stabilizing transformation assuming a mixed Poisson-Gaussian
    noise model as:

    signal = poisson_multi*Poisson{signal0} + Gauss{gauss_mean, gauss_std},

    where Poisson{} and Gauss{} are generalized descriptions of Poisson and
    Gaussian noise.

    Parameters
    ----------
    fsignal : ndarray
        Forward Anscombe-transformed noisy signal (1-,2-,3D)

    gauss_std : float, int
        Standard deviation of Gaussian noise

    (poisson_multi) : float, int (default = 1)
        Effectively a multiplier that scales the effect of the Poisson
        noise

    (gauss_mean) : float, int (default = 0)
        Mean Gaussian noise level

    Returns
    -------
    signal : ndarray (matched to signal shape)
        Inverse Anscombe-transformed signal with mixed Gaussian-Poisson
        noise

    Note
    ----
    This software is a direct translation (with minor alterations) of the
    original MATLAB software created by Alessandro Foi and Markku Mäkitalo
    (Tampere University of Technology - 2011-2012). Please cite the references
    below if using this software. http://www.cs.tut.fi/~foi/

    References
    ------------------
    [1] M. Mäkitalo and A. Foi, "Optimal inversion of the generalized Anscombe
    transformation for Poisson-Gaussian noise", IEEE Trans. Image Process.,
    doi:10.1109/TIP.2012.2202675

    [2] J.L. Starck, F. Murtagh, and A. Bijaoui, Image  Processing  and  Data
    Analysis, Cambridge University Press, Cambridge, 1998)

    Software Info
    --------------
    Original Python branch: Feb 16 2015

    @author: ("Charles H Camp Jr")\n
    @email: ("charles.camp@nist.gov")\n
    @date: ("Sep 2 2015")\n
    @version: ("1.1")\n
    """
    from scipy.io import loadmat
    from scipy.interpolate import InterpolatedUnivariateSpline, interp2d

    SMALL_VAL = 0
    
    mat_dict = loadmat(resource_dir + 'GenAnscombe_vectors.mat')
    
    Efzmatrix = _np.squeeze(mat_dict['Efzmatrix'])
    Ez = _np.squeeze(mat_dict['Ez'])
    sigmas = _np.squeeze(mat_dict['sigmas'])

    gauss_std = gauss_std/poisson_multi;


    # interpolate the exact unbiased inverse for the desired gauss_std
    # gauss_std is given as input parameter
    if (gauss_std > _np.max(sigmas)):
        # for very large sigmas, use the exact unbiased inverse of
        # Anscombe modified by a -gauss_std^2 addend
        exact_inverse = anscombe_inverse_exact_unbiased(fsignal) - gauss_std**2

        # this should be necessary, since anscombe_inverse_exact_unbiased(fsignal) is >=0 and gauss_std>=0.
        
        exact_inverse = _np.fmax(_np.zeros(exact_inverse.shape),exact_inverse)

    elif gauss_std > 0:
        # interpolate Efz

        Efz = interp2d(sigmas,Ez,Efzmatrix,kind='linear')(gauss_std,Ez)

        # apply the exact unbiased inverse
        exact_inverse = InterpolatedUnivariateSpline(Efz,Ez,k=1)(fsignal)

        # outside the pre-computed domain, use the exact unbiased inverse
        # of Anscombe modified by a -gauss_std^2 addend
        # (the exact unbiased inverse of Anscombe takes care of asymptotics)
        outside_exact_inverse_domain = fsignal > _np.max(Efz.flatten())
        asymptotic = anscombe_inverse_exact_unbiased(fsignal) - gauss_std**2
        exact_inverse[outside_exact_inverse_domain] = asymptotic[outside_exact_inverse_domain]
        outside_exact_inverse_domain = fsignal < _np.min(Efz);
        exact_inverse[outside_exact_inverse_domain] = 0;
    elif gauss_std == 0:
        # if gauss_std is zero, then use exact unbiased inverse of Anscombe
        # transformation (higher numerical precision)
        exact_inverse = anscombe_inverse_exact_unbiased(fsignal);
    else:  # gauss_std < 0
        raise ValueError('Error: gauss_std must be non-negative!')

    # reverse the initial variable change

    exact_inverse=exact_inverse*poisson_multi;


    exact_inverse=exact_inverse+gauss_mean;

    return exact_inverse

def anscombe_inverse_exact_unbiased(fsignal):
    """
    Applies an exact, unbiased inverse of the Anscombe
    variance-stabilizing transformation assuming a mixed Poisson-Gaussian
    noise model as:

    signal = poisson_multi*Poisson{signal0} + Gauss{gauss_mean, gauss_std},

    where Poisson{} and Gauss{} are generalized descriptions of Poisson and
    Gaussian noise.

    Parameters
    ----------
    fsignal : ndarray
        Forward Anscombe-transformed noisy signal (1-,2-,3D)

    Returns
    -------
    signal : ndarray (matched to signal shape)
        Inverse Anscombe-transformed signal

    Note
    ----
    This software is a direct translation (with minor alterations) of the
    original MATLAB software created by Alessandro Foi and Markku Mäkitalo
    (Tampere University of Technology - 2011-2012). Please cite the references
    below if using this software. http://www.cs.tut.fi/~foi/

    References
    ------------------
    [1] M. Mäkitalo and A. Foi, "On the inversion of the Anscombe
    transformation in low-count Poisson image denoising", Proc. Int.
    Workshop on Local and Non-Local Approx. in Image Process., LNLA 2009,
    Tuusula, Finland, pp. 26-32, August 2009. doi:10.1109/LNLA.2009.5278406

    [2] M. Mäkitalo and A. Foi, "Optimal inversion of the Anscombe
    transformation in low-count Poisson image denoising", IEEE Trans.
    Image Process., vol. 20, no. 1, pp. 99-109, January 2011.
    doi:10.1109/TIP.2010.2056693

    [3] Anscombe, F.J., "The transformation of Poisson, binomial and
    negative-binomial data", Biometrika, vol. 35, no. 3/4, pp. 246-254,
    Dec. 1948.

    Software Info
    --------------
    Original Python branch: Feb 16 2015

    @author: ("Charles H Camp Jr")\n
    @email: ("charles.camp@nist.gov")\n
    @date: ("Jun 28 2015")\n
    @version: ("1.1")\n
    """
    import time

    from scipy.io import loadmat
    from scipy.interpolate import InterpolatedUnivariateSpline

    #mat_dict = loadmat('C:/Users/chc/Documents/Python/CRIkit_develop_bitbucket/crikit/utils/resources/Anscombe_vectors.mat')
    mat_dict = loadmat(resource_dir + 'Anscombe_vectors.mat')    
    
    Efz = mat_dict['Efz']
    Ez = mat_dict['Ez']

    #asymptotic = (fsignal/2)**2 - 1/8;  # asymptotically unbiased inverse [3]
    asymptotic = _ne.evaluate('(fsignal/2)**2 - 1/8')  # asymptotically unbiased inverse [3]

    #start = time.process_time()
    signal = InterpolatedUnivariateSpline(Efz,Ez,k=1)(fsignal)   # exact unbiased inverse [1,2]
    #stop = time.process_time()
    #print(stop-start)

    outside_exact_inverse_domain = fsignal > _np.max(Efz)    # for large values use asymptotically unbiased inverse instead of linear extrapolation of exact unbiased inverse outside of pre-computed domain

    signal[outside_exact_inverse_domain] = asymptotic[outside_exact_inverse_domain];

    outside_exact_inverse_domain = fsignal < 2*_np.sqrt(3/8) # min(Efz(:));

    signal[outside_exact_inverse_domain] = 0;
    return signal
    
if __name__ == '__main__':
    import numpy as np
    import matplotlib as mpl
    mpl.use('Qt5Agg')
    import matplotlib.pyplot as plt
    
    stddev = 20
    gain = 1
    
    x = np.linspace(500,4000,1000)
    y = 10e4*np.exp(-(x-2000)**2/(500**2))
    gnoise = stddev*np.random.randn(x.size)
    ygn = y + gnoise
    ymix = np.random.poisson(y) + gnoise
    ymix_ansc = gen_anscombe_forward(ymix, gauss_std=stddev, poisson_multi=gain)
    y_ansc = gen_anscombe_forward(y, gauss_std=stddev, poisson_multi=gain)
    
    y_inv_ansc = gen_anscombe_inverse_exact_unbiased(y_ansc, gauss_std=stddev, 
                                                     poisson_multi=gain)    
    
    plt.subplot(211)
    plt.plot(x,y)
    plt.hold(True)
    plt.plot(x,ymix)
    plt.title('Signal')
    
    plt.subplot(212)
    plt.plot(x,ymix-y)
    plt.title('Difference')
    
    plt.figure()
    plt.subplot(211)
    plt.plot(x,ymix_ansc)
    plt.plot(x,y_ansc)
    plt.title('Anscombe Transformed')
    
    plt.subplot(212)
    plt.plot(x,ymix_ansc - y_ansc)
    plt.title('Difference')
    
    plt.figure()
    plt.subplot(211)
    plt.plot(x,y_inv_ansc)
    plt.plot(x,y)
    plt.title('Inverse Anscombe Transformed')
    
    plt.subplot(212)
    plt.plot(x,y_inv_ansc - ymix)
    plt.title('Difference')
    
    plt.show()
    