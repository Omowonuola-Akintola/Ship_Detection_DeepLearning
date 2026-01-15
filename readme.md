## Deep Learning–Based Ship Detection in SAR Imagery

#### Background
Ship detection plays a vital role in maritime monitoring and security. Synthetic Aperture Radar (SAR) enables day-and-night, all-weather observation of ships, overcoming the limitations of optical sensors such as cloud cover and illumination
dependence (Gupta et al., 2024).
Deep learning enables end-to-end, noise-robust ship detection in SAR imagery by automatically learning discriminative features (Qiao et al., 2025).

#### Objectives

The main objective of this project is to develop and evaluate deep learning–based methods for ship detection in Synthetic Aperture Radar (SAR) imagery. 
The specific objectives are:

- To implement and train deep learning models, including YOLO, DETR, and Faster R-CNN, for detecting ships in SAR data.

- To compare the performance of these models in terms of mAP, and computational efficiency.

#### Datasets

For the experiment, data were accessed from kaggle [SARscope](https://www.kaggle.com/datasets/kailaspsudheer/sarscope-unveiling-the-maritime-landscape). It contains a total of 6,735 SAR images, supporting both detection and segmentation tasks. 

The Key features of datasets are as follow:

- Dual-purpose dataset: Suitable for ship detection and instance segmentation

- High-resolution data: 5,719 SAR images resized to 640 × 640, with 17,708 ship instances

- Polarizations: Includes VV and VH channels

- Efficient processing: Images resized for faster training and stored using lossless compression

- Balanced split: 70% training, 20% validation, 10% testing

- Standard format: Annotations provided in COCO (MMDetection-compatible) format
  
- Dataset size: 398.17 MB

#### Models
This project evaluates multiple deep learning models, focusing on both accuracy and computational efficiency.

**1. YOLO (You Only Look Once)**

Released on 10 January 2023 by Ultralytics, this model is a fast and robust single-stage, anchor-free detector designed for efficient object detection. It enhances generalization across diverse object shapes and supports multiple tasks, including object detection, instance segmentation, image classification, and pose estimation. The model is available in nano, small, medium, large, and extra-large variants.

**2. DETR (DEtection TRansformer)**

Real-Time Detection Transformer (RT-DETR), released in 2023 and developed by Baidu, is based on the DETR architecture, which operates without the need for non-maximum suppression (NMS). The model is available in large and extra-large sizes.


**3. Faster R-CNN**

Released in 2015 by Ren, He, Girshick, and Sun from Microsoft Research, this model is a two-stage object detector that first generates region proposals and then performs classification. It uses a Region Proposal Network (RPN) to produce candidate bounding boxes and improves efficiency by sharing convolutional features between the proposal and classification stages. The original backbone architecture is VGG16.


#### Model Performance Comparision

<img width="751" height="224" alt="Screenshot 2026-01-14 at 21 11 42" src="https://github.com/user-attachments/assets/2cb60126-4325-4176-a36f-07cacef51e52" />

RT-DETR achieves the highest detection accuracy on both validation and test sets, outperforming
YOLOv8 models at the cost of longer training and inference time.

YOLOv8m and YOLOv8l provide faster training and inference, making them suitable for speed-
essential applications.

Faster R-CNN shows lower accuracy and efficiency, despite comparable model size, highlighting the
advantage of single-stage and transformer-based detectors.

#### Results

**YOLOv8m model**
<img width="1127" height="378" alt="Screenshot 2026-01-14 at 22 14 21" src="https://github.com/user-attachments/assets/d8157271-c2d3-4ffa-a5e7-79592e5b3c56" />

**YOLOv8l model**
<img width="1127" height="378" alt="Screenshot 2026-01-14 at 22 14 44" src="https://github.com/user-attachments/assets/a72c06f1-632e-44bd-827e-1d9cbc059df5" />

**RT-DETR model**

<img width="1127" height="380" alt="Screenshot 2026-01-14 at 22 15 26" src="https://github.com/user-attachments/assets/c4174334-5afe-4f32-a42b-d46721510e86" />

**Faster-RCNN model**

<img width="584" height="479" alt="Screenshot 2026-01-14 at 22 16 09" src="https://github.com/user-attachments/assets/7b0a7aeb-761b-4f54-b05b-34de6de9b7c1" />
