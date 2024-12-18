# Camera Calibration

## Pin-hole Camera Model

The relationship between 3D world coordinates and 2D image coordinates:

```math
\begin{bmatrix} u\\\ v\\\ 1 \end{bmatrix} = K [R | t] \begin{bmatrix} x\\\ y\\\ z\\\ 1 \end{bmatrix}
```

Where:  
* $`K`$: Intrinsic matrix, $`K = \begin{bmatrix}f_u & s & c_u \\ 0 & f_v & c_v \\ 0 & 0 & 1 \end{bmatrix},`$
* $`[R | t]`$: Extrinsic parameters (rotation and translation)
* $`f_u`$, $`f_v`$: Focal lengths
* $`c_u`$, $`c_v`$: Principal point
* $`s`$: Skew coefficient

## Steps for Calibration:
1. Capture multiple images of a **chessboard** pattern.  
2. Detect corners using **OpenCV's `findChessboardCorners`**.  
3. Estimate camera parameters using **`cv2.calibrateCamera`**.  
4. Validate reprojection error.  