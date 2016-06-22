# Manga-Download
This script could be rendered useful for downloading batch images of manga from [mangareader.net](http://www.mangareader.net).
It is currently at a very basic level as one would have to (1)enter the url of the first page of the manga chapter along with (2)the number of chapters.

The user can decide (3)the name of the folder, where the images will be stored.

All of the information must be changed in the cell titled ``User Specific Data``.

If one would like to convert the images to a pdf, ImageMagik could be used to do so with a single command
```sh
convert *.jpg manga.pdf
```


At present, only python 2.7 is supported. It may be backwards compatible with python 3, but I have not checked.



