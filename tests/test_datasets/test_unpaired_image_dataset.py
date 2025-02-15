# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from mmedit.datasets import UnpairedImageDataset
from mmedit.utils import register_all_modules

register_all_modules()


class TestUnpairedImageDataset(object):

    @classmethod
    def setup_class(cls):
        cls.imgs_root = osp.join(
            osp.dirname(osp.dirname(__file__)), 'data/unpaired')
        cls.default_pipeline = [
            dict(type='LoadImageFromFile', key='img_a', color_type='color'),
            dict(type='LoadImageFromFile', key='img_b', color_type='color'),
            dict(
                type='TransformBroadcaster',
                mapping={'img': ['img_a', 'img_b']},
                auto_remap=True,
                share_random_params=True,
                transforms=[
                    dict(
                        type='Resize',
                        scale=(286, 286),
                        interpolation='bicubic')
                ]),
            dict(
                type='Crop',
                keys=['img_a', 'img_b'],
                crop_size=(256, 256),
                random_crop=True),
            dict(type='Flip', direction='horizontal', keys=['img_a', 'img_b']),
            dict(type='PackEditInputs', keys=['img_a', 'img_b']),
        ]

    def test_unpaired_image_dataset(self):
        dataset = UnpairedImageDataset(
            self.imgs_root,
            pipeline=self.default_pipeline,
            domain_a='a',
            domain_b='b')
        assert len(dataset) == 2
        img = dataset[0]['inputs']['img_a']
        assert img.ndim == 3
        img = dataset[0]['inputs']['img_b']
        assert img.ndim == 3
