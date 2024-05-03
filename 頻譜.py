import numpy as np
import cv2
from numpy.fft import fft2, fftshift

def spectrum(f):
    F=fft2(f)
    Fshift=fftshift(F)
    mag=20*np.log(np.abs (Fshift)+1)
    mag=mag/mag.max()*255.0
    g=np.uint8(mag)
    return g

def phase_spectrum(f):
    F = fft2(f)
    phase = np.angle(F, deg=True)
    phase = np.where(phase < 0, phase + 360, phase)
    phase = (phase * 255 / 360).astype(np.uint8)
    g = np.uint8(np.clip(phase, 0, 255))
    return g

def main():
    img = cv2.imread("regular_gray.jpg",-1)
    magnitude=spectrum(img)
    phase=phase_spectrum(img)
    cv2.imshow("Regular Original Image", img)
    cv2.imshow("Regular Frequency Spectrum", magnitude)
    cv2.imshow("Regular Phase Specrum", phase)
    cv2.imwrite("regular_magnitude.jpg", magnitude)
    cv2.imwrite("regular_phase.jpg", phase)    
    
    img = cv2.imread("irregular_gray.jpg",-1)
    magnitude=spectrum(img)
    phase=phase_spectrum(img)
    cv2.imshow("Irregularl Original Image", img)
    cv2.imshow("Irregularl Frequency Spectrum", magnitude)
    cv2.imshow("Irregularl Phase Specrum", phase)
    cv2.imwrite("irregular_magnitude.jpg", magnitude)
    cv2.imwrite("irregular_phase.jpg", phase)    
    
    img = cv2.imread("randomness_gray.jpg",-1)
    magnitude=spectrum(img)
    phase=phase_spectrum(img)
    cv2.imshow("Randomness Original Image", img)
    cv2.imshow("Randomness Frequency Spectrum", magnitude)
    cv2.imshow("Randomness Phase Specrum", phase)
    cv2.imwrite("randomness_magnitude.jpg", magnitude)
    cv2.imwrite("randomness_phase.jpg", phase)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()