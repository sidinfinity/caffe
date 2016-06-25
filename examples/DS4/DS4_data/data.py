import h5py
import scipy.io
mat = scipy.io.loadmat('DS4.mat')
data= mat['X']
y = mat['y']
te_labels = mat['te_labels']
d = h5py.File('train.h5','w')
d.create_dataset('data',data.shape,data.dtype,data)
d.create_dataset('y',y.shape,y.dtype,y)
e = h5py.File('test.h5','w')
data = mat['test']
e.create_dataset('data',data.shape,data.dtype,data)
e.create_dataset('te_labels',te_labels.shape,te_labels.dtype,te_labels)
