import sys
import json
import pprint
import random
from ua_parser import user_agent_parser
from random import randint, uniform
import numpy as np
from faker import Faker
import hashlib

md = hashlib.md5()
pp = pprint.PrettyPrinter(depth=6)
fake = Faker()

def loadMobileUA():
    file = open("lib/mobileUserAgents.txt", "r")
    x = []
    for item in file:
        x.append(item.split('\n')[0])
    return np.array(x)
def loadDomainsList():
    file = open("lib/topsites.txt", "r")
    x = []
    for item in file:
        x.append(item.split('\n')[0])
    return np.array(x)
def loadIABCategories():
    with open("lib/IAB-categories.json") as iabc_json:
        categories = json.load(iabc_json)
        return categories
def getRandMD5():
    return str(fake.md5(raw_output=False))
def randAuctionType():
    atList = ['1'] + ['2'] * 95
    return random.choice(atList)
def getIABCategories():
    randomCategories = []
    for x in range(0,randint(1,6)):
        randCat = random.choice(iabCategories.keys())
        if randCat not in randomCategories:
            randomCategories.append(randCat)
    return randomCategories
def getBlockedAdvertisers():
    randomAdvertisers = []
    for x in range(0,randint(3,10)):
        randAdvertiser = random.choice(topDomainTlds)
        if randAdvertiser not in randomAdvertisers:
            randomAdvertisers.append(randAdvertiser)
    return randomAdvertisers
def getRandomUA(uaList):
    return random.choice(uaList)
def getRandBidFloor():
    return round(uniform(0, 2.0),2)
def getMostlyFalse():
    boolean = [0] * 9 + [1]
    return random.choice(boolean)
def getRandomBannerSizes():
    randBanner = {}
    bannerSizes = [
     { "w": 300, "h": 250 },
     { "w": 250, "h": 250 },
     { "w": 240, "h": 400 },
     { "w": 336, "h": 280 },
     { "w": 180, "h": 150 },
     { "w": 300, "h": 100 },
     { "w": 720, "h": 300 },
     { "w": 468, "h": 60 },
     { "w": 234, "h": 60 },
     { "w": 88, "h": 31 },
     { "w": 120, "h": 90 },
     { "w": 120, "h": 60 },
     { "w": 120, "h": 240 },
     { "w": 125, "h": 125 },
     { "w": 728, "h": 90 },
     { "w": 160, "h": 600 },
     { "w": 120, "h": 600 },
     { "w": 300, "h": 600 }
    ]
    randIndex = randint(0,len(bannerSizes) -1)
    return bannerSizes[randIndex]
def getRandomAdPosition():
    # 0 Unknown
    # 1 Above the Fold
    # 2 DEPRECATED - May or may not be initially visible depending on screen size/resolution.
    # 3 Below the Fold
    # 4 Header
    # 5 Footer
    # 6 Sidebar
    # 7 Full Screen
    adPositionList = [0] * 3 + [1] * 10 + [2] + [3] * 10 + [4] * 2 + [5] * 2 + [6] * 4 + [7]
    return random.choice(adPositionList)
def getRandomBlockedAdType():
    # 1 XHTML Text Ad (usually mobile)
    # 2 XHTML Banner Ad. (usually mobile)
    # 3 JavaScript
    # 4 iframe
    bannerTypes = [1] + [2] + [3] + [4] * 5
    blockedBannerTypes = []
    for x in range(0,randint(1, 2)):
        bannerType = random.choice(bannerTypes)
        if bannerType not in blockedBannerTypes:
            blockedBannerTypes.append(bannerType)
    return blockedBannerTypes
def getRandomBlockedCreativeAttrs():
    # 1 Audio Ad (Auto-Play)
    # 2 Audio Ad (User Initiated)
    # 3 Expandable (Automatic)
    # 4 Expandable (User Initiated - Click)
    # 5 Expandable (User Initiated - Rollover)
    # 6 In-Banner Video Ad (Auto-Play)
    # 7 In-Banner Video Ad (User Initiated)
    # 8 Pop (e.g., Over, Under, or Upon Exit)
    # 9 Provocative or Suggestive Imagery
    # 10 Shaky, Flashing, Flickering, Extreme Animation, Smileys
    # 11 Surveys
    # 12 Text Only
    # 13 User Interactive (e.g., Embedded Games)
    # 14 Windows Dialog or Alert Style
    # 15 Has Audio On/Off Button
    # 16 Ad Provides Skip Button (e.g. VPAID-rendered skip button on pre-roll video)
    # 17 Adobe Flash
    bannerAttrs = [1] + [2] + [3] + [4] + [5] + [6] + [7] + [8] + [9] * 10 + [10] * 10 + [11] + [12] + [13] + [14] * 10 + [15] + [16] + [17] * 10
    blockedBannerAttrs = []
    for x in range(0,randint(2, 4)):
        bannerType = random.choice(bannerAttrs)
        if bannerType not in blockedBannerAttrs:
            blockedBannerAttrs.append(bannerType)
    return blockedBannerAttrs
def getSupportedAPIFrameworks():
    # 1 VPAID 1.0
    # 2 VPAID 2.0
    # 3 MRAID-1
    # 4 ORMMA
    # 5 MRAID-2
    apiFrameworks = [1] + [2] + [3] * 100 + [4] + [5]
    supportedAPIFrameworks = []
    for x in range(0,randint(1, 2)):
        apiFramework = random.choice(apiFrameworks)
        if apiFramework not in supportedAPIFrameworks:
            supportedAPIFrameworks.append(apiFramework)
    return supportedAPIFrameworks
def getCompanyName():
    return str(fake.company())
def getRandomVersion():
    return "{0}.{1}.{2}".format(fake.random_digit(),fake.random_digit()
,fake.random_digit())
def getRandomPublisher():
    pub = {}
    pub['domain'] = random.choice(topDomainTlds)
    pub['name'] =   pub['domain'].split(".")[0]
    pub['bundle'] =  "com.{0}.app".format(pub['name'])
    md.update(pub['name'])
    pub['id'] =  md.hexdigest()
    return pub


# Load external data
iabCategories = loadIABCategories()
mobileUserAgents = loadMobileUA()
topDomainTlds = loadDomainsList()
randDimensions = getRandomBannerSizes()
randPublisher = getRandomPublisher()
# sys.exit()
randomUserAgent = getRandomUA(mobileUserAgents)
profile = fake.profile(['sex', 'birthdate', 'current_location'])
uaObject = user_agent_parser.Parse(randomUserAgent)
deviceMake = uaObject.get('device').get('brand')
deviceModel = uaObject.get('device').get('model')
ip = fake.ipv4(network=False)
geoLat = str(profile.get('current_location')[0])
geoLon = str(profile.get('current_location')[1])
# pp.pprint(uaObject)

#
# sys.exit()
req = {
    "id": getRandMD5(),
    "at": randAuctionType(),
    "bcat": getIABCategories(),
    "badv": getBlockedAdvertisers(),
    "imp": [
        {
            "id": "1",
            "bidfloor": getRandBidFloor(),
            "instl": getMostlyFalse(),
            "tagid": getRandMD5(),
            "banner": {
                "w": randDimensions['w'],
                "h": randDimensions['h'],
                "pos": getRandomAdPosition(),
                "btype": getRandomBlockedAdType(),
                "battr": getRandomBlockedCreativeAttrs(),
                "api": getSupportedAPIFrameworks()
            }
        }
    ],
    "app": {
        "id": getRandMD5(),
        "name": getCompanyName(),
        "cat": getIABCategories(),
        "ver": getRandomVersion(),
        "bundle": randPublisher['bundle'],
        "storeurl": "https://itunes.apple.com/id{0}".format(fake.random_int(428677149, 999999999)),
        "publisher": {
            "id": randPublisher['id'],
            "name": randPublisher['name'],
            "domain": randPublisher['domain']
        }
    },
    "device": {
        "dnt": 0,
        "ua": randomUserAgent,
        "ip": ip,
        "ifa": "AA000DFE74168477C70D291f574D344790E0BB11",
        "carrier": "VERIZON",
        "language": "en",
        "make": deviceMake,
        "model": deviceModel,
        "os": "uaObject.get('os').get('family')",
        "osv": "6.1",
        "js": 1,
        "connectiontype": 3,
        "devicetype": 1,
        "geo": {
            "lat": geoLat, "lon": geoLon,
            "country": fake.country_code(),
            "metro": "803",
            "region": fake.state_abbr(),
            "city": fake.city(),
            "zip": fake.zipcode()
        }
    },
    "user": {
        "id": "ffffffd5135596709273b3a1a07e466ea2bf4fff",
        "yob": profile.get('birthdate')[:4],
        "gender": profile.get('sex')
    }
}

 pp.pprint(req)
