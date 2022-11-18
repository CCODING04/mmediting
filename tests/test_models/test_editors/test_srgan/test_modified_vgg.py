# Copyright (c) OpenMMLab. All rights reserved.
import torch

from mmedit.models.editors import ModifiedVGG


def test_modifiedVGG():
    model = ModifiedVGG(3, 16)
    inputs = torch.randn(1, 3, 128, 128)
    outputs = model(inputs)
    assert outputs.shape == (1, 1)
