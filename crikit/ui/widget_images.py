"""
Visualization Widgets (crikit.ui.widget_images)
=======================================================

widgetColorMath : Mathematical operations on raw data leading to color \
    images

widgetBWImg : Grayscale imagery

widgetSglColor : Single-color imagery

widgetCompositeColor : Composite-color imagery

_mplWin : Matplotlib window container


"""

import sys as _sys
import numpy as _np

# Generic imports for QT-based programs
from PyQt5.QtWidgets import (QApplication as _QApplication,
                             QWidget as _QWidget,
                             QSizePolicy as _QSizePolicy,
                             QColorDialog as _QColorDialog,
                             QHBoxLayout as _QHBoxLayout)

import PyQt5.QtCore as _QtCore

# Import from Designer-based GUI
from crikit.ui.qt_SglColorImage import Ui_Form as Ui_SglColorImage_Form
from crikit.ui.qt_ColorMath import Ui_Form as Ui_ColorMath_Form
from crikit.ui.qt_BWImage import Ui_Form as Ui_BWImage_Form
from crikit.ui.qt_CompositeColor import Ui_Form as Ui_CompositeColor_Form
#from crikit.ui.widget_mpl import MplCanvas as _MplCanvas
from sciplot.ui.widget_mpl import MplCanvas as _MplCanvas

# NEW
from crikit.ui.qt_GrayScaleImgInfoBar import Ui_formWidgetGrayScaleImgInfoBar as Ui_GrayImgInfoBar
from crikit.ui.qt_ColorModeSetting import Ui_Form as Ui_ColorModeSetting
from crikit.ui.qt_BlankLayout import Ui_Form as Ui_Blank
from crikit.ui.qt_PopSpectrumGS import Ui_Form as Ui_PopSpectrumGS
from crikit.ui.qt_ImageGainMath import Ui_Form as Ui_ImageGainMath

# Generic imports for MPL-incorporation
import matplotlib as _mpl
import matplotlib.cm as _mpl_cm
import sciplot as _sciplot
#import matplotlib.pyplot as _plt

_mpl.use('Qt5Agg')
_mpl.rcParams['font.family'] = 'sans-serif'
_mpl.rcParams['font.size'] = 10
#import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as _NavigationToolbar)

from crikit.ui.classes_ui import BW, SingleColor, CompositeColor


class widgetColorMath(_QWidget):
    """
    Contains information about what mathematical operations are possible for \
    taking raw HSI data and converting it to grayscale/color.

    Software Info
    --------------

    Original Python branch: Feb 16 2015

    author: ("Charles H Camp Jr")

    email: ("charles.camp@nist.gov")

    version: ("16.03.14")
    """
    OPERATION_STRINGS = ['','+','-','*','/','Peak b/w troughs','SUM']
    OPERATION_FREQ_COUNT = [1, 2, 2, 2,2, 3, 2]
    COND_TYPE_STRINGS = ['>','<','=','<=','>=']

    def __init__(self, parent = None):
        super(widgetColorMath, self).__init__(parent) ### EDIT ###
        self.ui = Ui_ColorMath_Form() ### EDIT ###
        self.ui.setupUi(self)     ### EDIT ###

        self.ui.comboBoxCondOps.addItem('OFF')

        for item in widgetColorMath.OPERATION_STRINGS:
            self.ui.comboBoxOperations.addItem(item)
            self.ui.comboBoxCondOps.addItem(item)

        for item in widgetColorMath.COND_TYPE_STRINGS:
            self.ui.comboBoxCondInEquality.addItem(item)

        self.ui.comboBoxOperations.currentIndexChanged.connect(self.operationchange)
        self.ui.comboBoxCondOps.currentIndexChanged.connect(self.condOpsChange)

    def condOpsChange(self):
        index = self.ui.comboBoxCondOps.currentIndex()

        if index == 0:
            num_freq = 0
        else:
            num_freq = widgetColorMath.OPERATION_FREQ_COUNT[index-1]

        self.ui.pushButtonCondFreq1.setEnabled(False)
        self.ui.pushButtonCondFreq2.setEnabled(False)
        self.ui.pushButtonCondFreq3.setEnabled(False)
        self.ui.comboBoxCondInEquality.setEnabled(False)
        self.ui.spinBoxInEquality.setEnabled(False)

        if num_freq >= 1:
            self.ui.pushButtonCondFreq1.setEnabled(True)
            self.ui.comboBoxCondInEquality.setEnabled(True)
            self.ui.spinBoxInEquality.setEnabled(True)
        if num_freq >= 2:
            self.ui.pushButtonCondFreq2.setEnabled(True)
        if num_freq >= 3:
            self.ui.pushButtonCondFreq3.setEnabled(True)

    def operationchange(self):
        index = self.ui.comboBoxOperations.currentIndex()

        num_freq = widgetColorMath.OPERATION_FREQ_COUNT[index]

        self.ui.pushButtonOpFreq1.setEnabled(False)
        self.ui.pushButtonOpFreq2.setEnabled(False)
        self.ui.pushButtonOpFreq3.setEnabled(False)

        if num_freq >= 1:
            self.ui.pushButtonOpFreq1.setEnabled(True)
        if num_freq >= 2:
            self.ui.pushButtonOpFreq2.setEnabled(True)
        if num_freq >= 3:
            self.ui.pushButtonOpFreq3.setEnabled(True)

class widgetImageGainMath(_QWidget):
    """
    Panel that controle image gain and applies math
    """
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)
        self.ui = Ui_ImageGainMath()
        self.ui.setupUi(self)

class widgetPopSpectrumGS(_QWidget):
    """ 
    Panel that let's user pop the current image, an average spectrum,
    or a grayscale image to SciPlot
    """
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)
        self.ui = Ui_PopSpectrumGS()
        self.ui.setupUi(self)

class widgetGrayScaleInfoBar(_QWidget):
    """
    Grayscale image info bar
    """
    def __init__(self, parent = None, **kwargs):
        super().__init__(parent)
        self.ui = Ui_GrayImgInfoBar()
        self.ui.setupUi(self)

class widgetColorMode(_QWidget):
    """
    Color mode selector
    """
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)
        self.ui = Ui_ColorModeSetting()
        self.ui.setupUi(self)

        # Get all MPL named colors
        color_list = ['red', 'green', 'blue', 'magenta', 'cyan', 'yellow', 
                      'black', 'white', 'CUSTOM']
        color_list.extend(sorted(set(_mpl.colors.cnames.keys()) - set(color_list)))
        self.ui.comboBoxBGColor.addItems(color_list)
        self.ui.comboBoxFGColor.addItems(color_list)
        self.ui.comboBoxBGColor.setCurrentIndex(color_list.index('black'))
        # Get all mpl colormaps and set combo box
        list_of_colormaps = sorted(_mpl_cm.datad.keys())
        self.ui.comboBoxColormap.addItems(list_of_colormaps)

        # Set default colormap to 'gray'
        idx = self.ui.comboBoxColormap.findText('gray')
        self.ui.comboBoxColormap.setCurrentIndex(idx)

class widgetBWImg(_QWidget):
    """
    Grayscale image widget
    """
    def __init__(self, parent = None, **kwargs):
        super().__init__(parent)
        self.win = Ui_Blank()
        self.win.setupUi(self)
        self.win.gridLayout.setEnabled(False)
        
        self._img_defaults = {'showcbar': True, 'axison': True}

        self.gsinfo = widgetGrayScaleInfoBar(parent=self)
        
        self.colormode = widgetColorMode(parent=self)
        self.colormode.ui.comboBoxColorMode.setCurrentIndex(1)
        self.colormode.ui.comboBoxColormap.setVisible(True)
        self.colormode.ui.labelColormap.setVisible(True)
        self.colormode.ui.comboBoxFGColor.setVisible(False)
        self.colormode.ui.comboBoxBGColor.setVisible(False)
        self.colormode.ui.comboBoxColorMode.setVisible(False)
        self.colormode.ui.labelBGColor.setVisible(False)
        self.colormode.ui.labelFGColor.setVisible(False)
        self.colormode.ui.labelColorMode.setVisible(False)

        self.popimage = widgetPopSpectrumGS(parent=self)
        self.popimage.ui.pushButtonGSPop.setVisible(False)

        self.ui = self.gsinfo.ui  # Alias

        self.win.horizLayout = _QHBoxLayout()
        self.win.horizLayout.setContentsMargins(2,2,2,2)

        self.win.verticalLayout.insertLayout(0, self.win.horizLayout)
        
        self.win.horizLayout.insertWidget(0, self.gsinfo, _QtCore.Qt.AlignHCenter)
        self.win.horizLayout.insertWidget(0, self.colormode, _QtCore.Qt.AlignBottom)

        # Initialize underlying data
        self.initData()
        self.external_plots = []

        # Stand-in image data
        self.data.grayscaleimage = _np.dot(_np.ones([100,1]),_np.linspace(1,100,100)[None,:])
        self.data.set_x(_np.linspace(1,400,self.data.xlen))
        self.data.set_y(_np.linspace(1,400,self.data.ylen))
        
        # Calculate extent of image
        winextent = (self.data.x.min(), self.data.x.max(), self.data.y.min(), self.data.y.max())

        # MPL canvas
        self.mpl = _MplCanvas(**kwargs)
        self.mpl.cbar = None  # Monkey patch on a cbar object
        
        # Create stand-image plot
        self.createImg(img=self.data.image, xunits=self.data.xunits,
                       yunits=self.data.yunits,
                       extent=winextent,
                       cmap=self.colormode.ui.comboBoxColormap.currentText())
        self.mpl.fig.tight_layout()
        
        # Insert canvas widget into this widget
        self.win.verticalLayout.insertWidget(0,self.mpl,_QtCore.Qt.AlignCenter)
        self.win.verticalLayout.insertWidget(0,self.popimage,_QtCore.Qt.AlignCenter)
        self.win.verticalLayout.insertWidget(0,self.mpl.toolbar, _QtCore.Qt.AlignHCenter)

        # # SIGNAL & SLOTS
        self.ui.checkBoxFixed.stateChanged.connect(self.checkBoxFixed)
        self.ui.checkBoxRemOutliers.stateChanged.connect(self.checkBoxRemOutliers)
        self.ui.spinBoxStdDevs.editingFinished.connect(self.checkBoxRemOutliers)
        
        # New
        self.ui.comboBoxAboveMax.currentIndexChanged.connect(self.comboBoxCompress)
        self.ui.comboBoxBelowMin.currentIndexChanged.connect(self.comboBoxCompress)
        self.ui.spinBoxMax.editingFinished.connect(self.spinBoxMinMaxSet)
        self.ui.spinBoxMin.editingFinished.connect(self.spinBoxMinMaxSet)
        self.colormode.ui.comboBoxColormap.currentIndexChanged.connect(self.checkBoxFixed)
        self.popimage.ui.pushButtonPop.pressed.connect(lambda: self.createImg_Ext(img=self.data.image,
                                                      cmap=self.colormode.ui.comboBoxColormap.currentText(),
                                                      showcbar=True,
                                                      extent=self.data.winextent,
                                                      xunits=self.data.xunits,
                                                      yunits=self.data.yunits))
    def initData(self):
        """
        (Re)-initialize self.data
        """
        self.data = BW()

    def createImg_Ext(self, img, xunits = None, yunits = None,
                  extent = None, showcbar = True, axison = True,
                  cmap = _mpl.cm.gray):
        """
        Create new figure window and show image of img
        """

        self.external_plots.append(_sciplot.main(parent=self))
        self.external_plots[-1].imshow(img, x_label=xunits, y_label=yunits, 
                      cmap=cmap, cbar=showcbar, extent=extent)

    def createImg(self, img, xunits = None, yunits = None,
                  extent = None, cmap = _mpl.cm.gray):
        self.mpl.ax.clear()
        self.mpl.img = self.mpl.ax.imshow(img, interpolation = 'none',
                                          extent = extent, cmap = cmap, 
                                          origin='lower')
        if xunits is not None:
            self.mpl.ax.xaxis.set_label_text(xunits)
        if yunits is not None:
            self.mpl.ax.yaxis.set_label_text(yunits)

        if self._img_defaults['axison'] == False:
            self.mpl.ax.set_axis_off()

        # print(self.mpl.cbar)
        if self.mpl.cbar is not None:
            self.mpl.cbar.remove()
            self.mpl.cbar = None
        if self._img_defaults['showcbar'] == True:
            self.mpl.cbar = self.mpl.fig.colorbar(self.mpl.img)

        if self.ui.checkBoxFixed.isChecked() == False:
            self.ui.spinBoxMax.setValue(self.data.maxer)
            self.ui.spinBoxMin.setValue(self.data.minner)
           
    def spinBoxMinMaxSet(self):
        try:
            self.data.setmin = self.ui.spinBoxMin.value()
            self.data.setmax = self.ui.spinBoxMax.value()
            self.ui.checkBoxFixed.setChecked(True)
            
            # Spin-Box call from Outlier-related widgets?
            if ((self.sender() == self.ui.checkBoxRemOutliers) |
                (self.sender() == self.ui.spinBoxStdDevs)):
                pass
            else:  # Max-min set manually
                self.ui.checkBoxRemOutliers.setChecked(False)

            self.createImg(img=self.data.image, xunits=self.data.xunits,
                           yunits=self.data.yunits,
                           extent=self.data.winextent,
                           cmap=self.colormode.ui.comboBoxColormap.currentText())
            self.mpl.draw()

        except:
            print('Error in spinBoxMinMaxSet')

    def checkBoxRemOutliers(self):
        """
        """
        if self.ui.checkBoxRemOutliers.isChecked() == False:
            pass
        else:
            new_max = self.data.mean + self.ui.spinBoxStdDevs.value()* \
                      self.data.std
            new_min = self.data.mean - self.ui.spinBoxStdDevs.value()* \
                      self.data.std
            self.ui.spinBoxMax.setValue(new_max)
            self.ui.spinBoxMin.setValue(new_min)
            self.spinBoxMinMaxSet()
           
        self.createImg(img=self.data.image, xunits=self.data.xunits,
                       yunits=self.data.yunits,
                       extent=self.data.winextent, 
                       cmap=self.colormode.ui.comboBoxColormap.currentText())
        self.mpl.draw()

    def checkBoxFixed(self):
        """
        See if the min and max are identified as being fixed by
        checkbox
        """

        # See if there is a min and max in the textBrowsers

        if self.ui.checkBoxFixed.isChecked() == True:  # Checked
            try:
                self.data.setmin = self.ui.spinBoxMin.value()
                self.data.setmax = self.ui.spinBoxMax.value()
                if self.ui.comboBoxAboveMax.currentIndex() == 0:
                    self.data.compress_high = False
                else:
                    self.data.compress_high = True
                if self.ui.comboBoxBelowMin.currentIndex() == 0:
                    self.data.compress_low = False
                else:
                    self.data.compress_low = True
            except:
                pass
        else:
            self.data.setmin = None
            self.data.setmax = None
            self.data.compress_low = None
            self.data.compress_high = None
            self.ui.checkBoxRemOutliers.setChecked(False)

        self.createImg(img=self.data.image, xunits=self.data.xunits,
                       yunits=self.data.yunits,
                       extent=self.data.winextent, 
                       cmap=self.colormode.ui.comboBoxColormap.currentText())
        self.mpl.draw()

    def comboBoxCompress(self):
        """
        See if compression is activated via the comboBoxAboveMax
        """
        if self.ui.comboBoxAboveMax.currentIndex() == 0:
            self.data.compress_high = False
        else:
            self.data.compress_high = True

        if self.ui.comboBoxBelowMin.currentIndex() == 0:
            self.data.compress_low = False
        else:
            self.data.compress_low = True

        self.createImg(img=self.data.image, xunits=self.data.xunits,
                       yunits=self.data.yunits,
                       extent=self.data.winextent,
                       cmap=self.colormode.ui.comboBoxColormap.currentText())
        self.mpl.draw()

class widgetSglColor_new(widgetBWImg):
    """
    Single-color widget
    """
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)
        self._img_defaults = {'showcbar': False, 'axison': True}
        self.initData()
        self.data.grayscaleimage = _np.dot(_np.ones([100,1]),_np.linspace(1,100,100)[None,:])
        self.data.set_x(_np.linspace(1,400,self.data.xlen))
        self.data.set_y(_np.linspace(1,400,self.data.ylen))
        self.changeColor()
        self.colormode.setMaximumHeight(130)
        
        self.math = widgetImageGainMath(parent=self)
        self.win.verticalLayout.insertWidget(3, self.math)

        # Disconnect colormap-related (from BW parent)
        self.colormode.ui.comboBoxColormap.currentIndexChanged.disconnect()
        
        self.colormode.ui.comboBoxColorMode.setCurrentIndex(0)
        self.colormode.ui.comboBoxColormap.setVisible(False)
        self.colormode.ui.labelColormap.setVisible(False)
        self.colormode.ui.comboBoxFGColor.setVisible(True)
        self.colormode.ui.comboBoxBGColor.setVisible(True)
        self.colormode.ui.comboBoxColorMode.setVisible(False)
        self.colormode.ui.labelBGColor.setVisible(True)
        self.colormode.ui.labelFGColor.setVisible(True)
        self.colormode.ui.labelColorMode.setVisible(True)

        self.colormode.ui.comboBoxFGColor.currentIndexChanged.connect(self.changeColor)
        self.colormode.ui.comboBoxBGColor.currentIndexChanged.connect(self.changeColor)
        self.math.ui.spinBoxGain.valueChanged.connect(self.applyGain)
        self.math.ui.pushButtonGain1.pressed.connect(self.gain1)
        self.math.ui.checkBoxDisable.stateChanged.connect(self.disabled)

        self.popimage.ui.pushButtonGSPop.setVisible(True)
        try:
            self.popimage.ui.pushButtonPop.pressed.disconnect()
        except:
            pass
        self.popimage.ui.pushButtonPop.pressed.connect(lambda: self.createImg_Ext(img = self.data.image,
                                                                                  showcbar=False,
                                                                                  extent=self.data.winextent, 
                                                                                  xunits=self.data.xunits,
                                                                                  yunits=self.data.yunits))
        
        try:
            self.popimage.ui.pushButtonGSPop.pressed.disconnect()
        except:
            pass
        self.popimage.ui.pushButtonGSPop.pressed.connect(lambda: self.createImg_Ext(img = self.data.imageGS,
                                                                                    showcbar=True,
                                                                                    extent=self.data.winextent,
                                                                                    xunits=self.data.xunits,
                                                                                    yunits=self.data.yunits))

    def initData(self):
        """
        (Re)-initialize self.data
        """
        self.data = SingleColor()
        
        
    def changeColor(self):
        # try:
        
        if self.sender() == self.colormode.ui.comboBoxFGColor:
            color_str = self.colormode.ui.comboBoxFGColor.currentText()
            if color_str == 'CUSTOM':
                color = _QColorDialog.getColor().getRgb()
                color = [round(color[0]/255,2), round(color[1]/255,2), round(color[2]/255,2)]

                self.data.colormap = color

            else:
                self.data.colormap = _mpl.colors.to_rgb(_mpl.colors.cnames[color_str])

        elif self.sender() == self.colormode.ui.comboBoxBGColor:
            bgcolor_str = self.colormode.ui.comboBoxBGColor.currentText()
            if bgcolor_str == 'CUSTOM':
                bgcolor = _QColorDialog.getColor().getRgb()
                bgcolor = [round(bgcolor[0]/255,2), round(bgcolor[1]/255,2), round(bgcolor[2]/255,2)]

                self.data.bgcolor = bgcolor

            else:
                self.data.bgcolor = _mpl.colors.to_rgb(_mpl.colors.cnames[bgcolor_str])
        
        self.createImg(img = self.data.image, xunits = self.data.xunits,
                                yunits = self.data.yunits,
                                extent = self.data.winextent)
        self.mpl.draw()
        
    def applyGain(self):
        self.data.setgain = self.math.ui.spinBoxGain.value()
        self.changeColor()
        if self.data.setgain == 0.0:
            self.math.ui.checkBoxDisable.setChecked(True)
        else:
            self.math.ui.checkBoxDisable.setChecked(False)

    def gain1(self):
        self.math.ui.spinBoxGain.setValue(1.0)

    def disabled(self):
        if self.math.ui.checkBoxDisable.isChecked():
            self.math.ui.spinBoxGain.setValue(0.0)
        else:
            self.math.ui.spinBoxGain.setValue(1.0)

class widgetCompositeColor(_QWidget):
    def __init__(self, sgl_color_widget_list = None, parent = None, **kwargs):
        super(widgetCompositeColor, self).__init__(parent)
        ## Double check the spellings
        self._img_defaults = {'showcbar':False, 'axison':True}
        self.ui = Ui_CompositeColor_Form()
        self.ui.setupUi(self)

        # Initialize underlying data
        self.initData(sgl_color_widget_list)

        # Create stand-in image data
        self.data.grayscaleimage = _np.dot(_np.ones([100,1]),_np.linspace(1,100,100)[None,:])
        self.data.set_x(_np.linspace(1,400,self.data.xlen))
        self.data.set_y(_np.linspace(1,400,self.data.ylen))
        winextent = (self.data.x.min(), self.data.x.max(), self.data.y.min(), self.data.y.max())

        # Instantiate mpl widget
        self.mpl = _MplCanvas(**kwargs)
        self.mpl.cbar = None  # Monkey patch on a cbar object

        # Create stand-in image data
        self.createImg(img = self.data.image, xunits = self.data.xunits,
                              yunits = self.data.yunits,
                              extent = winextent)
        self.mpl.fig.tight_layout()

        # Insert mpl widget into this widget
        self.ui.verticalLayout.insertWidget(0,self.mpl,_QtCore.Qt.AlignHCenter)
        self.ui.verticalLayout.insertWidget(0,self.mpl.toolbar, _QtCore.Qt.AlignHCenter)

        # SIGNALS & SLOTS
        self.ui.checkBoxFixed.stateChanged.connect(self.checkBoxFixed)
        self.ui.checkBoxCompress.stateChanged.connect(self.checkBoxCompress)
        self.ui.checkBoxRemOutliers.stateChanged.connect(self.checkBoxRemOutliers)
        self.ui.spinBoxStdDevs.valueChanged.connect(self.spinBoxOutliersChanged)

        #self.ui.lineEditMin.editingFinished.connect(self.textEditMinMaxSet)
        #self.ui.lineEditMax.editingFinished.connect(self.textEditMinMaxSet)

    def initData(self, sgl_color_widget_list):
        """
        (Re)-initialize self.data
        """

        if sgl_color_widget_list is None:
            self.data = CompositeColor()
        else:
            temp = []
            for count in sgl_color_widget_list:
                temp.append(count.data)

            self.data = CompositeColor(temp)

    def createImg(self, img, xunits = None, yunits = None,
                  extent = None,
                  cmap = _mpl.cm.gray):
        self.mpl.ax.clear()
        self.mpl.img = self.mpl.ax.imshow(img, interpolation = 'none',
                                      extent = extent, cmap = cmap, origin='lower')
        if xunits is not None:
            self.mpl.ax.xaxis.set_label_text(xunits)
        if yunits is not None:
            self.mpl.ax.yaxis.set_label_text(yunits)

        if self._img_defaults['axison'] == False:
            self.mpl.ax.set_axis_off()

        if self.mpl.cbar is not None:
                self.mpl.cbar.remove()
        if self._img_defaults['showcbar'] == True:
            self.mpl.cbar = self.mpl.fig.colorbar(self.mpl.img)


    def spinBoxOutliersChanged(self):
        self.checkBoxRemOutliers()

    def checkBoxRemOutliers(self):
        """
        """
        if self.ui.checkBoxRemOutliers.isChecked() == False:
            pass
        else:
            pass
        self.createImg(img = self.data.image, xunits = self.data.xunits,
                              yunits = self.data.yunits,
                              extent = self.data.winextent)
        self.mpl.draw()

    def checkBoxFixed(self):
        """
        See if the min and max are identified as being fixed by
        checkbox
        """

        # See if there is a min and max in the textBrowsers

        len_min = len(self.ui.lineEditMin.text())
        len_max = len(self.ui.lineEditMax.text())

        if self.ui.checkBoxFixed.isChecked() == True:  # Checked
            if len_min > 0 and len_max > 0:
                try:
                    self.data.setmin = float(self.ui.lineEditMin.text())
                    self.data.setmax = float(self.ui.lineEditMax.text())
                    if self.ui.checkBoxCompress.isChecked() == False:
                        self.data.compress = False
                    else:
                        self.data.compress = True
                except:
                    pass
            else:
                pass
        else:
            self.data.setmin = None
            self.data.setmax = None
            self.data.compress = None

        self.createImg(img = self.data.image, xunits = self.data.xunits,
                              yunits = self.data.yunits,
                              extent = self.data.winextent)
        self.mpl.draw()

    def checkBoxCompress(self):
        """
        See if compression is activated via the checkbox_4
        """

        if self.ui.checkBoxCompress.isChecked() == False:
            self.data.compress = False
        else:
            self.data.compress = True

        self.createImg(img = self.data.image, xunits = self.data.xunits,
                              yunits = self.data.yunits,
                              extent = self.data.winextent)
        self.mpl.draw()

class _mplWin:
    def __init__(self, parent = None):
        self.fig = None
        self.ax = None
        self.canvas = None
        self.img = None
        self.cbar = None
        self.toolbar = None

    def useToolBar(self, use=True):
        if use is True:
            self.toolbar = _NavigationToolbar(self.canvas, None,
                                                  coordinates = True)


if __name__ == '__main__':

    app = _QApplication(_sys.argv)
    app.setStyle('Cleanlooks')

    # winBWImg = widgetBWImg()
    # winBWImg.setWindowTitle('BW Image')
    # winBWImg.show()
    
    winSglColor = widgetSglColor_new()
    winSglColor.setWindowTitle('Single Color')
    winSglColor.show()
    
    
    # winColorMath = widgetColorMath()
    # winColorMath.setWindowTitle('Color Math')
    
    # winCompositeColor = widgetCompositeColor(sgl_color_widget_list=[winSglColor])
    # winCompositeColor.setWindowTitle('Composite Color')
    
    # Final stuff
    # winColorMath.show()
    
    # winCompositeColor.show()

    _sys.exit(app.exec_())