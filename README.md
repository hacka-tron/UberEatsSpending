# UberEatsSpending
This is a tool I made for calculating UberEats order spending. See it in action at https://www.youtube.com/watch?v=U3GDPXsux74

## Try it yourself!
You can try this tool out yourself by downloading this project and going through the following steps. It requries a bit of setup, but shouldn't be too difficult. 

1. Download [Selenium Webdriver for  Python](https://pypi.org/project/selenium/#files).
2. Open Chrome and login to UberEats. 
   1. This step is important!! Without it you won't be authenticated and your orders can't be tallied.
   2. This step must be done before step 3. If you have already created a copy of your `User Data`, delete it and create a new one afer logging in. 
   3. This could probably work for other browsers than Chrome, but you would have to play with [`test_install_drivers.py`](./test_install_drivers.py) to get it working.
3. Create a copy of your Chrome "User Data" file, and add it to this UberEatsSpending directory. The "User Data" folder will usually be found under `C:\Users\[YOUR USER]\AppData\Local\Google\Chrome\User Data`
4. Figure out which Chrome profile you logged in to UberEats on in step 2. If you only have 1 profile, or used your main Chrome profile, it should just be "Default". You can find other profiles in the `User Data` directory.  
5. Add the COPPIED directory, e.g. C:\Code\UberEatsSpending\User Data, and the profile used to the marked fields in [`get_spend.py`](./get_spend.py)

Upon completing setup, run this tool with `python [PATH TO DIR]/get_spend.py`