# https://github.com/enthought/comtypes/issues/334#issue-1323791612

from comtypes.automation import VARIANT
from comtypes import npsupport
import numpy as np

array = np.zeros((1,1),npsupport.VARIANT_dtype, order='F')
array.flat = VARIANT("123")

