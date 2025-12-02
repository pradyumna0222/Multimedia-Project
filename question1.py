# Added gray, median-cut and octree quantization code
from PIL import Image
import numpy as np
# grey quantization
img = np.array(Image.open('tiger.png').convert('RGB'))
gray = ((img[:,:,0] + img[:,:,1] + img[:,:,2]) // 3).astype('uint8')
Image.fromarray(gray).save('grey.png')
# median-cut quantization
img = Image.open('tiger.png')
q = img.quantize(colors=16, method=Image.MEDIANCUT)
q.save('mediancut.png')
# octree quantization
Image.open('tiger.png').quantize(colors=16, method=Image.FASTOCTREE).save('octree.png')
