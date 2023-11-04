from PIL import Image
class Pet:
    #initialize Pet object
    #objects in the pet class have 3 data attributes: name, age, and animal type
    def __init__(self, name, animal_type, age, image):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        self.__image = image
    #mutator method, changes name
    def set_name(self, name):
        self.__name = name
    #mutator method, changes animal type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    #mutator method, changes age
    def set_age(self, age):
        self.__age = age
    def set_image(self, image):
        self.__image = image
    #accesor method, returns name
    def get_name(self):
        return self.__name
    def get_image(self):
        return self.__image
    #accessor method, returns animal type
    def get_animal_type(self):
        return self.__animal_type
    #accessor method, returns age
    def get_age(self):
        return self.__age
    
#this function resizes images to 500 pixels maximum on a side and saves as a web
#image copy with an appropriate filename
def imSizer(imFile):
    #open the image pile with pillow
    im = Image.open(imFile)
    #slice all except extension for name
    imName = imFile[:-4]
    #slice last 3 for extension
    imFormat = imFile[-3:]
    dispIm = im.copy()
    #these images are too large to effeciently load online, pillow has a thumbnail
    #function and I'll use that to make the image to display in the output
    dispIm.thumbnail((500,500))
    #display image in program output
    webFile = f'{imName}_websize.{imFormat}'

    dispIm.save(webFile)
    dispIm.close()
    im.close()
    return webFile