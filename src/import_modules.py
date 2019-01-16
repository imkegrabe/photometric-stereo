# Python modules
import scipy.io as sio
import numpy as np
import matplotlib 
from matplotlib import pyplot as plt
from numpy import dot
from scipy import fftpack as fft
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve
from scipy.io import loadmat
from sys import version_info
from itertools import combinations

from ps_utils import *
from photometric_stereo_functions import *
