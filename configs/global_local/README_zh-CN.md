# Global&Local (ToG'2017)

> **任务**: 图像修复

<!-- [ALGORITHM] -->

<details>
<summary align="right">Global&Local (ToG'2017)</summary>

```bibtex
@article{iizuka2017globally,
  title={Globally and locally consistent image completion},
  author={Iizuka, Satoshi and Simo-Serra, Edgar and Ishikawa, Hiroshi},
  journal={ACM Transactions on Graphics (ToG)},
  volume={36},
  number={4},
  pages={1--14},
  year={2017},
  publisher={ACM New York, NY, USA}
}
```

</details>

<br/>

*请注意，为了与当前的深度图像修复方法进行公平比较，我们没有在 Global&Local 中使用后处理模块。*

**Places365-Challenge**

|                               算法                               |  掩膜类型   | 分辨率  | 训练集容量 |    测试集     | l1 损失 |  PSNR  | SSIM  | GPU 信息 |                                 下载                                  |
| :--------------------------------------------------------------: | :---------: | :-----: | :--------: | :-----------: | :-----: | :----: | :---: | :------: | :-------------------------------------------------------------------: |
| [Global&Local](/configs/global_local/gl_8xb12_places-256x256.py) | square bbox | 256x256 |    500k    | Places365-val | 11.164  | 23.152 | 0.862 |    8     | [模型](https://download.openmmlab.com/mmediting/inpainting/global_local/gl_256x256_8x12_places_20200619-52a040a8.pth) \| [日志](https://download.openmmlab.com/mmediting/inpainting/global_local/gl_256x256_8x12_places_20200619-52a040a8.log.json) |

**CelebA-HQ**

|                               算法                               |  掩膜类型   | 分辨率  | 训练集容量 |   测试集   | l1 损失 |  PSNR  | SSIM  | GPU 信息 |                                   下载                                   |
| :--------------------------------------------------------------: | :---------: | :-----: | :--------: | :--------: | :-----: | :----: | :---: | :------: | :----------------------------------------------------------------------: |
| [Global&Local](/configs/global_local/gl_8xb12_celeba-256x256.py) | square bbox | 256x256 |    500k    | CelebA-val |  6.678  | 26.780 | 0.904 |    8     | [模型](https://download.openmmlab.com/mmediting/inpainting/global_local/gl_256x256_8x12_celeba_20200619-5af0493f.pth) \| [日志](https://download.openmmlab.com/mmediting/inpainting/global_local/gl_256x256_8x12_celeba_20200619-5af0493f.log.json) |

## 快速开始

**训练**

<details>
<summary>训练说明</summary>

您可以使用以下命令来训练模型。

```shell
# CPU上训练
CUDA_VISIBLE_DEVICES=-1 python tools/train.py configs/global_local/gl_8xb12_places-256x256.py

# 单个GPU上训练
python tools/train.py configs/global_local/gl_8xb12_places-256x256.py

# 多个GPU上训练
./tools/dist_train.sh configs/global_local/gl_8xb12_places-256x256.py 8
```

更多细节可以参考 [train_test.md](/docs/zh_cn/user_guides/train_test.md) 中的 **Train a model** 部分。

</details>

**测试**

<details>
<summary>测试说明</summary>

您可以使用以下命令来测试模型。

```shell
# CPU上测试
CUDA_VISIBLE_DEVICES=-1 python tools/test.py configs/global_local/gl_8xb12_places-256x256.py https://download.openmmlab.com/mmediting/inpainting/global_local/gl_256x256_8x12_places_20200619-52a040a8.pth

# 单个GPU上测试
python tools/test.py configs/global_local/gl_8xb12_places-256x256.py https://download.openmmlab.com/mmediting/inpainting/global_local/gl_256x256_8x12_places_20200619-52a040a8.pth

# 多个GPU上测试
./tools/dist_test.sh configs/global_local/gl_8xb12_places-256x256.py https://download.openmmlab.com/mmediting/inpainting/global_local/gl_256x256_8x12_places_20200619-52a040a8.pth 8
```

更多细节可以参考 [train_test.md](/docs/zh_cn/user_guides/train_test.md) 中的 **Test a pre-trained model** 部分。

</details>
