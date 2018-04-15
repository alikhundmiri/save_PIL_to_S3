"""
TODO:
In this file, I am trying to create a new image, using PIL, and upload that image to AWS S3.
"""
from PIL import Image
import os
import sys

#  stringify the image (?)
from io import StringIO, BytesIO

import boto3
from botocore.client import Config

import s3_upload as s
from s3_upload import s3

i__width = 600
i__height = 200


def get_image():
	# make the base image
	i__  = Image.new('RGB', (i__width, i__height*3))

	# generate 3 images
	i__1 = Image.new('RGB', (i__width, i__height), (125, 47, 0))
	i__2 = Image.new('RGB', (i__width, i__height), (161, 60, 0))
	i__3 = Image.new('RGB', (i__width, i__height), (196, 73, 0))

	# paste those 3 images on top of the base images after the height of previous image.
	i__.paste(im=i__1, box=(0, 0))
	i__.paste(im=i__2, box=(0, i__height))
	i__.paste(im=i__3, box=(0, i__height*2))
	return i__

# This is working!
def sample_upload(image):
	# Enter the image name
	IMAGE_NAME = 'sample_3'
	# Enter the bucket name
	BUCKET_NAME = ''
	# Create a buffer
	buffer = BytesIO()
	# save the image onto buffer
	image.save(buffer, 'PNG')
	# reset the position to zero
	buffer.seek(0) #If this line is not there, the process will get stuck after printing "Done". So keep it.

	s.s3.Bucket(BUCKET_NAME).put_object(Key=IMAGE_NAME+".png", Body=buffer)

def main():
	image = get_image()

	sample_upload(image)
	

	# image.show()



if __name__ == '__main__':
	main()