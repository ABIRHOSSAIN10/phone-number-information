import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='phoneinfo',  

     version='0.1',

     scripts=['phoneinfo'] ,

     author="ABIR HOSSAIN",

     author_email="abirhossain200019@gmail.com",

     description="this is Phone number information tool",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/ABIRHOSSAIN10/phone-number-information",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",

     ],

 )
