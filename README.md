# AI vs Human-Generated Image Detection

## Project Overview
This project focuses on distinguishing between AI-generated and human-generated images.

## Approach
1. **Baseline Model:**
   - We initially implemented a **Histogram of Oriented Gradients (HOG)** feature extractor combined with a **Support Vector Machine (SVM)** classifier.
   
2. **Optimal Model:**
   - To improve accuracy, we developed a **Deep Convolutional Neural Network (CNN)** as our final model for robust classification.

## Dataset
The dataset used for this project can be found at: [Dataset Link](https://www.kaggle.com/datasets/alessandrasala79/ai-vs-human-generated-dataset)  
(Replace `#` with the actual dataset URL)

## Conclusion
Through experimentation, we found that deep learning models, specifically CNNs, provide significantly better performance for this task compared to traditional methods like HOG+SVM.

---

