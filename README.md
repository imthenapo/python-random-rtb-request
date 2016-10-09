# Python Random RTB Request

###### What and why
This is a very basic randomized RTB Request generator using python library [Faker](https://github.com/joke2k/faker).

The RTB object is built according to [IAB Open RTB Protocol 2.4](http://www.iab.com/wp-content/uploads/2016/01/OpenRTB-API-Specification-Version-2-4-DRAFT.pdf)

I built this for usage with [Locust - distributed load testing tool](http://locust.io) but it isn't implemented yet
###### Installation
```
git clone https://github.com/imthenapo/python-random-rtb-request.git
cd python-random-rtb-request
pip install ua_parser random numpy faker
```

###### Notes

Some code functions are customized to return common values for a 'mobile'  RTB Request

i.e. the following function uses a mobile only useragent list:

```python
def loadMobileUA():
    file = open("lib/mobileUserAgents.txt", "r")
    x = []
    for item in file:
        x.append(item.split('\n')[0])
    return np.array(x)
 ```
so change that according to your needs
