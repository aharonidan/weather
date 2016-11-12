## Installation and Usage Instructions

This code implements a simple web service to retrieve weather forecast information.

A live server is running at http://weatherf.herokuapp.com/.

To run the server locally download the files and run `python app.py`.

The attached London weather forecast.json comes from www.openweathermap.org. The data is taken from this file.

The following options are provided:

#### A general summary of the weather:
`curl http://<host:ip>/weather/london/<date>/<hour minute>/`

##### Note, temperature converted from Kelvin to C and rounded up.
e.g. `curl http://<host:ip>/weather/london/20160706/0900/`
```
{
  "description": "few clouds",
  "temperature": "15C",
  "pressure": "1028.12",
  "humidity": "88%"
}
```

#### Ask for individual pieces of information:

`curl http://<host:ip>/weather/london/<date>/<hour minute>/temperature`

e.g. `curl http://<host:ip>/weather/london/20160706/0900/temperature/`
```
{
  "temperature": "15C"
}
```

`curl http://<host:ip>/weather/london/<date>/<hour minute>/pressure`

e.g. `curl http://<host:ip>/weather/london/20160706/0900/pressure/`
```
{
  "pressure": "1028.12"
}
```

`curl http://<host:ip>/weather/london/<date>/<hour minute>/humidity`

e.g. `curl http://<host:ip>/weather/london/20160706/0900/humidity/`
```
{
  "humidity": "88%"
}
```

##### When no data is found:
`curl http://<host:ip>/weather/london/17670812/0900/temperature`
```
{
  "status": "error", "message": "No data for 1767-08-12 09:00"
}
```
