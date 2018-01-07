---
layout: post
title: 'Golang: convert any form of string  to int'
date: '2017-05-09 03:11:57'
tags:
- golang
---

Last week, Supervisor gave me a task that reduces the output of log. Logs are information about millions of devices. Each device has a unique key. Convert key into int, and mod it with a special number, we could filter target device to log.

mod operation in golang is %. The challenge is convert key. Here are the code to convert any form of string to int. 

`func stringToInt(s string) int64 {
	var binString string
	for _, c := range s {
		binString = fmt.Sprintf("%s%b", binString, c)
	}
	number, _ := strconv.ParseInt(binString, 2, 64)
	return number
}`

Clike [here](https://play.golang.org/p/T9rkTsrc0B) to run a online demo

Reforence:
http://stackoverflow.com/questions/37349071/golang-how-to-convert-string-to-binary-representation/37350639