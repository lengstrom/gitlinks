# `gitlinks` - Git Powered Go Links!
<p align = 'center'>
    Map memorable keys to URLS using Git and <a href="https://pages.github.com">GitHub Pages</a>
    <br/>
    <code>pip install gitlinks</code>
</p>

# Quick Overview
`gitlinks` is a command line tool that maps keys to URLs via 
<a href="https://git-scm.com">Git</a> and [GitHub Pages](https://pages.github.com).
The following table shows example mappings for user `lengstrom`:

| Key           | Url                                                                                   | GitHub Pages Reference                                                                        |
| :------------ | :------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------- |
| `zoom`        | <a href="https://mit.zoom.us/j/95091088705">https://mit.zoom.us/j/95091088705</a>     | <a href="http://loganengstrom.com/go/zoom">http://loganengstrom.com/go/zoom</a>               |
| `classes/NLP` | <a href="https://canvas.mit.edu/courses/7503">https://canvas.mit.edu/courses/7503</a> | <a href="http://loganengstrom.com/go/classes/nlp">http://loganengstrom.com/go/classes/nlp</a> |

Here, if user `lengstrom`
maps `zoom` to <a href="https://mit.zoom.us/j/95091088705">https://mit.zoom.us/j/95091088705</a>,
he (or any other user) can then access it at
<a href="http://loganengstrom.com/go/zoom">http://loganengstrom.com/go/zoom</a>
(since the GitHub pages site `lengstrom.github.io` maps to `loganengstrom.com`).
We can also organize keys through nesting, such as with `classes/NLP`.

# EZ Setup
Setup `gitlinks` in two easy steps!
## First: Cook up a new GitHub Repository
<p>
First, visit https://github.com/new and choose a short, memorable name like
<code>go</code> for your repository. Remember, a short shortlink <code>key</code> will reside at
<code>yourusername.github.io/repository_name/key</code>!
</p>
<img src="static/make_repo.png"/>
<p>
Now, check the box "Add a README file".
</p>
<img src="static/add_readme.png"/>
<p>
Make the repository, then go your repository's settings (e.g. <code>https://github.com/yourusername/repository_name/settings</code>).
Then, scroll down to the GitHub Pages section, and enable it for the `main` branch:
</p>
<img src="static/enable_ghpages.png"/>

## Initialize `gitlinks` locally
<p>
    Install the `gitlinks` executable via `pip`: `pip install gitlinks`. Then, 
    initialize `gitlinks` to use the repository above: `gitlinks init <remote url>`---where your remote URL
    can be found here:
</p>
<img src="static/remote_url.png"/>
<p>
    Then, you can add, remove, and visualize link mappings through the command line:
</p>

```
$ gitlinks set zoom https://mit.zoom.us/j/95091088705
  => Checking for changes from remote...
  => Rebuilding HTML...
  => Committing and pushing...
  => Success: Set key "zoom" → "https://mit.zoom.us/j/95091088705".
```
```
$ gitlinks show
  => Checking for changes from remote...
  == GitLinks (Remote: git@github.com:lengstrom/go.git) ==
  classes/nlp     →   https://canvas.mit.edu/courses/7503
  unadversarial   →   https://arxiv.org/abs/2012.12235
  zoom            →   https://mit.zoom.us/j/95091088705
```

# Shoutouts
- Tony Peng ([Twitter](https://twitter.com/iamtonypeng), [Website](http://tonypeng.com)) - for inspiring this project!
- Michael Yang ([Twitter](https://twitter.com/themichaelyang), [Website](http://yang.money)) - for some massive PRs and aesthetics expertise!

# License
GPL v3
