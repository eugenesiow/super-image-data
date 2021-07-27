# Datasets for super-image

You can find here a list of common image super resolution datasets on [`huggingface datasets`](https://huggingface.co/datasets?filter=task_ids:other-other-image-super-resolution) 
for use with the [`super-image`](https://github.com/eugenesiow/super-image) library.

### Datasets

| dataset  |train |validation|test|
|-------|-----:|---:|---:|
|[Div2k](https://huggingface.co/datasets/eugenesiow/Div2k)|800|100|-|
|[Set5](https://huggingface.co/datasets/eugenesiow/Set5)|-|5|-|
|[Set14](https://huggingface.co/datasets/eugenesiow/Set14)|-|14|-|
|[BSD100](https://huggingface.co/datasets/eugenesiow/BSD100)|-|100|-|
|[Urban100](https://huggingface.co/datasets/eugenesiow/Urban100)|-|100|-|

### Quick Start

Install with `pip`:
```bash
pip install datasets super-image
```

Evaluate a model with the [`super-image`](https://github.com/eugenesiow/super-image) library:
```python
from datasets import load_dataset
from super_image import EdsrModel
from super_image.data import EvalDataset, EvalMetrics

dataset = load_dataset('eugenesiow/Set5', 'bicubic_x2', split='validation')
eval_dataset = EvalDataset(dataset)
model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=2)
EvalMetrics().evaluate(model, eval_dataset)
```