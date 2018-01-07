---
layout: post
title: Hot to use proxy in Linux
date: '2017-05-08 02:10:04'
tags:
- linux
- proxy
- shell
- tips
---

Thanks for GFW, coders have to overcome difficulties for some resources. Master the skill of proxy became indispensable. Here are some tips for the Linux user.

## WHERE NEED PROXIES
* Browser, Chrome/Firefox/Safari etd.
* Shell, handle http request bypass firewalls

## TOOLS
1. [shadowsocks](https://github.com/shadowsocks)，a fast tunnel proxy
2. [Polipo](https://www.irif.fr/~jch/software/polipo/), a caching web proxy
3. [SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega), Manage and switch between multiple proxies quickly & easily.

## TIPS
* Conver convert socks into an HTTP proxy              
  `polipo socksParentProxy=localhost:PORT daemonise=true`

* Set proxy for shell              
  `export http_proxy="http://127.0.0.1:PORT/"`

* Set proxy for git               
  `git config --global http.proxy 127.0.0.1:PORT`

* Use proxy in python               
`proxies = {
    "http": cf.get('proxy','http://127.0.0.1:PORT'),
    "https": cf.get('proxy','https://127.0.0.1:PORT'),
}
requests.get(url, proxies=proxies)`

