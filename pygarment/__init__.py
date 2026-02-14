"""
    A Python library for building parametric sewing pattern programs
"""

# Add NvidiaWarp-GarmentCode to sys.path if not already installed
import os as _os
import sys as _sys
_warp_dir = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), '..', 'NvidiaWarp-GarmentCode')
_warp_dir = _os.path.abspath(_warp_dir)
if _os.path.isdir(_warp_dir) and _warp_dir not in _sys.path:
    _sys.path.insert(0, _warp_dir)

# Building blocks
from pygarment.garmentcode.component import Component
from pygarment.garmentcode.panel import Panel
from pygarment.garmentcode.edge import Edge, CircleEdge, CurveEdge, EdgeSequence
from pygarment.garmentcode.connector import Stitches
from pygarment.garmentcode.interface import Interface
from pygarment.garmentcode.edge_factory import EdgeSeqFactory
from pygarment.garmentcode.edge_factory import CircleEdgeFactory
from pygarment.garmentcode.edge_factory import EdgeFactory
from pygarment.garmentcode.edge_factory import CurveEdgeFactory


# Operations
import pygarment.garmentcode.operators as ops
import pygarment.garmentcode.utils as utils

# Parameter support
from pygarment.garmentcode.params import BodyParametrizationBase, DesignSampler

# Errors
from pygarment.pattern.core import EmptyPatternError

