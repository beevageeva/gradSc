import yt 
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import pylab as plt
plt.rc('font', family='serif', size=20)
plt.rcParams['mathtext.fontset'] = "stix"
plt.ion()
# Load the dataset.




from os.path import join


dir1="ORIG"
dir1="W-1"
dir1="DISC"


start=0
end=1000


lmax = 2
import sys

NMIN=1
NMAX=16

amp = np.zeros((NMAX-NMIN+1,end-start+1))

for k in range(start,end+1): 
  print("FILE %d" % k)
  ds = yt.load("%s/16_modes_B_0.009%04d.dat" % (dir1,k))
  mz = ds.domain_dimensions[1]*2**(lmax)
  mx = ds.domain_dimensions[0]*2**(lmax)
  data = ds.covering_grid(level=lmax, left_edge=ds.domain_left_edge,
                                        dims=[mx,mz,1])

  starty=3*mz//8
  endy=5*mz//8
  #midy=mz//2
  #starty=midy-2
  #endy=midy+2 
  arr = data["m2"][:,starty:endy,0]/data["rho"][:,starty:endy,0]

  yf = (np.absolute(np.fft.rfft(arr,axis=0)))/arr.shape[0]  #divide by this for Python FFT
  yf=np.mean(yf,axis=1)
  amp[:,k]=yf[NMIN:NMAX+1]


for ii in range(NMIN,NMAX+1):
  nn= ii-1
  np.savetxt(join(dir1,("%d.txt"%ii)),amp[nn,:])
