# Camera Calibration Cheat Sheet

---

## Pin-hole Camera Model

The relationship between 3D world coordinates \( X_w \) and 2D image coordinates \( x \) is:

$$
x = K [R | t] X_w
$$

Where:  
- \( K \): Intrinsic matrix  
- \( [R | t] \): Extrinsic parameters (rotation and translation)  

---

## Intrinsic Matrix \( K \):

$$
K = 
\begin{bmatrix}
f_x & s & c_x \\
0 & f_y & c_y \\
0 & 0 & 1
\end{bmatrix}
$$

- \( f_x, f_y \): Focal lengths  
- \( c_x, c_y \): Principal point  
- \( s \): Skew coefficient  

---

## Steps for Calibration:
1. Capture multiple images of a **chessboard** pattern.  
2. Detect corners using **OpenCV's `findChessboardCorners`**.  
3. Estimate camera parameters using **`cv2.calibrateCamera`**.  
4. Validate reprojection error.  