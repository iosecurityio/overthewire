# OverTheWire Wargames

## Overview 

The wargames offered by the OverTheWire community can help you to learn and practice security concepts in the form of fun-filled games.

Personally, I learned a lot by repeatedly trying to get as far as I could in a short span of time (eg. seeing what level you can get to over the course of a lunch break).

Everyone recommends to start out with the Bandit challenges and progress from there, working your way up to full blown attack/defense scenarios.

> There are a variety of ways to do every challenge, I will add different methods if they are handy or notable.I don't always do things the same way, BASH is like play-doh :) If you have another method or a way of doing things, submit them!

## Link

- [over the wire: wargames](http://overthewire.org/wargames/)

- [over the wire: wargames - bandit](http://overthewire.org/wargames/bandit/)

---

```python
##################
##################
##################
##################
##################
##################
##################
##################
##################
##################
# SPOILERS BELOW #
##################
##################
##################
##################
##################
##################
##################
##################
##################
##################
```

---

## Levels

### Bandit0

- `ssh bandit0@bandit.labs.overthewire.org -p 2220`

- bandit0 password

- `cat readme`

- boJ9jbbUNNfktd78OOpsqOltutMc3MY1

### Bandit1

- `ssh bandit1@localhost`

- boJ9jbbUNNfktd78OOpsqOltutMc3MY1

- `ls -al`

- `cat ./-`

- CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

### Bandit2

- ssh bandit2@localhost

- CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
- ls -al
- cat spaces\ in\ this\ filename
- UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

### Bandit3

- ssh bandit3@localhost
- UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
- ls -al
- cd inhere
- ls -al
- cat .hidden
- pIwrPrtPN36QITSp3EQaw936yaFoFgAB

### Bandit4

- ssh bandit4@localhost
- pIwrPrtPN36QITSp3EQaw936yaFoFgAB
- ls -al
- cd inhere
- file ./*
- cat ./-file07
- koReBOKuIDDepwhWk7jZC0RTdopnAYKh

### Bandit5

- ssh bandit5@localhost
- koReBOKuIDDepwhWk7jZC0RTdopnAYKh
- ls -al
- cd inhere
- find -size 1033c
- cat ./maybehere07/.file2
- DXjZPULLxYr17uwoI01bNLQbtFemEgo7

### Bandit6

- ssh bandit6@localhost
- DXjZPULLxYr17uwoI01bNLQbtFemEgo7
- find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
- cat /var/lib/dpkg/info/bandit7.password
- HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

### Bandit7

- ssh bandit7@localhost
- ls -al
- grep millionth data.txt
- cvX2JJa4CFALtqS87jk27qwqGhBM9plV

### Bandit8

- ssh bandit8@localhost
- cvX2JJa4CFALtqS87jk27qwqGhBM9plV
- ls -al
- cat data.txt | sort | uniq -u
- UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

### Bandit9

- ssh bandit9@localhost
- UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
- ls -al
- strings data.txt | grep ==
- truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

### Bandit10

- ssh bandit10@localhost
- truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
- ls -al
- base64 -d data.txt
- IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

### Bandit11

- ssh bandit11@localhost
- IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
- ls -al
- cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
- 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

### Bandit12

- ssh bandit12@localhost
- 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
- mkdir /tmp/bamtech && cp data.txt /tmp/bamtech/data && cd /tmp/bamtech
- ls -al
- xxd -r data > data2
- file data2
- mv data2 data2.gz && gunzip data2.gz
- file data2
- bzip2 -d data2
- file data2.out
- mv data2.out data2.gz && gunzip data2.gz
- tar xf data2
- tar xf data5.bin
- file data6.bin
- bzip2 -d data6.bin
- file data6.bin.out
- tar xf data6.bin.out
- file data8.bin
- mv data8.bin data8.gz && gunzip data8.gz
- file data8
- cat data8
- 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

### Bandit13

- ssh bandit13@localhost
- 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
- ls -al
- ssh -i sshkey.private bandit14@localhost
- cat /etc/bandit_pass/bandit14
- 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

### Bandit14

- (continued from Bandit13)
- nc localhost 30000
- 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
- BfMYroe26WYalil77FoDi9qh59eK5xNr

### Bandit15

- ssh bandit15@localhost
- BfMYroe26WYalil77FoDi9qh59eK5xNr
- openssl s_client -connect localhost:30001 -ign_eof
- cluFn7wTiGryunymYOu4RcffSxQluehd

### Bandit16

- ssh bandit16@localhost
- cluFn7wTiGryunymYOu4RcffSxQluehd
- nmap -v localhost -p31000-32000
- nmap -sV localhost -p31046,31518,31691,31790,31960
- 31790 returns data
- openssl s_client -connect localhost:31790 -ign_eof
- cluFn7wTiGryunymYOu4RcffSxQluehd
- mkdir /tmp/allen && echo "
	-----BEGIN RSA PRIVATE KEY-----
	MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
	imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
	Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
	DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
	JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
	x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
	KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
	J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
	d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
	YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
	vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
	+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
	8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
	SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
	HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
	SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
	R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
	Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
	R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
	L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
	blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
	YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
	77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
	dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
	vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
	-----END RSA PRIVATE KEY----- " > cert
- chmod 400 cert
- ssh bandit17@localhost -i cert

### Bandit17

- diff passwords.*
	42c42
	< kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
	---
	> 6vcSC74ROI95NqkKaeEC2ABVMDX9TyUr

### Bandit18

- ssh bandit18@localhost cat readme
- kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
- IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

### Bandit19

- ssh bandit19@localhost
- IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
- ./bandit20-do cat /etc/bandit_pass/bandit20
- GbKksEFF4yrVs6il55v6gwY5aVje5f0j

### Bandit20

- ssh bandit20@localhost
- GbKksEFF4yrVs6il55v6gwY5aVje5f0j
- ls -al
- you need to use tmux to open two terminals, so type tmux and CTRL+B %
- in the left terminal start a listener with nc -l 31337
- enter the password: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
- Jump to the right terminal with CTRL+B right arrow ->
- ./suconnect 31337
- Passwords matched!
- gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

### Bandit21

- ssh bandit21@localhost
- gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
- cd /etc/cron.d
- ls -al
- less /usr/bin/cronjob_bandit22.sh
- cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
- Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

### Bandit22

- ssh bandit22@localhost
- Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
- cd /etc/cron.d/
- ls -al
- mytarget=$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)
- cat /tmp/$mytarget
- jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

### Bandit23

- ssh bandit23@localhost
- jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
- cat /usr/bin/cronjob_bandit24.sh
