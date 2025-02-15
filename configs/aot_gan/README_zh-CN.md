# AOT-GAN (TVCG'2021)

> [AOT-GAN: Aggregated Contextual Transformations for High-Resolution Image Inpainting](https://arxiv.org/pdf/2104.01431.pdf)

> **任务**: 图像修复

<!-- [ALGORITHM] -->

## 摘要

<!-- [ABSTRACT] -->

<!-- [IMAGE] -->

<div align=center >
 <img src="https://user-images.githubusercontent.com/12756472/169230414-3ca7fb6b-cf2a-401f-8696-71df75a08c32.png"/>
</div >

## 结果与模型

**Places365-Challenge**

|                           算法                           |      掩膜类型      | 分辨率  | 训练集容量 |    测试集     | l1 损失 | PSNR  | SSIM  |        GPU 信息         |                           下载                           |
| :------------------------------------------------------: | :----------------: | :-----: | :--------: | :-----------: | :-----: | :---: | :---: | :---------------------: | :------------------------------------------------------: |
| [AOT-GAN](/configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py) | free-form (50-60%) | 512x512 |    500k    | Places365-val |  7.07   | 19.01 | 0.682 | 4 (GeForce GTX 1080 Ti) | [模型](https://openmmlab-share.oss-cn-hangzhou.aliyuncs.com/mmediting/inpainting/aot_gan/AOT-GAN_512x512_4x12_places_20220509-6641441b.pth) \| [日志](https://openmmlab-share.oss-cn-hangzhou.aliyuncs.com/mmediting/inpainting/aot_gan/AOT-GAN_512x512_4x12_places_20220509-6641441b.json) |

<!-- SKIP THIS TABLE -->

| 评估指标        | 掩膜缺损 | 论文结果 | 复现结果 |
| :-------------- | :------- | :------- | :------- |
| L1 (10^-2)      | 1 – 10%  | 0.55     | 0.54     |
| (lower better)  | 10 – 20% | 1.19     | 1.47     |
|                 | 20 – 30% | 2.11     | 2.79     |
|                 | 30 – 40% | 3.20     | 4.38     |
|                 | 40 – 50% | 4.51     | 6.28     |
|                 | 50 – 60% | 7.07     | 10.16    |
| PSNR            | 1 – 10%  | 34.79    | inf      |
| (higher better) | 10 – 20% | 29.49    | 31.22    |
|                 | 20 – 30% | 26.03    | 27.65    |
|                 | 30 – 40% | 23.58    | 25.06    |
|                 | 40 – 50% | 21.65    | 23.01    |
|                 | 50 – 60% | 19.01    | 20.05    |
| SSIM            | 1 – 10%  | 0.976    | 0.982    |
| (higher better) | 10 – 20% | 0.940    | 0.951    |
|                 | 20 – 30% | 0.890    | 0.911    |
|                 | 30 – 40% | 0.835    | 0.866    |
|                 | 40 – 50% | 0.773    | 0.815    |
|                 | 50 – 60% | 0.682    | 0.739    |

## 快速开始

**训练**

<details>
<summary>训练说明</summary>

您可以使用以下命令来训练模型。

```shell
# CPU上训练
CUDA_VISIBLE_DEVICES=-1 python tools/train.py configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py

# 单个GPU上训练
python tools/train.py configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py

# 多个GPU上训练
./tools/dist_train.sh configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py 8
```

更多细节可以参考 [train_test.md](/docs/zh_cn/user_guides/train_test.md) 中的 **Train a model** 部分。

</details>

**测试**

<details>
<summary>测试说明</summary>

您可以使用以下命令来测试模型。

```shell
# CPU上测试
CUDA_VISIBLE_DEVICES=-1 python tools/test.py configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py https://openmmlab-share.oss-cn-hangzhou.aliyuncs.com/mmediting/inpainting/aot_gan/AOT-GAN_512x512_4x12_places_20220509-6641441b.pth

# 单个GPU上测试
python tools/test.py configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py https://openmmlab-share.oss-cn-hangzhou.aliyuncs.com/mmediting/inpainting/aot_gan/AOT-GAN_512x512_4x12_places_20220509-6641441b.pth

# 多个GPU上测试
./tools/dist_test.sh configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py https://openmmlab-share.oss-cn-hangzhou.aliyuncs.com/mmediting/inpainting/aot_gan/AOT-GAN_512x512_4x12_places_20220509-6641441b.pth 8
```

更多细节可以参考 [train_test.md](/docs/zh_cn/user_guides/train_test.md) 中的 **Test a pre-trained model** 部分。

</details>

## 引用

```bibtex
@inproceedings{yan2021agg,
  author = {Zeng, Yanhong and Fu, Jianlong and Chao, Hongyang and Guo, Baining},
  title = {Aggregated Contextual Transformations for High-Resolution Image Inpainting},
  booktitle = {Arxiv},
  pages={-},
  year = {2020}
}
```
