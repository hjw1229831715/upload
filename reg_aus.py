import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from pandas import DataFrame,Series
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

filename= "../data/ec/ecpw*.nc"
data1=nc.MFDataset(filename)
data2=nc.Dataset("../data/ec/ec_hur_sfc.nc")
data3=nc.Dataset("../data/ec/pw_ec.nc")
pw=data3.variables["pw"][:,110:123,115:151]
t=data1.variables["t2m"][:,110:123,115:151]

t_a1=t.mean(axis=2)
t_a =t_a1.mean(axis=1)
hur=data2.variables["hur"][:,110:123,115:151]
print(type(hur[0,0,0]))
ed=data2.variables["ed"][:,110:123,115:151]
hur_a1=np.mean(hur,axis=2)
hur_a =np.mean(hur_a1,axis=1)
ed_a1= np.mean(ed, axis=2)
ed_a =np.mean(ed_a1,axis=1)
model = LinearRegression()
plt.figure()
time=np.arange(1979,2018)
month=['Jan','Apr','Jul','Oct']
ymajorFormatter = FormatStrFormatter('%1.1f')
for i in [0,3,6,9] :
 t_a_l = list(t_a[i::12])
 hur_a_l =list(hur_a[i::12])
 ed_a_l =ed_a[i::12]
 t_a_l.extend(hur_a_l)
 j=i/3+1
 ed_a_l=list((ed_a_l).reshape(-1,1))
 train=list(np.reshape(t_a_l,(39,2),order='F'))

 model.fit(train,ed_a_l)
 a = list(model.coef_.reshape(2))
 b= list(model.intercept_)
 print(type(a[0]))
 print(b)
 ed_s=float(a[0])*np.array(t_a_l[0:39])+float(a[1])*np.array(hur_a_l[:])+float(b[0])
## 绘制第一个图
 ax=plt.subplot(2, 2, j)
 plt.plot(time, ed_a_l,color = 'black', label='SVP(real)',linewidth = 1.0, linestyle = '-')
 plt.plot(time, ed_s,color = 'red', label='SVP(simu)',linewidth = 1.0, linestyle = ':')
 plt.xticks([1980, 1990, 2000, 2010, 2017])
 plt.xlim(1979,2017)
 ax.yaxis.set_major_formatter(ymajorFormatter)

 plt.title(month[int(j-1)])
plt.tight_layout()
plt.legend(loc=2, bbox_to_anchor=(-0.55,1.16),markerscale=0.8,mode="horizontal",framealpha=0,ncol=4,fontsize=8,borderaxespad = 0.)
plt.savefig("../pics/aus_reg.png")
plt.show()