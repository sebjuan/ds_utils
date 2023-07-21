import matplotlib as mpl
from matplotlib.lines import Line2D


ALL_MARKERS = [m for m, func in Line2D.markers.items() if func != 'nothing']

ALL_COLORS = list(mpl.colors.BASE_COLORS.keys())
