## `gitlinks` - Git Powered Go Links!
Map memorable keys to URLS using Git and [GitHub Pages)](https://pages.github.com).

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
- Make a new repository at https://github.com/new with a short, memorable name (Remember: a shortlink `<key>` will reside at
`<username>.github.io/<repository name>/<key>`).
- Install the `gitlinks` executable via `pip`: `pip install gitlinks`
- 

## Shoutouts
- Michael Yang
- Noah Moroze
- Shoutouts to: @tony peng 

## License
GPL v3
