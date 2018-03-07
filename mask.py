import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def redlogo(original_image,red,template):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = template.size
    resized_image = original_image.resize((width,height))
    
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    rounded_mask.paste(red, (0,0))
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    
    #resizes the image to 200 to 200 for easy pasting
   
    
    result = PIL.Image.new('RGBA', template.size, (0,0,0,0))
    result.paste(resized_image, (0,0), mask=rounded_mask)
    return result
def bluelogo(original_image,blue,template):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = template.size
    resized_image = original_image.resize((width,height))
    
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    rounded_mask.paste(blue, (0,0))
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    
    #resizes the image to 200 to 200 for easy pasting
   
    
    result = PIL.Image.new('RGBA', template.size, (0,0,0,0))
    result.paste(resized_image, (0,0), mask=rounded_mask)
    return result
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        if len(file_list)<2:
            absolute_filename = os.path.join(directory, entry)
            try:
                image = PIL.Image.open(absolute_filename)
                file_list += [entry]
                image_list += [image]
            except IOError:
                pass # do nothing with errors tying to open non-images
    return image_list, file_list

def pepsi(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    red = PIL.Image.open(os.path.join(directory, 'red.png'))
    blue = PIL.Image.open(os.path.join(directory, 'blue.png'))
    template =PIL.Image.open(os.path.join(directory, 'template.png'))
    topp = PIL.Image.open(os.path.join(directory, '1.jpeg'))
    bottomm = PIL.Image.open(os.path.join(directory, '2.jpg'))
        
    # Round the corners with radius = 30% of short side

    top = redlogo(topp,red,template)
    bottom = bluelogo(bottomm,blue,template)
    new_image = template
    new_image.paste(top,(0,0))
    new_image.paste(bottom,(0,0))
    #save the altered image, suing PNG to retain transparency
    new_image_filename = os.path.join(new_directory, 'final' + '.png')
    new_image.save(new_image_filename)    #9b: 