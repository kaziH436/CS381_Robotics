# **Upper-Body Muscle Estimation from Smartphone Video with OpenCap**

## **The idea** 

Human pose estimation is one of the most challenging problems in computer vision. The paper, “Deep High-Resolution Representation Learning for Human Pose Estimation” (HRNet), addresses it by starting with a high-resolution subnetwork, gradually adding lower-resolution subnetworks, and connecting these multiresolution subnetworks in parallel. The paper “Whole-Body Human Pose Estimation in the Wild” extends this approach to the entire human body. OpenCap builds on both papers, combining pose estimation with OpenSim inverse kinematics to estimate kinematics and dynamics from videos captured by two or more smartphones. This project extends OpenCap by addressing the limitation of the deep learning model and help it generalize 3D marker set to activities outside of the distribution of activities that it was trained on. This can include task-specific tuning of the deep learning model.

## **The three papers**

1. **Uhlrich SD, Falisse A, Kidzinski L, Muccini J, Ko M, Chaudhari AS, Hicks JL, Delp SL (2023).** OpenCap: Human movement dynamics from smartphone videos. *PLOS Computational Biology* 19(10): e1011462. [https\://doi.org/10.1371/journal.pcbi.1011462](https://doi.org/10.1371/journal.pcbi.1011462)  
2. **Sun K, Xiao B, Liu D, Wang J (2019).** Deep High-Resolution Representation Learning for Human Pose Estimation. *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. [https\://arxiv.org/pdf/1902.09212](https://arxiv.org/pdf/1902.09212)  
3. **Jin S, Xu L, Xu J, Wang C, Liu W, Qian C, Ouyang W, Luo P (2020).** Whole-Body Human Pose Estimation in the Wild. *European Conference on Computer Vision (ECCV)*. [https\://arxiv.org/pdf/2007.11858](https://arxiv.org/pdf/2007.11858) (DOI 10.1007/978-3-030-58545-7\_12)

## 

## 

## 

## **Summary of the techniques connected to the project**

**Paper 1: OpenCap (Uhlrich et al., 2023).** OpenCap, an open-source platform for computing both the kinematics (i.e., motion) and dynamics (i.e., forces) of human movement using videos captured from two or more smartphones. HRNet is used to extract 2D keypoints from videos and time synchronizing them across videos using cross-correlations of keypoint velocities which is used to get the 3D keypoints triangulated. The user first records a standing pose and OpenCap uses the anatomical marker positions to scale an OpenSim musculoskeletal model. Long short-term memory (LSTM) is used to find  joint kinematics and kinetics from tracking simulations are used to find muscle excitations minimizing a cost under dynamics constraints. The optimal control problems are formulated in Python with CasADi \[[93](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011462#pcbi.1011462.ref093)\] (v3.5), using direct collocation and implicit formulations of the muscle and skeleton dynamics. The authors validated it on 10 people doing squats, sit-to-stand, drop jumps, and walking against marker-based motion capture, and ran a 100-subject field study in which a clinician estimated dynamics 25 times faster than a lab approach at under 1% of the cost. The goal of our project is to improve how the pose estimation is done for the human upper body.

**Paper 2: HRNet (Sun et al., 2019).** Most pose networks encode an image at low resolution and then recover high resolution afterwards. HRNet instead starts from a high-resolution subnetwork, adds high-to-low resolution subnetworks in parallel, and repeatedly exchanges information across resolutions. Hence, the predicted keypoint heatmaps are potentially more accurate and spatially more precise. It was evaluated on the COCO keypoint and MPII Human Pose benchmarks. 

**Paper 3: Whole-Body Pose (Jin et al., 2020).** Most pose estimation datasets and methods cover certain parts of the body as separate problems. This paper introduces COCO-WholeBody, which extends the COCO dataset with whole-body annotations of 133 keypoints per person covering the body, feet, face, and hands. The authors also propose ZoomNet, a single network that accounts for the hierarchical structure of the human body and for the large differences between parts such as the body, face, and hands. They benchmark existing methods on the new dataset and show that whole-body estimation is considerably harder than body-only estimation. 

## **Tutorials**

* YouTube: Webinar (Tutorial): OpenCap \- Analyzing 3D Human Movement Dynamics using Smartphone Videos, Part 2 of 2: [https\://www\.youtube.com/watch?v=7Xk8-K7A3Zk](https://www.youtube.com/watch?v=7Xk8-K7A3Zk)  
* Webinar: OpenCap \- Analyzing 3D Human Movement Dynamics using Smartphone Videos, Part 1 of 2: [https\://www\.youtube.com/watch?v=8dPumbAQpIA](https://www.youtube.com/watch?v=8dPumbAQpIA)  
* Web app: [https\://app.opencap.ai](https://app.opencap.ai)  
* Github: [https\://github.com/opencap-org/opencap-core](https://github.com/opencap-org/opencap-core)  
* Code for muscle-driven simulations: [https\://github.com/opencap-org/opencap-processing](https://github.com/opencap-org/opencap-processing)

