# `gitlinks` - Git Powered Go-Links
<p align = 'center'>
    Hosted "<a href="https://yiou.me/blog/posts/google-go-link">Go-Links</a>" via Git and <a href="https://pages.github.com">GitHub Pages</a>
    <br/>
    <code>pip install gitlinks</code>
    <br/>
    <p align = 'center'>
    <img src="static/demo.gif"/>
    </p>
    <p align = 'center'>
        <a href="#setup">Jump to setup</a> | By <a href="https://twitter.com/logan_engstrom">@logan_engstrom</a>
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
    Here, anyone can access the
    <code>zoom</code> link (<a href="https://mit.zoom.us/j/95091088705">https://mit.zoom.us/j/95091088705</a>) at
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
calendly                 →   https://calendly.com/loganengstrom
classes/18.102           →   http://math.mit.edu/~rbm/18-102-S17/
classes/6.005            →   http://web.mit.edu/6.031/www/fa18/general/
ffcv_slack               →   https://ffcv-workspace.slack.com/join/shared_invite/zt-11olgvyfl-dfFerPxlm6WtmlgdMuw_2A#/shared-invite/email
papers/bugsnotfeatures   →   https://arxiv.org/abs/1905.02175
zombocom                 →   https://www.zombo.com
zoom                     →   https://mit.zoom.us/j/95091088705
```

<p>
    <code>gitlinks</code> also generates an index page: see 
    http://loganengstrom.com/goto/ as an example. The big caveat of `gitlinks` is that <b>all of your links are public to anyone on the web</b>, so be careful with what you link!
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
Make the repository, then go your repository's GitHub pages settings: 
    <code>https://github.com/yourusername/repository_name/settings/pages</code>) and <b>enable GitHub pages</b> for the <code>main</code> branch:
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

# License
GPL v3
