import shutil
import os

# Get current directoy
current_path = os.getcwd()
print(current_path)

# Download data using Kaggle API 
os.system('kaggle competitions download -c aptos2019-blindness-detection -p "./data/external/"')

# Unpack .zip file
shutil.unpack_archive('./data/external/aptos2019-blindness-detection.zip', \
    './data/raw/aptos2019-blindness-detection.zip')