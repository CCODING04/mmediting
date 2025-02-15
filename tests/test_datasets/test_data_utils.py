# Copyright (c) OpenMMLab. All rights reserved.
from mmedit.datasets.data_utils import infer_io_backend


def test_infer_io_backend():
    path = 'http://openmmlab/xxx'
    assert infer_io_backend(path) == 'http'

    path = 'https://torchvision/xxx'
    assert infer_io_backend(path) == 'http'

    path = 'MYCLUSTER:s3://openmmlab/datasets/mmediting/lsun/'
    assert infer_io_backend(path) == 'petrel'

    path = 's3://work_dirs/'
    assert infer_io_backend(path) == 'petrel'

    path = 'this/is/a/test'
    assert infer_io_backend(path) == 'disk'


# TODO: add more uts
