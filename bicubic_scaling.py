from PIL import Image
from pathlib import Path


def bicubic_scaling(input_dir, scales):
    input_path = Path(input_dir)
    scale_paths = {}
    for scale in scales:
        parent_path = (input_path.parent / f'{input_path.name}_LR_x{scale}')
        scale_paths[scale] = parent_path
        parent_path.mkdir(parents=True, exist_ok=True)
    for file_name in input_path.glob('*.png'):
        hr = Image.open(file_name).convert('RGB')
        for scale, scale_path in scale_paths.items():
            lr = hr.resize((hr.width // scale, hr.height // scale), resample=Image.BICUBIC)
            lr.save(scale_path / f'{file_name.name}', "PNG")


# bicubic_scaling('./data/Set5', [2, 3, 4])
# bicubic_scaling('./data/Set14', [2, 3, 4])
# bicubic_scaling('./data/BSD100', [2, 3, 4])
bicubic_scaling('./data/Urban100', [2, 3, 4])
