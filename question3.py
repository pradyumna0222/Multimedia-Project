# This program performs both frequency sampling and spatial sampling on a color image.
# Frequency sampling is done by applying FFT, filtering low-frequency components.
import numpy as np
from PIL import Image
img = np.array(Image.open("Grevys_Zebra.png").convert("RGB"))
# Frequency Sampling 
def freq_sample_color(img, k):
    H, W, C = img.shape
    out = np.zeros_like(img)
    for ch in range(3): 
        F = np.fft.fftshift(np.fft.fft2(img[..., ch]))
        rr, cc = H // k, W // k
        F_low = np.zeros_like(F)
        F_low[H//2-rr:H//2+rr, W//2-cc:W//2+cc] = \
            F[H//2-rr:H//2+rr, W//2-cc:W//2+cc]
        out[..., ch] = np.abs(np.fft.ifft2(np.fft.ifftshift(F_low)))

    return out.astype(np.uint8)
# Spatial Sampling 
def spatial_sample_color(img, k):
    return img[::k, ::k, :]
# Run for k = 2, 4, 8, 16 
for k in [2, 4, 8, 16]:
    Image.fromarray(freq_sample_color(img, k)).save(f"freq_{k}.png")
    Image.fromarray(spatial_sample_color(img, k)).save(f"spatial_{k}.png")

