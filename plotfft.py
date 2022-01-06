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

#dir1="ORIG"
#dir1="W-1"
i1=300
i2=400
dir1="DISC"
i1=200
i2=300


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8,8))


def analytical(nn):
  Lx=4    
  qv=0.645
  dV = 2*qv
  rho1=1
  rho2=1
  alpha1=rho1/(rho1+rho2)
  alpha2=rho2/(rho1+rho2)
  B=9e-3
  from math import pi,sqrt
  kx = 2 * pi * nn/Lx 
  sigma2 = kx**2*(alpha1*alpha2*dV**2 - 2*B**2/(rho1 + rho2) )
  return sqrt(sigma2)


dt=2e-3

for nn in range(1,17):

  ax.cla()
  ax.grid(True)
  ax.set_ylabel(r"$\langle A(v_y) \rangle_y$")
  ax.set_xlabel(r"Time")
  
  
  amp = np.loadtxt(join(dir1,("%d.txt" % nn)))
  xx = dt*(np.arange(len(amp)) + 1)  
  ax.plot(xx,amp,marker="o")
  
  #ax.plot(xx[i1:i2],amp[i1:i2],ls='None',marker='x')
  from math import log,e
  pf,cov = np.polyfit(xx[i1:i2],np.log(amp[i1:i2]),1,cov=True)
  p = np.poly1d(pf)
  err = np.sqrt(np.diag(cov))
  print("FIT ", pf[0])
  ax.plot(xx[i1:i2],e**p(xx[i1:i2]),ls='None', marker="x",  label=r"fit (%.2f $\pm$ %.3f)" % (pf[0],err[0]) )
  ax.set_title("Mode %d, analytical %e" % (nn,analytical(nn)))
  ax.set_yscale("log")
  
  ax.legend()
  plt.show()
  
   
  fig.canvas.draw()
  plt.draw()
    
    
  plt.tight_layout()	
    
  newfn = join(dir1,("amp%d.png" % nn)) 
  print("file saved %s " % newfn)
  plt.savefig(newfn)
