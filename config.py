import os

# -----------------
# DATASET ROOTS
# -----------------

BASE_DATA_PATH = './data'

cifar_10_root = os.path.join(BASE_DATA_PATH, 'cifar10')
cifar_100_root = os.path.join(BASE_DATA_PATH, 'cifar100')
cub_root = os.path.join(BASE_DATA_PATH, 'CUB')
aircraft_root = os.path.join(BASE_DATA_PATH, 'aircraft')
herbarium_dataroot = os.path.join(BASE_DATA_PATH, 'herbarium_19')
imagenet_root = os.path.join(BASE_DATA_PATH, 'imagenet')

# OSR Split dir
osr_split_dir = os.path.join(BASE_DATA_PATH, 'ssb_splits')

# -----------------
# OTHER PATHS
# -----------------
exp_root = '/home/pbt245/D:/generalized-category-discovery/outputs'
feature_extract_dir = '/home/pbt245/D:/generalized-category-discovery/features'
dino_pretrain_path = '/home/pbt245/D:/generalized-category-discovery/dino/dino_vitbase16_pretrain.pth'
scars_root = '/home/pbt245/datasets/stanford_car'