# AWS Sagemaker Custom Tensorflow Object Detection Development

Welcome to my personal template for TensorFlow Object Detection API training and model deployment in AWS Repository! This repository contains:

## PREQUISITION

1. You shall have already labeled dataset in .xml format. You may use labelImg tools for data labelling or other tools.
2. Create your local conda environment in your local computer.
3. You already setup AWS SDK and configuration on your local computer.
4. You have created the respective AWS S3 Storage access.
5. You have created the respective AWS Sagemaker access.
6. You have created your own AWS Sagemaker Notebook to run the notebook code.
7. You have created IAM Role to allow Sagemaker to access your S3 Storage.
8. Setup your own AWS Network Security if necessary.

## STEPS

### 1. Convert PASCAL VOC labeling format (xml t0 json)

- **Description:** AWS did not accept .xml format for data labelling. Hence, we need to convert the format into single annotaion.json format. I already provide the utility tools to convert all of the .xml into annotation.json.

1. Activate conda local environment

```
conda activte YOUR_ENV_NAME
```

2. Ensure all of the dataset (images and xml files) alread in the "dataset" folder. You may include subdirectory.

3. To generate annotation.json files. Run:

```
python3 xml_to_annotation_json.py
```

4. All of the images will be sorted and copied into input_directory folders. You need to upload this folder into your AWS S3 Storage!

### 2. Test TensorFlow Object Detection Model Zoo in AWS Sagemaker

If you want to test any of the TensorFlow Object Detection Model Zoo in AWS Sagemaker Environment, you may look into the "aws_sagemaker_tensorflow_model_zoo_object_detection.ipynb" files.

Note: Please understand what each of the code line represent. You may change the lines according to your case. E.g the S3 directory etc.

### 2. Train & Deploy CUSTOM TensorFlow Object Detection Model in AWS Sagemaker

If you want to train & deploy custom object detection model in AWS Sagemaker Environment, you may look into the "aws_sagemaker_tensorflow_custom_object_detection.ipynb" files.

Note: Please understand what each of the code line represent. You may change the lines according to your case. E.g the S3 directory etc.

### Credit:

This repository is a modification code from the main [AWS repository](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/object_detection_tensorflow/Amazon_Tensorflow_Object_Detection.ipynb)
