#!/usr/bin/python3

import argparse
import matplotlib.pyplot as plt
import numpy as np

# 

class points():
    
    def __init__(self, x=[0,1,2], y=[3,4,5]):
        self.x = np.array(x)
        self.y = np.array(y)

class schematic():

    def __init__(self):


        pass

    def draw(self):
        plt.show()

    def test(self):
        o = op()
        o.draw()
        pass

class segment():

    def __init__(self, edges=points([0,0],[1,1])):
        
        self.edges = edges
        pass

    def draw(self, fig = None):
        if fig is None:
            fig = plt.figure()
        plt.figure(1)
        print(self.edges.x)
        plt.plot(self.edges.x, self.edges.y, 'o-')
        
        
    

class polygon:
    def __init__(self, xy=points([0,0]),
                 form=points([0,1,2],[3,4,5])):
        self.xy = xy
        self.form = points(form.x.tolist()+[form.x.tolist()[0]],
                            form.y.tolist()+[form.y.tolist()[0]])
        self.loc = self.move(self.xy)
        pass

    def move(self, xy=points([0,0])):
        #self.form.x = self.form.x + xy.x
        #self.form.y = self.form.y + xy.y
        
        return points(self.form.x + xy.x, self.form.y + xy.y)
    
    def draw(self, fig=None):
        if fig is None:
            fig = plt.figure()

        plt.figure(fig)
        plt.plot(self.loc.x, self.loc.y)
        
        return fig
    
class op():

    def __init__(self, xy=points([0],[0]),
                 rot=0,
                 mir=(False,False),
                 scale=1):
        self.xy = xy
        self.rot = rot
        self.mir = mir
        self.scale = scale
        self.forms = [polygon(xy=self.xy,
                               form=points([0,0,1], [0,1,0.5])),
                      segment(points([-0.5, 0], [0.75, 0.75])),
                      segment(points([-0.5, 0], [0.25, 0.25])),
                      segment(points([ 1, 1.5], [0.5, 0.5]))]
        

    def draw(self):
        for form in self.forms:
            form.draw(fig=1)
            
    def define():
        pass
        
    

def main():
    # test
    sch = schematic()
    sch.test()
    sch.draw()
                       
                       
if __name__ == "__main__":
    # 
    main()
