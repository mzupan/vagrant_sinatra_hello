vagrant_sinatra_hello
=====================

Vagrant setup for sinatra_hello

Install
=====================

To install

```
git clone git@github.com:mzupan/vagrant_sinatra_hello.git
cd vagrant_sinatra_hello
vargrant up --provision
```

This should have everything up and running on port 8080 localhost so to test

```
curl http://localhost:8080/
```

You should get something like 

```
Mikes-MacBook-Pro:pagerduty mike$ curl http://localhost:8080/
Hello! The current time is 18:59
```

To view logs for type of requests per 5 minutes run the following

```
vagrant ssh
tail -f ~/requests.log
```
