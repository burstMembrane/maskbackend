import gdown

# get pretrained pkl from google drive server if it isn't there already

url = "https://drive.google.com/uc?id=19wQe12syOYopUVA_eEHUdiqtdIKl4m7L"
output = 'pretrained/masks-early.pkl'
if os.path.isfile(output) is False:
    print('file not found, downloading from google drive')
    gdown.download(url, output)

