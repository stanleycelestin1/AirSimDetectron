# Using AirsimDetectron

Currently integration in only done in tools/car/airsim_infer_simple.py. The idea is instead of using images in 
a folder, we will use Airsim's API's to get images.



To run inference on the images from airsiom, use  `airsim_infer_simple.py` tool. In this example, we're using an end-to-end trained Mask R-CNN model with a ResNet-101-FPN backbone from the model zoo:


```
python tools/car/airsim_infer_simple.py     
    --cfg configs/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml  \   
    --output-dir /tmp/detectron-visualizations     \
    --image-ext jpg  \   
    --wts https://s3-us-west-2.amazonaws.com/detectron/35861858/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml.02_32_51.SgT4y1cO/output/train/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl \
    demo

```

This should give you a general idea of how airsim get image API's work.


http://cseweb.ucsd.edu/~amt062/wearecse.jpg
http://grad.ucsd.edu/admissions/requirements/what/statement-of-purpose.html