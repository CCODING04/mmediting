# Copyright (c) OpenMMLab. All rights reserved.
from unittest import TestCase
from unittest.mock import MagicMock

import numpy as np
import torch

from mmedit.evaluation import SlicedWassersteinDistance
from mmedit.models import GenDataPreprocessor
from mmedit.structures import EditDataSample, PixelData


class TestSWD(TestCase):

    def test_init(self):
        swd = SlicedWassersteinDistance(
            fake_nums=10, image_shape=(3, 32, 32))  # noqa
        self.assertEqual(len(swd.real_results), 2)

    def test_prosess(self):
        model = MagicMock()
        model.data_preprocessor = GenDataPreprocessor()
        swd = SlicedWassersteinDistance(fake_nums=100, image_shape=(3, 32, 32))
        swd.prepare(model, None)

        torch.random.manual_seed(42)
        real_samples = [
            dict(inputs=torch.rand(3, 32, 32) * 255.) for _ in range(100)
        ]
        fake_samples = [
            EditDataSample(
                fake_img=PixelData(data=torch.rand(3, 32, 32) * 2 - 1),
                gt_img=PixelData(data=torch.rand(3, 32, 32) * 2 -
                                 1)).to_dict() for _ in range(100)
        ]

        swd.process(real_samples, fake_samples)
        output = swd.evaluate()
        result = [16.495922580361366, 24.15413036942482, 20.325026474893093]
        output = [item / 100 for item in output.values()]
        result = [item / 100 for item in result]
        np.testing.assert_almost_equal(output, result, decimal=1)

        swd = SlicedWassersteinDistance(
            fake_nums=4,
            fake_key='fake',
            real_key='img',
            sample_model='orig',
            image_shape=(3, 32, 32))
        swd.prepare(model, None)
