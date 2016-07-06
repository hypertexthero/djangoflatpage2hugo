# djangoflatpages2hugo

Script to convert Django [flatpages](https://docs.djangoproject.com/en/1.9/ref/contrib/flatpages/) to [Hugo](http://gohugo.io/) Markdown files with YAML frontmatter

I needed to export a lot of entries stored in the SQLite database of my [previous Django site](http://github.com/hypertexthero/hypertexthero.com) for importing into the new [Hugo-powered SimonGriffee.com](/notebook/website-redesign-july2016/). 

Thankfully, [Sam Kingston](https://github.com/sjkingo) had already [written a script](https://github.com/sjkingo/mezzanine2jekyll) to export [Mezzanine](http://mezzanine.jupo.org/) blog posts to [Jekyll](https://jekyllrb.com/), so I modified it to make [djangoflatpage2hugo.py](https://github.com/hypertexthero/djangoflatpage2hugo), below. 

To use it:

1. Save `djangoflatpage2hugo.py` below in: 
    <pre><code>yourdjangoproject/
                management/
                        commands/
                                djangoflatpage2hugo.py</code></pre>.
2. Make sure there are `__init__.py` files in both the `management` and `commands` folders.
3. Run the following in your terminal: `python manage.py djangoflatpage2hugo /chosen/output/directory/`.
4. Find the converted .md files in the `/chosen/output/directory`.
