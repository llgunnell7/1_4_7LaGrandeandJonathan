import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def redlogo(original_image,red,template):
    """ resizes the original image to template, creates a mask out of the top portion, and then creates the top portion
    """
    width, height = template.size #defines the size of the picture
    resized_image = original_image.resize((width,height)) #resizes original image to paste it
    
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    rounded_mask.paste(red, (0,0))#paste the red portion of the logo into the mask

    result = PIL.Image.new('RGBA', template.size, (0,0,0,0))
    result.paste(resized_image, (0,0), mask=rounded_mask)#paste the new image, but use the red as a mask
    return result
def bluelogo(original_image,blue,template):
    """ This is the exact same as redlogo, but its for the bottom portion
    """
    width, height = template.size
    resized_image = original_image.resize((width,height))
    
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    rounded_mask.paste(blue, (0,0))
    result = PIL.Image.new('RGBA', template.size, (0,0,0,0))
    result.paste(resized_image, (0,0), mask=rounded_mask)
    return result
def get_images(directory=None):
    """ This was not edited from the source, mask.py from 1.4.5
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
    """ this creates the main pepsi logo from the 1.jpeg and 2.jpg in the directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'pepsi'
    new_directory = os.path.join(directory, 'pepsi')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory) #this step is unneccesary as the lines below do it instead, but in the future we will add support for multiple images  

    #open all of the images for use
    red = PIL.Image.open(os.path.join(directory, 'red.png'))
    blue = PIL.Image.open(os.path.join(directory, 'blue.png'))
    template =PIL.Image.open(os.path.join(directory, 'template.png'))
    topp = PIL.Image.open(os.path.join(directory, '1.jpeg'))
    bottomm = PIL.Image.open(os.path.join(directory, '2.jpg'))
        
    top = redlogo(topp,red,template)#creates the top portion of the pepsi logo
    bottom = bluelogo(bottomm,blue,template)#creates the bottom portion of the pepsi logo
    
    new_image = template#creates a new image based on template
    new_image.paste(bottom,(0,0), mask=bottom)#pastes the top and bottom onto the new image
    new_image.paste(top,(0,0), mask=top)
    
    #save the new image, suing PNG to retain transparency
    new_image_filename = os.path.join(new_directory, 'final' + '.png')
    new_image.save(new_image_filename)    #9b: 