import os

# Install required packages 
os.system("pip install keras tensorflow scipy pillow numpy")


from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

def get_file_names(inDir):
    # Get a list of all files in the specified folder
    files = os.listdir(inDir)
    return files

def dataset_Augmentation(file_names, inDir, outDir, fName, fileFormat, numAug, input_width, input_height):
    for file_name in file_names:
        # Construct the complete file path
        file_path = os.path.join(inDir, file_name)

        datagen = ImageDataGenerator(
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )
        img = load_img(file_path, target_size=(input_height, input_width))  # Resize the image to the specified dimensions
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)

        i = 0
        for batch in datagen.flow(x, batch_size=1,
                                   save_to_dir=outDir, save_prefix=fName, save_format=fileFormat):

            i += 1
            if i > numAug-1:
                break

def generate_ascii_art():
    ascii_art = """
    ________             __     __  __            __                               _              __         
    /_  __/ /  ___ ____  / /__   \ \/ /__  __ __  / /  ___ __  _____   ___ _  ___  (_)______   ___/ /__ ___ __
     / / / _ \/ _ `/ _ \/  '_/    \  / _ \/ // / / _ \/ _ `/ |/ / -_) / _ `/ / _ \/ / __/ -_) / _  / _ `/ // /
    /_/ /_//_/\_,_/_//_/_/\_\     /_/\___/\_,_/ /_//_/\_,_/|___/\__/  \_,_/ /_//_/_/\__/\__/  \_,_/\_,_/\_, / 
                                                                                                   /___/  
                         __      __              _ ___     __                                                     
      __ _  ___ ____/ /__   / /  __ __  ____(_) _/__ _/ /_                                                    
     /  ' \/ _ `/ _  / -_) / _ \/ // / / __/ / _/ _ `/ __/                                                    
    /_/_/_/\_,_/\_,_/\__/ /_.__/\_, / /_/ /_/_/ \_,_/\__/                                                     
                               /___/                                                                          
                                                                                                                        
    """
    print(ascii_art)

# input image directory
print("Input Image Directory")
inDir = input("Copy and paste the url : ")

# output image directory
print("\nOutput Image Directory")
outDir = input("Copy and paste the url : ")

# file name prefix
fName = input("\nAny valid File Name : ")

# file format
options = input("\nChoose File Format\n1.jpeg\n2.jpg\n3.png\n\n")
if options == '1':
    fileFormat = 'jpeg'
elif options == '2':
    fileFormat = 'jpg'
else:
    fileFormat = 'png'

# number of augmentation
numAug = input("Number of Augmentation you Want : ")
numAug = int(numAug)

# image width and height
input_width = int(input("Input Image Width (in pixels): "))
input_height = int(input("Input Image Height (in pixels): "))

file_names = get_file_names(inDir)
dataset_Augmentation(file_names, inDir, outDir, fName, fileFormat, numAug, input_width, input_height)
generate_ascii_art()
