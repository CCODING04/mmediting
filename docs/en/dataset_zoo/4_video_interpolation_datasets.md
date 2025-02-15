# Video Frame Interpolation Datasets

It is recommended to symlink the dataset root to `$MMEDITING/data`. If your folder structure is different, you may need to change the corresponding paths in config files.

MMEditing supported video frame interpolation datasets:

- [Vimeo90K-triplet](#vimeo90k-triplet-dataset) \[ [Homepage](http://toflow.csail.mit.edu) \]

## Vimeo90K-triplet Dataset

<!-- [DATASET] -->

```bibtex
@article{xue2019video,
  title={Video Enhancement with Task-Oriented Flow},
  author={Xue, Tianfan and Chen, Baian and Wu, Jiajun and Wei, Donglai and Freeman, William T},
  journal={International Journal of Computer Vision (IJCV)},
  volume={127},
  number={8},
  pages={1106--1125},
  year={2019},
  publisher={Springer}
}
```

The training and test datasets can be download from [here](http://toflow.csail.mit.edu/).

The Vimeo90K-triplet  dataset has a `clip/sequence/img` folder structure:

```text
mmediting
├── mmedit
├── tools
├── configs
├── data
│   ├── vimeo_triplet
│   │   ├── tri_testlist.txt
│   │   ├── tri_trainlist.txt
│   │   ├── sequences
│   │   │   ├── 00001
│   │   │   │   ├── 0001
│   │   │   │   │   ├── im1.png
│   │   │   │   │   ├── im2.png
│   │   │   │   │   └── im3.png
│   │   │   │   ├── 0002
│   │   │   │   ├── 0003
│   │   │   │   ├── ...
│   │   │   ├── 00002
│   │   │   ├── ...
```
