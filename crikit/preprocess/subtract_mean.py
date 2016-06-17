# -*- coding: utf-8 -*-
"""
Subtract mean value (optionally, over a range from all spectrum/spectra/hsi)

Created on Thu May 26 14:31:39 2016

@author: chc
"""
if __name__ == '__main__':  # pragma: no cover
    import sys as _sys
    import os as _os
    _sys.path.append(_os.path.abspath('../../'))

import numpy as _np

from crikit.utils.general import find_nearest as _find_nearest


class SubtractMeanOverRange:
    def __init__(self, rng=None):
        if rng is None:
            self.rng = None
        elif len(rng) == 2:
            rng.sort()
            self.rng = _np.arange(rng[0],rng[1])
        else:
            self.rng = rng

    def _calc(self, data, ret_obj):
        if self.rng is None:
            self.rng = _np.arange(data.shape[-1])
        meaner = data[..., self.rng].mean(axis=-1)
        try:
            ret_obj -= meaner[..., None]
        except:
            return False
        else:
            return True


    def transform(self, data):
        """
        Subtract the mean intensity over a pixel range (rng). \
        (Overwrite data).

        Parameters
        ----------
        data : ndarray
            Input data.

        Returns
        -------
        bool
            Returns the success state (True=success)

        """
        success = self._calc(data, ret_obj=data)
        return success

    def calculate(self, data):
        """
        Subtract the mean intensity over a pixel range (rng). \
        (Return copy).

        Parameters
        ----------
        data : ndarray
            Input data.

        Returns
        -------
        ndarray
            Returns data with mean subtracted (or None if fails)

        """
        data_copy = _copy.deepcopy(data)
        success = self._calc(data, ret_obj=data_copy)
        print(success)
        if success:
            return data_copy
        else:
            return None

if __name__ == '__main__':  # pragma: no cover

    from crikit.data.spectrum import Spectrum as _Spectrum
    from crikit.data.spectra import Spectra as _Spectra
    from crikit.data.hsi import Hsi as _Hsi

    import copy as _copy

    x = _np.linspace(0, 100, 10)
    y = _np.linspace(0, 100, 10)
    freq = _np.arange(20)
    data = _np.ones((10, 10, 20))

    hs = _Hsi(data=_copy.deepcopy(data), freq=freq, x=x, y=y)
    spa = _Spectra(data=_copy.deepcopy(data), freq=freq)
    sp = _Spectrum(data=_copy.deepcopy(data)[0, 0, :], freq=freq)

    mean_sub = SubtractMeanOverRange([5, 8])

    print('\n---------TRANSFORM TEST----------\n')
    print('\n3D----------')
    print('Initial mean: {}'.format(hs.data.mean()))
    out = mean_sub.transform(hs.data)
    print('Success?: {}'.format(out))
    print('Final mean: {}\n'.format(hs.data.mean()))

    print('2D----------')
    print('Initial mean: {}'.format(spa.data.mean()))
    out = mean_sub.transform(spa.data)
    print('Success?: {}'.format(out))
    print('Final mean: {}\n'.format(spa.data.mean()))

    print('1D----------')
    print('Initial mean: {}'.format(sp.data.mean()))
    out = mean_sub.transform(sp.data)
    print('Success?: {}'.format(out))
    print('Final mean: {}'.format(sp.data.mean()))

    # NOT-OVERWRITE TEST
    print('\n---------CALCULATE TEST----------\n')

    hs = _Hsi(data=_copy.deepcopy(data), freq=freq, x=x, y=y)
    spa = _Spectra(data=_copy.deepcopy(data)[0, :, :], freq=freq)
    sp = _Spectrum(data=_copy.deepcopy(data)[0, 0, :], freq=freq)

    mean_sub = SubtractMeanOverRange([5, 8])

    print('\n3D----------')
    print('Initial Data Mean: {}'.format(hs.data.mean()))
    out = mean_sub.calculate(hs.data)
    print('Returned Mean: {}'.format(out.mean()))
    print('Final Data Mean: {}'.format(hs.data.mean()))

    print('2D----------')
    print('Initial Data Mean: {}'.format(spa.data.mean()))
    out = mean_sub.calculate(spa.data)
    print('Returned Mean: {}'.format(out.mean()))
    print('Final Data Mean: {}'.format(spa.data.mean()))

    print('1D----------')
    print('Initial Data Mean: {}'.format(sp.data.mean()))
    out = mean_sub.calculate(sp.data)
    print('Returned Mean: {}'.format(out.mean()))
    print('Final Data Mean: {}'.format(sp.data.mean()))
