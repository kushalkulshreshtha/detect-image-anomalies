# Checking for anomalies in images using vision transformer

## Steps:

1. Data Preparation: Base image data was taken form Logo 2k-plus dataset ( https://github.com/Wangjing1551/Logo-2k-plus-Dataset?tab=readme-ov-file ). To create the flawed data, 2000 random images were sampled and 3 kinds of anomalies were introduced using OpenCV (smudge, blur and crack). The sampled and prepared data is stored under data folder. The script is [prepare_data.py](prepare_data.py)
   
2. Model training: Vision transformer's pretrained model was taken from HuggingFace, and only last 3 layers were fine-tuned to our task. 87% accuracy was recorded on validation data only after 3 epochs of training!

## Colab Link

https://colab.research.google.com/drive/1ceVU3YzonQvNnDamPK4ojsb2Ci7O7xG7?usp=sharing


**Data source:**

```
@inproceedings{Wang2020Logo2K,
author={Jing Wang, and Weiqing Min, and Sujuan Hou, and Shengnan Ma, and Yuanjie Zheng, and Haishuai Wang, and Shuqiang Jiang},
booktitle={AAAI Conference on Artificial Intelligence. Accepted},
title={{Logo-2K+:} A Large-Scale Logo Dataset for Scalable Logo Classification},
year={2020}
}
```
