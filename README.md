## Diff2RSS
A Python script that converts GitHub Commits Atom into Diffs and generates an
RSS feed for each commit showing the diff.

## Overview

Transform GitHub commits Atom feed into a format that highlights the actual code
changes, allowing users to easily monitor updates in a traditional RSS reader
like Feedly or InoReader.

## Functionality

1. Grabs an Atom feed from GitHub (https://github.com/:owner/:repo/commits.atom)
2. Parses all commits to obtain the diff
3. Generates an RSS feed for each commit, displaying the corresponding diff

## 📸 Shots
![alt text](metadata/image.png)

## Installation

You can easily get started by pulling the latest image from GitHub Container Registry (GHCR):

```bash
docker pull chkpwd/diff2rss:latest
```

Once you have the container installed, you're ready to go!

## Usage

### Add to your favorite RSS Reader

Open your preferred RSS reader and create a new subscription. The URL should be
in the following format:
``https://github.com/:owner/:repo/commits.atom``

Specifying the branch:
``https://github.com/:owner/:repo/commits/:branch.atom``

### Manual Testing
```
curl -s -X GET https://github.com/:owner/:repo/commits.atom
```

#### Response
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <title>GitHub Feed for Recent Commits to iac:main</title>
    <link>https://github.com/chkpwd/iac/commits/main</link>
    <description>Latest entries from GitHub repository</description>
  </channel>
</rss>
... # Removed for brevity
```
