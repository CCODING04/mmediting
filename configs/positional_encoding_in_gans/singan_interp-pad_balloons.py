_base_ = ['../singan/singan_balloons.py']

# TODO: bugs here
# MODEL
# NOTE: add by user, e.g.:
# test_pkl_data = './work_dirs/singan_pkl/singan_interp-pad_balloons_20210406_180014-96f51555.pkl'  # noqa
test_pkl_data = None

model = dict(
    type='PESinGAN',
    generator=dict(
        type='SinGANMSGeneratorPE', interp_pad=True, noise_with_pad=True),
    fixed_noise_with_pad=True,
    test_pkl_data=test_pkl_data)
