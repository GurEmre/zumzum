import numpy as np
import os
import matplotlib.pyplot as plt



def DirLocManage(returnchar=False):
    ''' with this segment code is callable from any folder '''
    if os.name=='nt':
        dirChangeCharacter='\\'
    else:
        dirChangeCharacter='/'
    if returnchar==False:
        scriptLoc=__file__
        for i in range(len(scriptLoc)):
            # if '/' in scriptLoc[-i-2:-i]: # in running
            if dirChangeCharacter in scriptLoc[-i-2:-i]: # in debuging
                scriptLoc=scriptLoc[0:-i-2]
                break
        # print('[+] code path',scriptLoc)
        os.chdir(scriptLoc)
    return dirChangeCharacter
    ''' done '''
DirLocManage()

dirs=os.listdir()
npys=[]
for _ in dirs:
    if ".npy" in _:
        npys.append(_)

npysDataList=[]

for c,v in enumerate(npys):
    with open(v,'rb') as f:
        data=np.load(f)
        npysDataList.append(data)
def movingaverage(values,window):
    weights = np.repeat(1.0,window)/window
    smas = np.convolve(values,weights,'valid')
    return smas
""" fig, axs = plt.subplots(ncols=2)
axs[0].plot(npysDataList[0])
axs[0].plot(npysDataList[1])
axs[1].plot(npysDataList[2])
axs[1].plot(npysDataList[3]) """
fig, axs = plt.subplots(ncols=2)
axs[0].plot(movingaverage(np.mean(npysDataList[0],axis=0),300))
axs[0].plot(movingaverage(np.mean(npysDataList[1],axis=0),300))
axs[1].plot(movingaverage(np.mean(npysDataList[2],axis=0),300))
axs[1].plot(movingaverage(np.mean(npysDataList[3],axis=0),300))
axs[0].legend(['BEECLUST','LBA']) 
axs[1].legend(['BEECLUST','LBA']) 
""" fig, axs = plt.subplots(ncols=2)
#plt.title(r'sdfg', fontsize=20)
axs[0].plot(np.mean(npysDataList[0],axis=1))
axs[0].plot(np.mean(npysDataList[1],axis=1))
axs[1].plot(np.mean(npysDataList[2],axis=1))
axs[1].plot(np.mean(npysDataList[3],axis=1))
axs[0].legend(['BEECLUST','LBA']) 
axs[1].legend(['BEECLUST','LBA'])  """
plt.show()
exit(0)

""" with open(docname,'rb') as f:
    x=np.load(f)
print(x)

def movingaverage(values,window):
    weights = np.repeat(1.0,window)/window
    smas = np.convolve(values,weights,'valid')
    return smas
plt.plot(movingaverage(x[0],5), color='blue', linewidth=2)
plt.plot(movingaverage(x[1],5), color='red', linewidth=2)
plt.plot(movingaverage(x[2],5), color='cyan', linewidth=2)
plt.plot(movingaverage(x[3],5), color='black', linewidth=2)
plt.plot(movingaverage(x[4],5), color='darkred', linewidth=2)
plt.plot(movingaverage(x[5],5), color='mistyrose', linewidth=2)
plt.plot(movingaverage(x[6],5), color='saddlebrown', linewidth=2)
plt.plot(movingaverage(x[7],5), color='green', linewidth=2)
plt.plot(movingaverage(x[8],5), color='yellowgreen', linewidth=2)
plt.plot(movingaverage(x[9],5), color='yellow', linewidth=2)
plt.plot(movingaverage(x[10],5), color='pink', linewidth=2)
plt.plot(movingaverage(x[11],5), color='lightblue', linewidth=2)
plt.plot(movingaverage(x[12],5), color='teal', linewidth=2)
plt.plot(movingaverage(x[13],5), color='fuchsia', linewidth=2)
plt.plot(movingaverage(x[14],5), color='slateblue', linewidth=2)
plt.plot(movingaverage(x[15],5), color='slategrey', linewidth=2)
plt.plot(movingaverage(x[16],5), color='tomato', linewidth=2)
plt.plot(movingaverage(x[17],5), color='sandybrown', linewidth=2)
plt.plot(movingaverage(x[18],5), color='darkkhaki', linewidth=2)
plt.plot(movingaverage(x[19],5), color='purple', linewidth=2)
plt.show() """
