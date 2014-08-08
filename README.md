vagrant_sinatra_hello
=====================

Vagrant setup for sinatra_hello

Install
=====================

To install

```
git clone https://github.com/mzupan/vagrant_sinatra_hello.git
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

The first run of the request counts will give no data since logster needs a mark in the log to work with to give
valid results. So wait till the next run if you ssh in right after bootup of the VM
