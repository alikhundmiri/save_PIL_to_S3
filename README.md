# save_PIL_to_S3

## what is this!

This is a code to save image to AWS S3.

I have been trying to find a solution which works for quite a while, and after months of searching over the internet, I found a solution which works.


## Whats in the box!

This entire repository is a virtualenv.

## Todo before running

Install all the libraries listed in `requirements.txt`

`pip install -r requirements.txt`

## How to use.

To use it, follow these steps.

1. Dowlnoad the repository on your local machine, and activate the virtualenv.
	- `source bin/activate`
2. Open the file `s3_upload.py` in your text editor,
	- Enter your `ACCESS_KEY_ID`, and `ACCESS_SECRET_KEY`.
3. Open the file `simple_image_upload_0.py` in your text editor,
	- Enter the bucket name. on line number `42`.
4. Run the script `simple_image_upload_0.py`

## Wha does this script does!

The following events takes place.
1. A new image in created using `PIL`
	- This image consists of three images (different shades or brown(?)) stiched together.
2. This new image is saved in side of `buffer`, which is `BytesIO()`
3. Buffer is reset to 0. (no idea why this is necessary, but it is. :/)
4. Image is uploaded to your bucket.


## Thanks
- (python-aws-s3 by keithweaver)[https://github.com/keithweaver/python-aws-s3]

