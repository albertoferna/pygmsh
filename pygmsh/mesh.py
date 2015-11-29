# -*- coding: utf8 -*-
#
'''
This class provides a Python interface for the Gmsh scripting language. While
geometry class covers creating geometry this one is going to set meshing parameters
'''


class Mesh(object):

    def __init__(self):
        # For now we only include what is needed for our cases
        # This values are used as defaults
        self.elem_order = 2  # Use quadratic elements as default
        self.algorithm2D = 2  # 1 Meshadapt, 2 Auto, 5 Delaunay, 6 Frontal, 8 Delaunay quads, 9 Packing parallel
        self.smoothing = 3
        self.recombine_all = 0
        self.recombination_algo = 1  # 0 Standard, 1 Blossom
        self._GMSH_CODE = ['\n //Added meshing options']

    def set_algorithm2D(self, algo='auto'):
        if algo=='meshadapt':
            self.algorithm2D = 1
        elif algo=='delaunay':
            self.algorithm2D = 5
        elif algo=='frontal':
            self.algorithm2D = 6
        elif algo=='delaunay quads':
            self.algorithm2D = 8
        elif algo=='packing':
            self.algorithm2D = 9
        else:
            self.algorithm2D = 2

    def get_mesh_options(self):
        self._GMSH_CODE.append('Mesh.Algorithm = %s;' % (self.algorithm2D))
        self._GMSH_CODE.append('Mesh.ElementOrder = %s;' % (self.elem_order))
        self._GMSH_CODE.append('Mesh.Smoothing = %s;' % (self.smoothing))
        self._GMSH_CODE.append('Mesh.RecombineAll = %s;' % (self.recombine_all))
        self._GMSH_CODE.append('Mesh.RecombinationAlgorithm = %s;' % (self.recombination_algo))
        return '\n'.join(self._GMSH_CODE)
