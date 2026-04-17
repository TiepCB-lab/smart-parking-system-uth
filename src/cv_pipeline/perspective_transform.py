"""Perspective transform (Bird-eye view) helpers."""

from __future__ import annotations

import cv2
import numpy as np

def calculate_perspective_matrix(src_points: list[tuple[int, int]], width: int, height: int) -> np.ndarray:
    """
    Tính toán ma trận biến đổi phối cảnh.
    
    Args:
        src_points: 4 điểm (x, y) đánh dấu khu vực bãi đỗ xe trên camera 
                    (Thứ tự: Trái-trên, Phải-trên, Phải-dưới, Trái-dưới).
        width: Chiều rộng mong muốn của ảnh sau khi biến đổi.
        height: Chiều cao mong muốn của ảnh sau khi biến đổi.
        
    Returns:
        Ma trận biến đổi 3x3.
    """
    pts_src = np.float32(src_points)
    pts_dst = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    
    matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)
    return matrix

def apply_bird_eye_view(frame: np.ndarray, matrix: np.ndarray, width: int, height: int) -> np.ndarray:
    """
    Áp dụng ma trận để 'kéo phẳng' khung hình.
    """
    warped_frame = cv2.warpPerspective(frame, matrix, (width, height))
    return warped_frame