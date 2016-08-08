# Manga-Download
This script could be rendered useful for downloading batch images of manga from [mangareader.net](http://www.mangareader.net).
It is currently at a very basic level as one would have to give options to select a particular manga.
  - URL of the first page in the manga (--site)
  - Number of Chapters (--num_chap)
  - Folder to store the outputs (--folder)

Example
```sh
python manga_download.py --site http://www.mangareader.net/death-note/1/1 --num_chap 10 --folder dn
```

If one would like to convert the images to a pdf, ImageMagik could be used to do so with a single command
```sh
convert *.jpg manga.pdf
```


At present, only python 2.7 is supported. It may be compatible with python 3, but I have not checked.
