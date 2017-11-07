from __future__ import absolute_import
from __future__ import division
from past.utils import old_div
import matplotlib.pyplot as plt
import numpy as np
from .smart_time import smart_time

def update_hov(sim):

    sim.fig.suptitle(smart_time(sim.time))
    if sim.Nx > 1:
        sim.hov_h[:,:,sim.hov_count] = sim.soln.h[:,0,:-1]
        x = old_div(sim.x,1e3)
    else:
        sim.hov_h[:,:,sim.hov_count] = sim.soln.h[0,:,:-1] 
        x = old_div(sim.y,1e3)
    sim.hov_count += 1

