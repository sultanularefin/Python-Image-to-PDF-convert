from PIL import Image


def main():
    # Load all the images in dedicated variable
    image0 = Image.open('../appointment_mindfork/0.jpg')
    image1 = Image.open('../appointment_mindfork/1.jpg')
    image2 = Image.open('../appointment_mindfork/2.jpg')
    image3 = Image.open('../appointment_mindfork/3.jpg')
    image4 = Image.open('../appointment_mindfork/4.jpg')
    image5 = Image.open('../appointment_mindfork/5.jpg')
    image6 = Image.open('../appointment_mindfork/6.jpg')
    image7 = Image.open('../appointment_mindfork/7.jpg')
    image8 = Image.open('../appointment_mindfork/8.jpg')
    image9 = Image.open('../appointment_mindfork/9.jpg')
    image10 = Image.open('../appointment_mindfork/10.jpg')
    image11 = Image.open('../appointment_mindfork/11.jpg')
    image12 = Image.open('../appointment_mindfork/12.jpg')
    image13 = Image.open('../appointment_mindfork/13.jpg')
    image14 = Image.open('../appointment_mindfork/14.jpg')
    

    # Convert all the images to RGB
    image0.convert('RGB')
    image1.convert('RGB')
    image2.convert('RGB')
    image3.convert('RGB')
    image4.convert('RGB')
    image5.convert('RGB')
    image6.convert('RGB')
    image7.convert('RGB')
    image8.convert('RGB')
    image9.convert('RGB')
    image10.convert('RGB')
    image11.convert('RGB')
    image12.convert('RGB')
    image13.convert('RGB')
    image14.convert('RGB')
    



    # List of image variables (without the first image)
    # Maintain image order if necessary
    # I'm not including my desired order's first image in the list
    # My desired first image is "image1"
    imageList = [
        # image0, 
        image1,
        image2,
        image3,
        image4,
        image5,
        image6, 
        image7,
        image8,
        image9,
        image10,
        image11,
        image12,
        image13,
        image14,
        ]

    # Creation of PDF
    fileName = 'Flowers.pdf'  # Filename of PDF
    # Now is the perfect time to use my first image
    # The PDF will organize Flower images in below order
    # image1, image2, image3, image4, image5
    # image1 is showing first because of using this for the saving process
    # image1.save(fileName, save_all=True, append_images=imageList)
    image0.save(fileName, save_all=True, append_images=imageList)

    # End
    print('Done')


if __name__ == '__main__':
    main()
