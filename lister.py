import matplotlib
matplotlib.use('Agg')
import pylab
import matplotlib.pyplot as plt
import numpy as np

winwid = 500

fname = open("C:/Users/Ben WORK ONLY/Desktop/GH repos/RTS ML detect beta/RTS_List.txt", "w+")
gname = open("C:/Users/Ben WORK ONLY/Desktop/GH repos/RTS ML detect beta/WN_List.txt", "w+")

for i in range(0,300):
    for j in range(0,600):
        p = pixel[0:1500, i, j]
        if j < 301:
            fname.write("%d %d\r\n" % (i,j))
        else:
            gname.write("%d %d\r\n" % (i,j))    
 #       for k in range(1,3):
            #winmean = abs(np.mean(p[(k*winwid):((k+1)*winwid)])-np.mean(p[(k-1)*winwid:(k*winwid)]))
 #           if winmean > 1.5*np.std(p):
 #               fname.write("%d %d\r\n" % (i,j))
 #               print(i,j)
 #               print(winmean,np.std(p))
 #               break
 #           else:
 #               if k ==2:
 #                   gname.write("%d %d\r\n" % (i,j))

            
fname.close()
gname.close()
        
        
        
        
#x = np.arange(0,500)

#plt.plot(x,p)