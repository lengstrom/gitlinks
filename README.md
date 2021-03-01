# `gitlinks` - Git Powered Go-Links
<p align = 'center'>
    Hosted "<a href="https://yiou.me/blog/posts/google-go-link">Go-Links</a>" via Git and <a href="https://pages.github.com">GitHub Pages</a>
    <br/>
    <code>pip install gitlinks</code>
    <br/>
    <p>
    <img src="static/demo.gif"/>
    </p>
    <p align = 'center'>
        <a href="#setup">Jump to setup</a> | <a href="https://twitter.com/logan_engstrom">Follow me on Twitter</a>
    </p>
</p>

# Quick Overview
<p>
<code>gitlinks</code> is a command line tool that maps custom shortlinks to URLs via 
<a href="https://git-scm.com">Git</a> and <a href="https://pages.github.com">GitHub Pages</a> .
The following table shows example mappings for user <code>lengstrom</code>'s gitlinks repository
<a href="https://github.com/lengstrom/goto">goto</a>:
</p>

| Key           | URL                                                                                   | GitHub Pages Shortlink                                                                        |
| :------------ | :------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------- |
| `zoom`        | <a href="https://mit.zoom.us/j/95091088705">https://mit.zoom.us/j/95091088705</a>     | <a href="http://loganengstrom.com/goto/zoom">http://loganengstrom.com/goto/zoom</a>               |
| `classes/NLP` | <a href="https://canvas.mit.edu/courses/7503">https://canvas.mit.edu/courses/7503</a> | <a href="http://loganengstrom.com/goto/classes/nlp">http://loganengstrom.com/goto/classes/nlp</a> |

<p>
    Here, if user <code>lengstrom</code>
    maps <code>zoom</code> to <a href="https://mit.zoom.us/j/95091088705">https://mit.zoom.us/j/95091088705</a>,
    he (or any other user) can then access it at
    <a href="http://loganengstrom.com/goto/zoom">http://loganengstrom.com/goto/zoom</a>
    (since the GitHub pages site <code>lengstrom.github.io</code> maps to <code>loganengstrom.com</code>).
    We can also organize keys through nesting, such as with <code>classes/NLP</code>.
</p>
<p>
    <code>gitlinks</code> works by <a href="https://github.com/lengstrom/goto/blob/main/index.csv">storing state on GitHub</a>
    and <a href="https://github.com/lengstrom/goto">rendering structured redirects on GitHub pages</a>. Add, remove, and visualize link mappings through the command line!
</p>

```
$ gitlinks set zoom https://mit.zoom.us/j/95091088705
  => Success: Set key "zoom" → "https://mit.zoom.us/j/95091088705".
```
```
$ gitlinks delete zoom
  => Success: Deleted key "zoom".
```
```
$ gitlinks show
  => Checking for changes from remote...
  == GitLinks (Remote: git@github.com:lengstrom/goto.git) ==
  chungus                  →   https://en.wikipedia.org/wiki/Chungus
  classes/18.102           →   http://math.mit.edu/~rbm/18-102-S17/
  classes/6.005            →   http://web.mit.edu/6.031/www/fa18/general/
  classes/nlp              →   https://canvas.mit.edu/courses/7503
  friends/ilyas            →   http://andrewilyas.com
  friends/kwokchain        →   https://twitter.com/antimatter15
  friends/nomo             →   https://noahmoroze.com
  friends/penger           →   http://tonypeng.com
  friends/yang             →   https://yang.money
  papers/bugsnotfeatures   →   https://arxiv.org/abs/1905.02175
  papers/robusttransfer    →   https://arxiv.org/abs/2007.08489
  papers/unadversarial     →   https://arxiv.org/abs/2012.12235
```
<p>
    <code>gitlinks</code> also generates an index page: see 
    http://loganengstrom.com/goto/ as an example.
</p>

# Setup
Configure `gitlinks` in two steps!
## First: Cook up a new GitHub Repository
<p>
First, visit https://github.com/new and choose a short, memorable name like
<code>go</code> for your gitlinks repository. 
</p>
<img src="static/make_repo.png"/>
<p>
Now, check the box "Add a README file" (the repository can't be empty).
</p>
<img src="static/add_readme.png"/>
<p>
Make the repository, then go your repository's settings (e.g. <code>https://github.com/yourusername/repository_name/settings</code>).
Then, scroll down to the GitHub Pages section, and enable it for the `main` branch:
</p>
<img src="static/enable_ghpages.png"/>

## Initialize `gitlinks` locally
<p>
    Install the <code>gitlinks</code> executable via <code>pip</code>: <code>pip install gitlinks</code>. Then, 
    initialize <code>gitlinks</code> to use your repository: <code>gitlinks init remote_url</code>.
    Your <code>remote_url</code> can be found here:
</p>
<img src="static/remote_url.png"/>
<p>
    After this step, you should be able to make go-links to your heart's content.  
</p>

# Big Shoutouts
- Tony Peng ([Twitter](https://twitter.com/iamtonypeng), [Website](http://tonypeng.com)) - for inspiring this project!
- Michael Yang ([Twitter](https://twitter.com/themichaelyang), [Website](http://yang.money)) - for critical contributions including the index page, the fancy arrows, and finding several SEV0 bugs.
- Andrew Ilyas ([Twitter](https://twitter.com/andrew_ilyas), [Website](http://andrewilyas.com))

# License
GPL v3
