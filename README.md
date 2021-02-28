## `gitlinks` - Git Powered Go Links!
Map memorable keys to URLS using Git and [GitHub Pages)](https://pages.github.com): `pip install gitlinks`.

## Quick Overview
`gitlinks` is a command line tool that maps keys to URLS via 
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

## EZ Setup
Setup `gitlinks` in two easy steps!
### Cook up a new GitHub Repository
<p>
First, open up https://github.com/new and choose a short, memorable name (Remember: a shortlink `<key>` will reside at
`<username>.github.io/<repository name>/<key>`) for your repository. The name "go" is a nice start! 
</p>
<img style="border:1px solid black" src="static/make_repo.png"/>
<p>
Now, check the box "Add a README file".
</p>
<img style="border:1px solid black" src="static/add_readme.png"/>
<p>
Make the repository, then go your repository's settings (e.g. `https://github.com/<yourusername>/<repository name>/settings`).
Then, scroll down to the GitHub Pages section, and enable it for the `main` branch:
</p>
<img style="border:1px solid black" src="static/enable_ghpages.png"/>

### Initialize `gitlinks` locally
Install the `gitlinks` executable via `pip`: `pip install gitlinks`. Then, 
initialize `gitlinks` to use the repository above: `gitlinks init <remote url>`---where your remote URL
can be found here:
<img style="border:1px solid black" src="static/remote_url.png"/>

## Shoutouts
- Tony Peng ([Twitter](https://twitter.com/iamtonypeng), [Website](http://tonypeng.com)) - for inspiring this project!
- Michael Yang ([Twitter](https://twitter.com/themichaelyang), [Website](http://yang.money)) - for some massive PRs and aesthetics expertise!

## License
GPL v3
