from setuptools import setup,find_packages
setup(
    name = "canova",
    version = "1.0",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    
    #metadata for upload to PyPI
    author = "JerryHao",
    author_email = "haombio@gmail.com",
    description = "This is canova python package",

)
