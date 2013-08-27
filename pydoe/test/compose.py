#!/usr/bin/env python
from pydoe import compose
parameters = {
              'num_nodes': { 'values' : [ 512 ] },
              'num_tasks': { 'values' : [ 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500 ] },
              'num_dims': { 'values' : [ 1, 2, 3, 4 ] },
              'slack': { 'values' : [ 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ] },
              'cov': { 'values' :[ 0.00, 0.15, 0.30, 0.45, 0.60, 0.75, 0.90, 1.05 ] },
              'split': { 'values' :[ 1, 2, 3, 4, 5, 6, 7, 8 ] }}
probspecs = compose(
    'file:/home/marklee/Projects/doescripts2/oadir/oa.64.9.8.2.txt', parameters)
print probspecs
