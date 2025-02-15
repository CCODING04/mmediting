# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from mmedit.apis.inferencers.matting_inferencer import MattingInferencer
from mmedit.utils import register_all_modules

register_all_modules()


def test_matting_inferencer():
    data_root = osp.join(osp.dirname(__file__), '../../../')
    config = data_root + 'configs/dim/dim_stage3-v16-pln_1xb1-1000k_comp1k.py'
    img_path = data_root + 'tests/data/matting_dataset/merged/GT05.jpg'
    trimap_path = data_root + 'tests/data/matting_dataset/trimap/GT05.png'
    result_out_dir = osp.join(
        osp.dirname(__file__), '..', '..', 'data', 'matting_result.png')

    inferencer_instance = \
        MattingInferencer(config, None)
    inferencer_instance(img=img_path, trimap=trimap_path)
    inference_result = inferencer_instance(
        img=img_path, trimap=trimap_path, result_out_dir=result_out_dir)
    result_img = inference_result[1]
    assert result_img.numpy().shape == (552, 800)


if __name__ == '__main__':
    test_matting_inferencer()
