"""Evaluation module to calculate Accuracy, Precision, and Recall."""

import json
from pathlib import Path

class Evaluator:
    def __init__(self, ground_truth_path: Path | str):
        self.ground_truth = {}
        path = Path(ground_truth_path)
        
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                self.ground_truth = json.load(f)
        else:
            print(f"[Cảnh báo] Không tìm thấy file Ground Truth tại {path}. Sẽ bỏ qua đánh giá.")
        
        # Ma trận nhầm lẫn (Confusion Matrix)
        self.true_positives = 0  # AI đoán có xe (occupied), thực tế có xe
        self.false_positives = 0 # AI đoán có xe, thực tế trống (Báo động giả)
        self.true_negatives = 0  # AI đoán trống (free), thực tế trống
        self.false_negatives = 0 # AI đoán trống, thực tế có xe (Bỏ lọt / Sai nguy hiểm)
        self.total_evaluated = 0

    def evaluate_frame(self, frame_index: int, predicted_slots: list):
        """So sánh dự đoán của AI với đáp án thật tại frame cụ thể."""
        frame_key = f"frame_{frame_index}"
        if frame_key not in self.ground_truth:
            return # Nếu frame này không được đánh dấu trong file JSON thì bỏ qua

        gt_slots = self.ground_truth[frame_key]
        
        for slot in predicted_slots:
            slot_id = slot.slot_id
            if slot_id not in gt_slots:
                continue
            
            actual_status = gt_slots[slot_id]
            predicted_status = slot.status
            
            # Đếm các trường hợp
            if predicted_status == "occupied" and actual_status == "occupied":
                self.true_positives += 1
            elif predicted_status == "occupied" and actual_status == "free":
                self.false_positives += 1
            elif predicted_status == "free" and actual_status == "free":
                self.true_negatives += 1
            elif predicted_status == "free" and actual_status == "occupied":
                self.false_negatives += 1
            
            self.total_evaluated += 1

    def print_report(self):
        """Tính toán và in báo cáo ra Terminal."""
        print("\n" + "="*50)
        print(" BÁO CÁO KẾT QUẢ ĐÁNH GIÁ (EVALUATION REPORT) ")
        print("="*50)
        
        if self.total_evaluated == 0:
            print("Chưa đánh giá được ô đỗ nào. Hãy kiểm tra lại file Ground Truth.")
            print("="*50 + "\n")
            return

        accuracy = (self.true_positives + self.true_negatives) / self.total_evaluated
        
        precision = 0.0
        if (self.true_positives + self.false_positives) > 0:
            precision = self.true_positives / (self.true_positives + self.false_positives)
        
        recall = 0.0
        if (self.true_positives + self.false_negatives) > 0:
            recall = self.true_positives / (self.true_positives + self.false_negatives)

        print(f"Tổng số mẫu đã kiểm tra: {self.total_evaluated}")
        print(f"1. Độ chính xác (Accuracy) : {accuracy * 100:.2f}%")
        print(f"2. Độ chuẩn xác (Precision): {precision * 100:.2f}% (Tỷ lệ báo 'Có xe' chính xác)")
        print(f"3. Độ bao phủ (Recall)    : {recall * 100:.2f}% (Tỷ lệ bắt trúng số xe thực tế)")
        print("="*50 + "\n")