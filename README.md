# page_viewsAdder   
A python script that generate views on a page using Firefox   
----------

This is a simple script that uses selenium webdriver and firefox to add views on a page. What is does is to automatically open-close a new Firefox window for a number of times (provided by the user). 

## Requirements

 - Firefox (latest version)
 - Python 2.7.*
 - Python Selenium (see bellow for installation guide)
 - Ubuntu >= 14.04 (it is not tested on other environments)

To install selenium type on terminal (maybe you'll need **sudo** privileges):

```
pip install selenium
```

## Usage

To run the script type:
```
python viewsAdder.py <url> <Number>
```

where **< url >** is the page url you want to add the views and **< Number >** is the number of views you want to add.

## Acknowledgements

You might think that open-close a firefox window multiple times, will have an impact on your computer speed. I tested it on my low spec machine (2.0 GHz Intel Pentium Inside, 2 Gb RAM) and I haven't seen any drawbacks on the speed. Just don't use any other program while running the script.

## License

This script is licensed under [MIT](https://github.com/GeorgeGks/page_viewsAdder/blob/master/LICENSE).
