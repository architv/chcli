Soccer CLI
=====

[![PyPI version](https://badge.fury.io/py/challenge-cli.svg)](https://badge.fury.io/py/challenge-cli)

Programming Challenges for Hackers - a CLI for all the programming challenges. 

![](http://imgur.com/R3OMV0A)

Install
=====

### Using `pip`

```bash
$ pip install challenge-cli
````

### Build from source


```bash
$ git clone git@github.com:architv/chcli.git
$ cd chcli
$ python setup.py install
```

Usage
====

### Get active challenges

```bash
$ challenges --active
$ challenges --active -p HR -p TC # get active challenges from HackerRank(HR) and topcoder(TC).
```

### Get upcoming challenges

```bash
$ challenges --upcoming
```

### Open a challenge in browser

```bash
$ challenges --active <challenge_id> # opens the first active challenges in your browser
```

### Get upcoming challenges from a particular platform

```bash
$ challenges --upcoming -p HR -p TC # HR and TC are platform code for HackerRank and TopCoder Respectively
```

### Get short challenges

```bash
$ challenges --short -p CF # get all the short challenges from codeforces
```

### Get hiring challenges

```bash
$ challenges --hiring

### Get challenges from all platforms with a set time period

```bash
$ challenges -t 2 # scores for all the platforms begining in the active or begining in the next 2 days
```

### Help
```bash
$ challenges --help
```

### Team and team codes

For a full list of supported platform and platform codes [see this](challenges/platformids.py).

Demo
====

### Active Challenges
![](http://imgur.com/Siedm4R)

### Open a challenge in browser
![](http://i.imgur.com/Peb9yga.gif)

### Hiring Challenges
![](http://imgur.com/c30BEqG)

### Short Challenges from a particular list of platform
![](http://i.imgur.com/SKQgona.png?1)

### Upcoming Challenges within 1 day
![](http://i.imgur.com/3mX7YGh.png)

Todo
====
- [ ] Fix allignment issues


Licence
====
Open sourced under [MIT License](LICENSE)

Support
====
If you like my work, please support the project by donating.

- https://gratipay.com/~architv
