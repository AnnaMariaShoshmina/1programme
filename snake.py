      #!/usr/bin/env python3
      #snakefunction
      # -*- coding: utf-8 -*-
  
      import math
      #из библиотеки math, numpy, matplotlib
      import numpy
      import matplotlib.pyplot as mpp
 
        if __name__=='__main__':
            #задай параметры синусоиды
        arguments = numpy.r_[0:200:0.1]
        mpp.plot(
           arguments,
           [math.sin(a) * math.sin(a/20.0) for a in arguments]
       )
      mpp.show() #выведи синусоиду

   
