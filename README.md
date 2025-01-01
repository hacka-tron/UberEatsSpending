# UberEatsSpending
This is a tool I made for calculating UberEats order spending. [See it in action!](https://www.youtube.com/watch?v=U3GDPXsux74)

## Try it yourself!
[Download the application](https://github.com/hacka-tron/UberEatsSpending/raw/main/Downloads/UberEatsSpending.zip) and going through the following steps: 

1. Open Chrome and login to UberEats. 
   1. This step is important!! Without it you won't be authenticated and your orders can't be tallied.
   2. This step must be done before step 2. If you have already created a copy of your `User Data`, delete it and create a new one after logging in. 
   3. This could probably work for other browsers than Chrome, but you would have to play with [`drivers.py`](./drivers.py) to get it working.
2. Create a copy of your Chrome "User Data" file. You can add it anywhere as you will reference it by its path. The "User Data" folder will usually be found under `C:\Users\[YOUR USER]\AppData\Local\Google\Chrome\User Data`. 
3. Figure out which Chrome profile you used logged in to UberEats on in step 2. For most people it should just be "Default". You can find other profiles in the `User Data` directory.  

Upon completing setup, run this tool with `get_spend <days_to_tally> <user_data_path_from_step_2> <profile-directory_from_step_3>`. So if I you were to add the `User Data` directory to the desktop, the command would look like `get_spend 5 "C:\Users\switch_this_with_your_user\OneDrive\Desktop\User Data" "Default"`
