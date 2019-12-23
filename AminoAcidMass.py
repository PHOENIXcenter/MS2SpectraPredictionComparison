# -*- coding: utf-8 -*-
from numpy import *
from numpy import linalg as la

def pearSim(inA,inB):
	return 0.5+0.5*corrcoef(inA,inB,rowvar=0)[0][1]

mass_H = 1.0078
mass_H2O = 18.0106
mass_NH3 = 17.0265
mass_N_terminus = 1.0078
mass_C_terminus = 17.0027
mass_CO = 27.9949

mass_AA = {
		   'A': 71.03711, # 0
		   'R': 156.10111, # 1
		   'N': 114.04293, # 2
		   'D': 115.02694, # 3
		   #~ 'C': 103.00919, # 4
		   'Cmod': 160.03065, # C(+57.02)
		   #~ 'Cmod': 161.01919, # C(+58.01) # orbi
		   'E': 129.04259, # 5
		   'Q': 128.05858, # 6
		   'G': 57.02146, # 7
		   'H': 137.05891, # 8
		   'I': 113.08406, # 9
		   'L': 113.08406, # 10
		   'K': 128.09496, # 11
		   'M': 131.04049, # 12
		   'Mmod': 147.0354,
		   'F': 147.06841, # 13
		   'P': 97.05276, # 14
		   'S': 87.03203, # 15
		   'T': 101.04768, # 16
		   'W': 186.07931, # 17
		   'Y': 163.06333, # 18
		   'V': 99.06841, # 19
		  }