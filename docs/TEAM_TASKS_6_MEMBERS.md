# BANG PHAN CONG NHIEM VU CHI TIET CHO NHOM 6 THANH VIEN

> Pham vi du an: he thong Smart Parking theo cau truc 3-layer + CV pipeline trong `src/`.
> Muc tieu phan cong: 100% thanh vien tham gia xu ly ky thuat truc tiep (code, test, tich hop), khong co vai tro chi lam tai lieu.

## 1) Tong quan phan vai theo cau truc project

| Thanh vien | Vai tro chinh | Ownership module/files chinh | Dau ra chinh |
|---|---|---|---|
| TV1 | Lead + Integration + Architecture Guard | `src/app/main.py`, `src/application/use_cases/process_video.py`, `src/application/use_cases/process_multi_camera.py`, `src/domain/interfaces.py` | Luong end-to-end on dinh, tich hop da camera, quy trinh merge/release |
| TV2 | Presentation + UX Demo | `src/presentation/video_controller.py`, `src/presentation/multi_camera_controller.py` | Giao dien/chay demo video va multi-camera ro rang, overlay day du |
| TV3 | CV Core (Preprocess + Foreground) | `src/cv_pipeline/preprocessing.py`, `src/cv_pipeline/background_subtraction.py`, `src/cv_pipeline/thresholding.py`, `src/cv_pipeline/morphology.py` | Detector baseline su dung background subtraction, thong so toi uu |
| TV4 | Slot Logic (Contour/ROI/Classifier) | `src/cv_pipeline/contour_detection.py`, `src/cv_pipeline/slot_extraction.py`, `src/cv_pipeline/classifier.py`, `config/slots.example.json` | Trich xuat slot chinh xac, phan loai occupied/free/unknown, smoothing |
| TV5 | Infrastructure + Data + Repository | `src/infrastructure/opencv/video_reader.py`, `src/infrastructure/repositories/json_slot_repository.py`, `data/`, `models/`, `config/slots.example.json` | Adapter doc video/repository on dinh, bo du lieu/chuan hoa config |
| TV6 | QA + Evaluation + Automation | `src/evaluation/evaluator.py`, test scripts benchmark/end-to-end, regression scenarios | Bo test tu dong, ket qua benchmark, bug reproduction packs |

## 2) Bang nhiem vu chi tiet tung thanh vien

## Thanh vien 1 - Lead/Integration (TV1)

**Muc tieu**
- Dam bao cac layer ket noi dung chuan: Presentation -> Application -> Domain -> Infrastructure/CV pipeline.
- Chot moi hop dong du lieu va luong xu ly chinh.

**Nhiem vu ky thuat chi tiet**
1. Chuan hoa use-case xu ly 1 camera va nhieu camera.
2. Dinh nghia ro interface giua `application` va `cv_pipeline` (input frame, output ket qua slot).
3. Dam bao `main.py` co 2 mode chay: single-video va multi-camera.
4. Viet luong xu ly loi tong quan (video khong mo duoc, file slot khong hop le, camera disconnect).
5. Thiet ke cau hinh runtime co the truyen qua argument hoac file config.
6. Dieu phoi merge theo nhanh tich hop tung tuan, giai quyet xung dot module.

**Deliverables bat buoc**
- 1 phien ban chay thong suot tu `python -m src.app.main` den ket qua occupancy.
- 1 bo integration test scenarios cho luong single va multi-camera.

**KPI/DoD cua TV1**
- Chay on dinh voi it nhat 2 video mau khac nhau.
- Khong con loi import vong lap giua cac layer.
- Tat ca PR lon deu co tieu chi test/kiem tra ro rang.

---

## Thanh vien 2 - Presentation/Controller (TV2)

**Muc tieu**
- Bien ket qua CV thanh giao dien quan sat de demo duoc ngay.

**Nhiem vu ky thuat chi tiet**
1. Hoan thien `video_controller.py`:
	- Chon nguon video, play/pause, frame stepping co ban (neu can).
	- Ve overlay polygon slot, id slot, mau occupied/free.
	- Hien thi thong ke tong so slot trong/da co xe theo frame.
2. Hoan thien `multi_camera_controller.py`:
	- Sap xep layout nhieu camera trong mot cua so.
	- Hien thi thong ke tung camera va tong hop.
3. Dong bo style output de de quan sat khi demo (font/mau/legend nhat quan).
4. Tich hop callback nhan ket qua tu application layer, khong chen logic CV vao presentation.
5. Xu ly truong hop UI khong nhan duoc frame/ket qua (fallback message).

**Deliverables bat buoc**
- Giao dien co overlay ro rang cho single-camera.
- Giao dien co ban cho multi-camera (toi thieu 2 nguon).
- 1 bo config chay demo (tham so input/nguong/mau hien thi) dung lai duoc.

**KPI/DoD cua TV2**
- Toc do hien thi khong giat manh tren may nhom dung demo.
- Mau sac occupied/free khong bi nham trong dieu kien anh sang trung binh.
- Co screenshot/clip ngan cho 2 kịch ban: single va multi-camera.

---

## Thanh vien 3 - CV Core Baseline (TV3)

**Muc tieu**
- Tao baseline detector on dinh dua tren preprocessing + background subtraction.

**Nhiem vu ky thuat chi tiet**
1. Trong `preprocessing.py`:
	- Chuan hoa resize, grayscale, blur (median/gaussian) co tham so.
2. Trong `background_subtraction.py`:
	- Thu nghiem MOG2/KNN.
	- Chuan hoa nguong foreground ratio cho tung slot.
3. Trong `thresholding.py` va `morphology.py`:
	- Bo loc nhieu (opening/closing), loai bo dom nho.
	- Tao helper de thu nghiem nhanh bo tham so.
4. Dua ra bo tham so baseline theo tung dieu kien:
	- Ban ngay, ban toi, camera rung nhe.
5. Danh dau cac case detector yeu va de xuat huong nang cap (YOLO segmentation/custom model).

**Deliverables bat buoc**
- Baseline detector co ham chay va tra ket qua nhat quan.
- Bang tham so khuyen nghi theo it nhat 3 dieu kien video.
- Script benchmark FPS/latency cho baseline detector.

**KPI/DoD cua TV3**
- Pipeline core co the xu ly lien tuc tren video mau ma khong vo frame.
- Ket qua foreground mask du sach de TV4 classifier su dung.
- Cac tham so duoc dua vao config/co constant ro rang, khong hard-code rai rac.

---

## Thanh vien 4 - Slot Extraction + Classification (TV4)

**Muc tieu**
- Bien mask/contour thanh trang thai tung slot de su dung truc tiep trong dashboard/demo.

**Nhiem vu ky thuat chi tiet**
1. `contour_detection.py`:
	- Tach contour vung xe/noise va danh dau do tin cay co ban.
2. `slot_extraction.py`:
	- Cat ROI theo polygon slot tu config.
	- Dam bao dung he toa do khi frame da resize.
3. `classifier.py`:
	- Rule occupied/free dua tren pixel ratio, contour area, va confidence.
	- Them trang thai `unknown` khi ket qua khong chac chan.
4. Xay co che smoothing/debounce theo N frame de giam nhay trang thai.
5. Chuan hoa schema slot:
	- `slot_id`, `polygon`, `camera_id`, `status`, `confidence`, `timestamp`.

**Deliverables bat buoc**
- Module classifier tra ve danh sach slot co status + confidence.
- Co che debounce hoạt dong tren it nhat 1 video nhiễu.
- File mau `config/slots.example.json` co schema ro rang, de sinh `config/slots.json`.

**KPI/DoD cua TV4**
- Trang thai slot khong bi dao qua lai lien tuc trong canh on dinh.
- Ty le slot khong xac dinh (`unknown`) duoc giam dan qua cac sprint.
- Du lieu output slot duoc TV2/TV6 doc va visual/evaluate truc tiep.

---

## Thanh vien 5 - Infrastructure + Data (TV5)

**Muc tieu**
- Cung cap ha tang doc video, quan ly config slot, va du lieu test de nhom lam viec tron tru.

**Nhiem vu ky thuat chi tiet**
1. `video_reader.py`:
	- Wrapper OpenCV cho file video va stream camera.
	- Xu ly reconnect/co che retry co gioi han.
2. `json_slot_repository.py`:
	- Doc/ghi slot config an toan, validate schema.
	- Bao loi ro rang khi file sai format.
3. Quan ly thu muc `data/`:
	- Chuan hoa ten file video test, metadata co ban (fps, resolution, thoi tiet).
	- Tach bo du lieu train/val/test neu phat trien model nang cao.
4. Quan ly `models/`:
	- Dat convention ten model + version.
	- Tao placeholder/huong dan luu tru model.
5. De xuat migration Data & API:
	- Phuong an chuyen JSON -> SQLite/PostgreSQL.
	- Bo schema occupancy history cho giai doan 3.

**Deliverables bat buoc**
- Adapter doc video su dung on dinh cho TV1/TV2.
- Repository config co validate schema co ban.
- Danh muc video benchmark voi mo ta ngan gon.
- 1 prototype luu occupancy history vao SQLite (minimal schema + ghi doc co ban).

**KPI/DoD cua TV5**
- Loi file/video khong lam crash toan bo chuong trinh.
- Cac file config mau doc duoc o moi may thanh vien.
- Co it nhat 3 video benchmark duoc dong bo cho nhom.

---

## Thanh vien 6 - QA + Evaluation + Automation (TV6)

**Muc tieu**
- Dam bao ket qua co the kiem chung duoc bang test script, benchmark script va bo testcase tai lap loi.

**Nhiem vu ky thuat chi tiet**
1. `src/evaluation/evaluator.py`:
	- Xay script tinh cac chi so co ban: accuracy/precision/recall theo slot neu co nhan.
	- Co mode so sanh output giua cac phien ban detector.
2. Xay bo regression tests:
	- Tu dong chay cho single-camera va multi-camera.
	- Luu output theo format de so sanh giua cac lan run.
3. Test kịch ban end-to-end:
	- Chay voi single-camera va multi-camera.
	- Kiem tra case mat ket noi camera, file slot loi, thay doi anh sang.
4. Tao bo testcase tai lap loi (bug reproduction packs):
	- Moi bug co input, tham so, output mong doi, output thuc te.
	- Danh dau bug theo muc do nghiem trong de uu tien fix.
5. Chuan bi benchmark package cuoi ky:
	- Script benchmark 5-7 phut cho kịch ban demo.
	- Bang ket qua benchmark de doi chieu truoc/sau moi toi uu.

**Deliverables bat buoc**
- Bo regression test script chay duoc tren may nhom.
- Bo benchmark script + output metrics luu theo sprint.
- Bo bug reproduction packs cho cac loi critical/major.

**KPI/DoD cua TV6**
- Moi sprint deu co ket qua regression pass/fail ro rang.
- Cac bug critical deu co testcase tai lap duoc.
- Benchmark cho thay xu huong cai thien hoac canh bao suy giam hieu nang.

## 3) Ke hoach theo giai doan (gan voi docs/TODO.md)

| Giai doan | Muc tieu | TV chiu trach nhiem chinh | TV phoi hop |
|---|---|---|---|
| Giai doan 1 - Setup nen tang | Chot structure, config slot, convention code/branch | TV1, TV5 | TV6 |
| Giai doan 2 - CV Core | Baseline detector + classifier + smoothing | TV3, TV4 | TV1, TV6 |
| Giai doan 3 - Data/API | Chuan bi persistence va API readiness | TV5, TV1 | TV6 |
| Giai doan 4 - Dashboard/Demo | Multi-camera monitoring + script benchmark/demo | TV2, TV6 | TV1, TV3, TV4 |

## 4) Diem ban giao (handoff) bat buoc

1. TV5 -> TV3/TV4:
	- Ban giao video benchmark + config slot hop le.
2. TV3 -> TV4:
	- Ban giao foreground/mask output va thong so da toi uu.
3. TV4 -> TV2:
	- Ban giao output status slot + confidence de ve overlay.
4. TV2 -> TV6:
	- Ban giao kịch ban thao tac demo va output can validate.
5. TV6 -> TV1:
	- Ban giao bao cao loi/rui ro de chot sprint va plan sprint tiep.

## 5) Co che lam viec va kiem soat chat luong

1. Nhanh lam viec:
	- Moi TV tao nhanh theo module (`feature/tvX-module-name`).
2. Quy tac PR:
	- Moi PR phai ghi ro: muc tieu, file anh huong, cach test, screenshot/log (neu co).
3. Review:
	- Toi thieu 1 reviewer, uu tien reviewer la TV co lien quan handoff.
4. Lich dong bo:
	- Daily sync 15 phut (blocker, progress, ke hoach 24h toi).
	- Sprint review hang tuan (demo va retro ngan).
5. Quan ly blocker:
	- Blocker > 24h phai escalate cho TV1 de doi huong ky thuat.
6. Quy tac tai lieu (khong giao rieng 1 nguoi):
	- Moi TV cap nhat phan mo ta ky thuat lien quan ngay trong PR cua minh.
	- TV nao code module nao thi cap nhat phan huong dan module do.

## 6) Tieu chi hoan thanh toan nhom (Team DoD)

- Chay duoc end-to-end tren it nhat 1 kịch ban single-camera va 1 kịch ban multi-camera.
- Co ket qua occupancy va overlay ro rang theo tung slot.
- Co test checklist + bao cao danh gia moi sprint.
- Moi module chinh deu co test hoac script kiem chung tuong ung.
- Co kịch ban demo cuoi ky va phuong an du phong khi loi camera/video.
