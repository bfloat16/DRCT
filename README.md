# DRCT

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/activating-more-pixels-in-image-super/image-super-resolution-on-set5-4x-upscaling)](https://paperswithcode.com/sota/image-super-resolution-on-set5-4x-upscaling?p=drct-saving-image-super-resolution-away-from)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/activating-more-pixels-in-image-super/image-super-resolution-on-urban100-4x)](https://paperswithcode.com/sota/image-super-resolution-on-urban100-4x?p=drct-saving-image-super-resolution-away-from)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/activating-more-pixels-in-image-super/image-super-resolution-on-set14-4x-upscaling)](https://paperswithcode.com/sota/image-super-resolution-on-set14-4x-upscaling?p=drct-saving-image-super-resolution-away-from)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/activating-more-pixels-in-image-super/image-super-resolution-on-manga109-4x)](https://paperswithcode.com/sota/image-super-resolution-on-manga109-4x?p=drct-saving-image-super-resolution-away-from)


### DRCT: Saving Image Super-resolution away from Information Bottleneck [[Paper Link]](https://arxiv.org/abs/2404.00722) [[Project Page]](https://allproj002.github.io/drct.github.io/)

[Chih-Chung Hsu](https://cchsu.info/), [Chia-Ming Lee](https://ming053l.github.io/), [Yi-Shiuan Chou](https://scholar.google.com/citations?&user=iGX8FBcAAAAJ)

<img src=".\figures\overview.png" width="800"/>


## Updates

- ✅ 2024-03-31: Release the first version of the paper at Arxiv.
- ✅ 2024-04-14: DRCT is accepted by NTIRE 2024, CVPR.


## Citations
#### BibTeX

    @misc{hsu2024drct,
      title={DRCT: Saving Image Super-resolution away from Information Bottleneck}, 
      author={Chih-Chung Hsu and Chia-Ming Lee and Yi-Shiuan Chou},
      year={2024},
      eprint={2404.00722},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
    }

## Environment
- [PyTorch >= 1.7](https://pytorch.org/) **(Recommend **NOT** using torch 1.8!!! It would cause abnormal performance.)**
- [BasicSR == 1.3.4.9](https://github.com/XPixelGroup/BasicSR/blob/master/INSTALL.md) 
### Installation
Install Pytorch first.
Then,
```
pip install -r requirements.txt
python setup.py develop
```

## How To Test

- Refer to `./options/test` for the configuration file of the model to be tested, and prepare the testing data and pretrained model.  
- Then run the following codes (taking `DRCT_SRx4_ImageNet-pretrain.pth` as an example):
```
python drct/test.py -opt options/test/DRCT_SRx4_ImageNet-pretrain.yml
```
The testing results will be saved in the `./results` folder.  

- Refer to `./options/test/DRCT_SRx4_ImageNet-LR.yml` for **inference** without the ground truth image.

**Note that the tile mode is also provided for limited GPU memory when testing. You can modify the specific settings of the tile mode in your custom testing option by referring to `./options/test/HAT_tile_example.yml`.**

## How To Train
- Refer to `./options/train` for the configuration file of the model to train.
- Preparation of training data can refer to [this page](https://github.com/XPixelGroup/BasicSR/blob/master/docs/DatasetPreparation.md). ImageNet dataset can be downloaded at the [official website](https://image-net.org/challenges/LSVRC/2012/2012-downloads.php).
- The training command is like
```
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python -m torch.distributed.launch --nproc_per_node=8 --master_port=4321 drct/train.py -opt options/train/train_DRCT_SRx2_from_scratch.yml --launcher pytorch
```
- Note that the default batch size per gpu is 4, which will cost about 20G memory for each GPU.  

The training logs and weights will be saved in the `./experiments` folder.



## Thanks

A part of our work has been facilitated by the [HAT](https://github.com/XPixelGroup/HAT) framework, and we are grateful for its outstanding contribution.

## Contact
If you have any question, please email zuw408421476@gmail.com to discuss with the author.
