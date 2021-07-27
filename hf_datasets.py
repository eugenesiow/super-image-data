from datasets import load_dataset

# dataset = load_dataset('./set5', 'bicubic_x2', split='test')
# dataset = load_dataset('./set5', split='test')
# dataset = load_dataset('./Div2k', 'bicubic_x2', split='validation')
# dataset = load_dataset('./Div2k', 'bicubic_x2', split='validation')
# dataset = load_dataset('eugenesiow/Div2k', 'bicubic_x2', split='validation')
# dataset = load_dataset('eugenesiow/Div2k', split='validation')
dataset = load_dataset('./Set5', 'bicubic_x2', split='validation')

# print(dataset)
# print(f"👉 Dataset len(dataset): {len(dataset)}")
# print(dataset['train'][0])
# print(dataset.config_name)


# def map_to_array(batch):
#     hr = Image.open(image_path).convert('RGB')
#     hr_width = (hr.width // scale) * scale
#     hr_height = (hr.height // scale) * scale
#     hr = hr.resize((hr_width, hr_height), resample=Image.BICUBIC)
#     lr = hr.resize((hr.width // scale, hr_height // scale), resample=Image.BICUBIC)
#
#     hr = np.array(hr)
#     lr = np.array(lr)
#     return batch


# dataset = dataset.map(map_to_array)

print(dataset)
print(dataset[0]['hr'])
print(dataset[0]['lr'])