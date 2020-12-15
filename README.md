# TrackingGame
Solutions for tracking-game.reaktor.com

### Mission 001: Noise
https://tracking-game.reaktor.com/signal/vs/noise

Using slices in a loop to get slices of 16 characters each and then using set() to remove duplucates.  
The output is a Base64 encoded string. I pipe it into `base64 -d` to get the flag.

```
python3 Mission001.py | base64 -d
Curtisisland
```

### Mission 002: Billion

https://tracking-game.reaktor.com/parts/per/billion

Used rapidtables.com to convert input to ASCII/UTF-8 and saved it as Mission002.json  
Then I just parsed the input to form a list of lists like this:

```
[1007342, 'D87E5645F3C192']
[1007706, 'C522188B90B15B']
[1007424, 'B38587A8372B63']
[1003367, '42A318979448E5']
```

Just by eyeballing the result I assemed that the standard range is around 1,000,000 - 1,010,000, so I just plugged it into my program and got the flag as a string of hex values.  
After that I piped it into `xxd -r -p` to get the flag.

```
python3 Mission002.py | xxd -r -p
KUNGRAD
```