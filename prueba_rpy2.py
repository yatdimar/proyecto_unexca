from rpy2.robjects import r
import numpy as np
from rpy2.robjects import numpy2ri

numpy2ri.activate()
    
x = r.matrix(np.array(range(9)), nrow=3, ncol=3)
r.assign('x', x)
r('print(x)')