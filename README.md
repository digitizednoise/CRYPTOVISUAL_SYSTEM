# CRYPTOVISUAL_SYSTEM

***FOR EMPLOYMENT PURPOSES ONLY***

CRYPTOVISUAL is a realtime global cryptocurrency chart created with TouchDesigner and Python. Chart displays the top ten most dominating cryptocurrencies in the market. Visual displays coins ranked in order starting from coin with the highest global percentage.

![TDMovieOut 4](https://user-images.githubusercontent.com/68321762/150186720-68c434cc-2f40-4adb-b94e-6aa87f143747.png)

Prices and current ranking are updated every minute. Current market percentage is updated every 5 minutes. OHLC (red / green price color) is updated every 30 minutes; but the time can be adjusted from within Touchdesigner by adjusting the  TimerCHOP values.

![TDMovieOut 5](https://user-images.githubusercontent.com/68321762/150187042-554c8726-5011-47ab-baa6-e5f59bbb825e.png)

Data is called using REQUESTS library. Data is fetched using <a href = "https://nomics.com/" class = "linkdescription">NOMICS.COM</a> API. JSON is then parsed using the JSON dat rather than the usual JSON.parse() method. Data is read and finally sent to the front end (TOP operators) to be vizualized.

![TDMovieOut 8](https://user-images.githubusercontent.com/68321762/150191893-239eeac7-b7a4-481f-af20-165a03853fad.png)

Inside CRYPTOVISAL there is a script that I created for myself that allows me to upload and tweet daily to a twitter bot I created all with the simple click of the TWEET button:

https://twitter.com/dn_CRYPTOVISUAL

![TDMovieOut 6](https://user-images.githubusercontent.com/68321762/150187695-89d98f66-ae95-485f-8f05-cf69a176e158.png)
