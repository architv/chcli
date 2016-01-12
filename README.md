Challenge CLI
=====

[![PyPI version](https://badge.fury.io/py/challenge-cli.svg)](https://badge.fury.io/py/challenge-cli)

Programming Challenges for Hackers - a CLI for all the programming challenges. 

![](http://i.imgur.com/F7BbEH2.png)

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
$ challenges --active 1 # opens the first active challenge in your browser
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
$ challenges --hiring # get all the hiring challenges
```

### Get challenges from all platforms with a set time period

```bash
$ challenges -t 2 # get all the active challenges and upcoming challenges which start in the next 2 days
```

### Help
```bash
$ challenges --help
```

### Platform and Platform codes

- TC: topcoder.com
- HR: hackerrank.com
- CF: codeforces.com
- HE: hackerearth.com
- CC: codechef.com
- GCJ: Google Code Jam
- KA: kaggle.com

For a full list of supported platform and platform codes [see this](challenges/platformids.py).

Demo
====

### Active Challenges
![](http://i.imgur.com/Siedm4R.gif)

### Open a challenge in browser
![](http://i.imgur.com/mxsrc8C.gif)

### Hiring Challenges
![](http://i.imgur.com/c30BEqG.gif)

### Short Challenges from a particular list of platform
![](http://i.imgur.com/SKQgona.png?1)

### Upcoming Challenges within 1 day
![](http://i.imgur.com/3mX7YGh.png)

Todo
====
- [ ] Fix alignment issues


Licence
====
Open sourced under [MIT License](LICENSE)

Support
====
If you like my work, please support the project by donating.

- https://gratipay.com/~architv
