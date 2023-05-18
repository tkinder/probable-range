import csv
import csv as my_csv
from matplotlib import colors
from matplotlib.pyplot import plot
import yfinance as yf
import pandas as pd
from pandas.tseries.offsets import BDay
import math
import google.oauth2
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime, time, timedelta
import json
import os
import configparser
import tradingview_ta
from tradingview_ta import TA_Handler, Interval
import plotly
import plotly.graph_objs as go

""" # Read the configuration file
config = configparser.ConfigParser()
config.read('C:/Python311/config.ini')

# Get the value of the PYTHONPATH variable
pythonpath = config.get('myapp', 'PYTHONPATH')

# Set the PYTHONPATH environment variable
os.environ['PYTHONPATH'] = pythonpath """

# Set up the OAuth 2.0 flow object and run the authorization flow

flow = InstalledAppFlow.from_client_secrets_file(
    "C:/Python311/djia_probable_range_blogger/client_secret_36700183469-algn87srtkhcbssuubj821r5aurbdfh5.apps.googleusercontent.com.json",
    scopes=["https://www.googleapis.com/auth/blogger"],
)
creds = flow.run_local_server(port=0)

# Declare the OAuth 2.0 scope used with Blogger API

SCOPES = "https://www.googleapis.com/auth/blogger"

# Get the client ID, client secret, and refresh token from the credentials object
client_id = creds.client_id
client_secret = creds.client_secret
refresh_token = creds.refresh_token

# Use the Credentials class to create an OAuth 2.0 token that authorizes your application to access the Blogger API

credentials = service_account.Credentials.from_service_account_file(
    "C:/Python311/djia_probable_range_blogger/stonksmaster-bf749211c14b.json"
)
access_token = creds.token

# Build the service object

service = build("blogger", "v3", credentials=creds)

# Use a refresh token to authenticate automatically, you can save the refresh token to a file and load it later

with open("refresh_token.txt", "w") as f:
    f.write(creds.refresh_token)

# Authenticate with the Blogger API using your Google Cloud Platform credentials

SERVICE_ACCOUNT_FILE = (
    "C:/Python311/djia_probable_range_blogger/stonksmaster-bf749211c14b.json"
) 

# Define the ticker symbol

tickerSymbol = "^DJI"


# Set the start and end dates but do not download the current day's data

end_date = pd.Timestamp.today() - pd.Timedelta(days=-1)
start_date = end_date - pd.Timedelta(days=30)

# Get the data from Yahoo Finance
dji_data = yf.download(tickerSymbol, start=start_date, end=end_date)

# Sort the data by 'Date' in descending order
dji_data = dji_data.sort_values("Date", ascending=False)

# Convert the data to a list of lists

exampledata = dji_data.reset_index().values.tolist()

# Perform some mathematical operations on the data
operation1 = math.sqrt((float)(exampledata[1][2])) * math.sqrt(
    (float)(exampledata[1][3])
)

operation2 = operation1 / 7 / 3.125

operation2a = operation1 / 7 / 3.125

operation3 = operation2 * 0.62

operation4 = operation2 * 0.38

operation5 = operation1 - operation4

operation6 = operation1 + operation4

operation7 = operation1 - operation3

operation8 = operation1 + operation3

operation9 = operation1 - (operation1 * 0.01)

operation10 = operation1 + (operation1 * 0.01)

operation11 = math.sqrt(operation1)

operation12 = (float(exampledata[1][2])) - (float(exampledata[1][3]))

operation13 = operation12**2

operation14 = 6.5**2

operation15 = operation13 + operation14

operation16 = (float(exampledata[2][2])) - (float(exampledata[2][3]))

operation17 = operation16**2

operation18 = operation17 + operation14

operation19 = (float(exampledata[3][2])) - (float(exampledata[3][3]))

operation20 = operation19**2

operation21 = operation20 + operation14

operation22 = (float(exampledata[4][2])) - (float(exampledata[4][3]))

operation23 = operation22**2

operation24 = operation23 + operation14

operation25 = (float(exampledata[5][2])) - (float(exampledata[5][3]))

operation26 = operation25**2

operation27 = operation26 + operation14

operation28 = (float(exampledata[6][2])) - (float(exampledata[6][3]))

operation29 = operation28**2

operation30 = operation29 + operation14

operation31 = (float(exampledata[7][2])) - (float(exampledata[7][3]))

operation32 = operation31**2

operation33 = operation32 + operation14

operation34 = (float(exampledata[8][2])) - (float(exampledata[8][3]))

operation35 = operation34**2

operation36 = operation35 + operation14

operation37 = (float(exampledata[9][2])) - (float(exampledata[9][3]))

operation38 = operation37**2

operation39 = operation38 + operation14

operation40 = (float(exampledata[10][2])) - (float(exampledata[10][3]))

operation41 = operation40**2

operation42 = operation41 + operation14

operation43 = (
    operation15
    + operation18
    + operation21
    + operation24
    + operation27
    + operation30
    + operation33
    + operation36
    + operation39
    + operation42
)

operation44 = operation43 / 10

operation45 = operation44 - operation14

operation46 = math.sqrt(operation45)

operation47 = operation1 - operation46

operation48 = operation1 + operation46

operation49 = (float(exampledata[1][4])) - operation46

operation50 = (float(exampledata[1][4])) + operation46

operation51 = math.sqrt(operation47) * math.sqrt(operation49)

operation52 = math.sqrt(operation48) * math.sqrt(operation50)

operation53 = math.sqrt(operation51)

if operation51 < 1250 and operation51 > 1218.749999:
    print("1218.75")

operation54 = (print(str(exampledata[1][1]) + "Open".rjust(5)),)
print(str(exampledata[1][2]) + "High".rjust(5)),
print(str(exampledata[1][3]) + "Low".rjust(4)),
print(str(exampledata[1][4]) + "Close".rjust(6))

# Perform calculations to determine the probable low

if operation51 < 5653.125 and operation51 > 5526.5:
    print(operation51)
elif operation51 < 5990.625 and operation51 > 5864:
    print(operation51)
elif operation51 < 6328.125 and operation51 > 6201.5:
    print(operation51)
elif operation51 < 6665.625 and operation51 > 6539:
    print(operation51)
elif operation51 < 7003.125 and operation51 > 6876.5:
    print(operation51)
elif operation51 < 7340.625 and operation51 > 7214:
    print(operation51)
elif operation51 < 7678.125 and operation51 > 7551.5:
    print(operation51)
elif operation51 < 8015.625 and operation51 > 7889:
    print(operation51)
elif operation51 < 8353.125 and operation51 > 8226.5:
    print(operation51)
elif operation51 < 8690.625 and operation51 > 8564:
    print(operation51)
elif operation51 < 9028.125 and operation51 > 8901.5:
    print(operation51)
elif operation51 < 9365.625 and operation51 > 9239:
    print(operation51)
elif operation51 < 9703.125 and operation51 > 9576.5:
    print(operation51)
elif operation51 < 10040.625 and operation51 > 9914:
    print(operation51)
elif operation51 < 10378.125 and operation51 > 10251.5:
    print(operation51)
elif operation51 < 10715.625 and operation51 > 10589:
    print(operation51)
elif operation51 < 11053.125 and operation51 > 10926.5:
    print(operation51)
elif operation51 < 11390.625 and operation51 > 11264:
    print(operation51)
elif operation51 < 11728.125 and operation51 > 11601.5:
    print(operation51)
elif operation51 < 12065.625 and operation51 > 11939:
    print(operation51)
elif operation51 < 12403.125 and operation51 > 12276.5:
    print(operation51)
elif operation51 < 12740.625 and operation51 > 12614:
    print(operation51)
elif operation51 < 13078.125 and operation51 > 12951.5:
    print(operation51)
elif operation51 < 13415.625 and operation51 > 13289:
    print(operation51)
elif operation51 < 13753.125 and operation51 > 13626.5:
    print(operation51)
elif operation51 < 14090.625 and operation51 > 13964:
    print(operation51)
elif operation51 < 14428.125 and operation51 > 14301.5:
    print(operation51)
elif operation51 < 14765.625 and operation51 > 14639:
    print(operation51)
elif operation51 < 15103.125 and operation51 > 14976.5:
    print(operation51)
elif operation51 < 15440.625 and operation51 > 15314:
    print(operation51)
elif operation51 < 15778.125 and operation51 > 15651.5:
    print(operation51)
elif operation51 < 16115.625 and operation51 > 15989:
    print(operation51)
elif operation51 < 16453.125 and operation51 > 16326.5:
    print(operation51)
elif operation51 < 16790.625 and operation51 > 16664:
    print(operation51)
elif operation51 < 17128.125 and operation51 > 17001.5:
    print(operation51)
elif operation51 < 17465.625 and operation51 > 17339:
    print(operation51)
elif operation51 < 17803.125 and operation51 > 17676.5:
    print(operation51)
elif operation51 < 18140.625 and operation51 > 18014:
    print(operation51)
elif operation51 < 18478.125 and operation51 > 18351.5:
    print(operation51)
elif operation51 < 18815.625 and operation51 > 18689:
    print(operation51)
elif operation51 < 19153.125 and operation51 > 19026.5:
    print(operation51)
elif operation51 < 19490.625 and operation51 > 19364:
    print(operation51)
elif operation51 < 19828.125 and operation51 > 19701.5:
    print(operation51)
elif operation51 < 20165.625 and operation51 > 20039:
    print(operation51)
elif operation51 < 20503.125 and operation51 > 20376.5:
    print(operation51)
elif operation51 < 20840.625 and operation51 > 20714:
    print(operation51)
elif operation51 < 21178.125 and operation51 > 21051.5:
    print(operation51)
elif operation51 < 21515.625 and operation51 > 21389:
    print(operation51)
elif operation51 < 21853.125 and operation51 > 21726.5:
    print(operation51)
elif operation51 < 22190.625 and operation51 > 22064:
    print(operation51)
elif operation51 < 22528.125 and operation51 > 22401.5:
    print(operation51)
elif operation51 < 22865.625 and operation51 > 22739:
    print(operation51)
elif operation51 < 23203.125 and operation51 > 23076.5:
    print(operation51)
elif operation51 < 23540.625 and operation51 > 23414:
    print(operation51)
elif operation51 < 23878.125 and operation51 > 23751.5:
    print(operation51)
elif operation51 < 24215.625 and operation51 > 24089:
    print(operation51)
elif operation51 < 24553.125 and operation51 > 24426.5:
    print(operation51)
elif operation51 < 24890.625 and operation51 > 24764:
    print(operation51)
elif operation51 < 25228.125 and operation51 > 25101.5:
    print(operation51)
elif operation51 < 25565.625 and operation51 > 25439:
    print(operation51)
elif operation51 < 25903.125 and operation51 > 25776.5:
    print(operation51)
elif operation51 < 26240.625 and operation51 > 26114:
    print(operation51)
elif operation51 < 26578.125 and operation51 > 26451.5:
    print(operation51)
elif operation51 < 26915.625 and operation51 > 26789:
    print(operation51)
elif operation51 < 27253.125 and operation51 > 27126.5:
    print(operation51)
elif operation51 < 27590.625 and operation51 > 27464:
    print(operation51)
elif operation51 < 27928.125 and operation51 > 27801.5:
    print(operation51)
elif operation51 < 28265.625 and operation51 > 28139:
    print(operation51)
elif operation51 < 28603.125 and operation51 > 28476.5:
    print(operation51)
elif operation51 < 28940.625 and operation51 > 28814:
    print(operation51)
elif operation51 < 29278.125 and operation51 > 29151.5:
    print(operation51)
elif operation51 < 29615.625 and operation51 > 29489:
    print(operation51)
elif operation51 < 29953.125 and operation51 > 29826.5:
    print(operation51)
elif operation51 < 30290.625 and operation51 > 30164:
    print(operation51)
elif operation51 < 30628.125 and operation51 > 30501.5:
    print(operation51)
elif operation51 < 30965.625 and operation51 > 30839:
    print(operation51)
elif operation51 < 31303.125 and operation51 > 31176.5:
    print(operation51)
elif operation51 < 31640.625 and operation51 > 31514:
    print(operation51)
elif operation51 < 31978.125 and operation51 > 31851.5:
    print(operation51)
elif operation51 < 32315.625 and operation51 > 32189:
    print(operation51)
elif operation51 < 32653.125 and operation51 > 32526.5:
    print(operation51)
elif operation51 < 32990.625 and operation51 > 32864:
    print(operation51)
elif operation51 < 33328.125 and operation51 > 33201.5:
    print(operation51)
elif operation51 < 33665.625 and operation51 > 33539:
    print(operation51)
elif operation51 < 34003.125 and operation51 > 33876.5:
    print(operation51)
elif operation51 < 34340.625 and operation51 > 34214:
    print(operation51)
elif operation51 < 34678.125 and operation51 > 34551.5:
    print(operation51)
elif operation51 < 35015.625 and operation51 > 34889:
    print(operation51)
elif operation51 < 35353.125 and operation51 > 35226.5:
    print(operation51)
elif operation51 < 35690.625 and operation51 > 35564:
    print(operation51)
elif operation51 < 36028.125 and operation51 > 35901.5:
    print(operation51)
elif operation51 < 36365.625 and operation51 > 36239:
    print(operation51)
elif operation51 < 36703.125 and operation51 > 36576.5:
    print(operation51)
elif operation51 < 37040.625 and operation51 > 36914:
    print(operation51)
elif operation51 < 37378.125 and operation51 > 37251.5:
    print(operation51)
elif operation51 < 37715.625 and operation51 > 37589:
    print(operation51)
elif operation51 < 38053.125 and operation51 > 37926.5:
    print(operation51)
elif operation51 < 38390.625 and operation51 > 38264:
    print(operation51)
elif operation51 < 38728.125 and operation51 > 38601.5:
    print(operation51)
elif operation51 < 39065.625 and operation51 > 38939:
    print(operation51)
elif operation51 < 39403.125 and operation51 > 39276.5:
    print(operation51)
elif operation51 < 39740.625 and operation51 > 39614:
    print(operation51)
elif operation51 < 40078.125 and operation51 > 39951.5:
    print(operation51)
elif operation51 < 40415.625 and operation51 > 40289:
    print(operation51)
elif operation51 < 40753.125 and operation51 > 40626.5:
    print(operation51)
elif operation51 < 41090.625 and operation51 > 40964:
    print(operation51)
elif operation51 < 41428.125 and operation51 > 41301.5:
    print(operation51)
elif operation51 < 41765.625 and operation51 > 41639:
    print(operation51)
elif operation51 < 42103.125 and operation51 > 41976.5:
    print(operation51)
elif operation51 < 42440.625 and operation51 > 42314:
    print(operation51)
elif operation51 < 42778.125 and operation51 > 42651.5:
    print(operation51)
elif operation51 < 43115.625 and operation51 > 42989:
    print(operation51)

# Perform additional calculations to determine probable low

elif operation51 < 5484.375:
    print("5400")
elif operation51 < 5526.5625:
    print("5484.375")
elif operation51 < 5737.5:
    print("5653.125")
elif operation51 < 5821.875:
    print("5737.5")
elif operation51 < 5864.0625:
    print("5821.875")
elif operation51 < 6075:
    print("5990.625")
elif operation51 < 6159.375:
    print("6075")
elif operation51 < 6201.5625:
    print("6159.375")
elif operation51 < 6412.5:
    print("6328.125")
elif operation51 < 6496.875:
    print("6412.5")
elif operation51 < 6539.0625:
    print("6496.875")
elif operation51 < 6750:
    print("6665.625")
elif operation51 < 6834.375:
    print("6750")
elif operation51 < 6876.5625:
    print("6834.375")
elif operation51 < 7087.5:
    print("7003.125")
elif operation51 < 7171.875:
    print("7087.5")
elif operation51 < 7214.0625:
    print("7171.875")
elif operation51 < 7425:
    print("7340.625")
elif operation51 < 7509.375:
    print("7425")
elif operation51 < 7551.5625:
    print("7509.375")
elif operation51 < 7762.5:
    print("7678.125")
elif operation51 < 7846.875:
    print("7762.5")
elif operation51 < 7889.0625:
    print("7846.875")
elif operation51 < 8100:
    print("8015.625")
elif operation51 < 8184.375:
    print("8100")
elif operation51 < 8226.5625:
    print("8184.375")
elif operation51 < 8437.5:
    print("8353.125")
elif operation51 < 8521.875:
    print("8437.5")
elif operation51 < 8564.0625:
    print("8521.875")
elif operation51 < 8775:
    print("8690.625")
elif operation51 < 8859.375:
    print("8775")
elif operation51 < 8901.5625:
    print("8859.375")
elif operation51 < 9112.5:
    print("9028.125")
elif operation51 < 9196.875:
    print("9112.5")
elif operation51 < 9239.0625:
    print("9196.875")
elif operation51 < 9450:
    print("9365.625")
elif operation51 < 9534.375:
    print("9450")
elif operation51 < 9576.5625:
    print("9534.375")
elif operation51 < 9787.5:
    print("9703.125")
elif operation51 < 9871.875:
    print("9787.5")
elif operation51 < 9914.0625:
    print("9871.875")
elif operation51 < 10125:
    print("10040.625")
elif operation51 < 10209.375:
    print("10125")
elif operation51 < 10251.5625:
    print("10209.375")
elif operation51 < 10462.5:
    print("10378.125")
elif operation51 < 10546.875:
    print("10462.5")
elif operation51 < 10589.0625:
    print("10546.875")
elif operation51 < 10800:
    print("10715.625")
elif operation51 < 10884.375:
    print("10800")
elif operation51 < 10926.5625:
    print("10884.375")
elif operation51 < 11137.5:
    print("11053.125")
elif operation51 < 11221.875:
    print("11137.5")
elif operation51 < 11264.0625:
    print("11221.875")
elif operation51 < 11475:
    print("11390.625")
elif operation51 < 11559.375:
    print("11475")
elif operation51 < 11601.5625:
    print("11559.375")
elif operation51 < 11812.5:
    print("11728.125")
elif operation51 < 11896.875:
    print("11812.5")
elif operation51 < 11939.0625:
    print("11896.875")
elif operation51 < 12150:
    print("12065.625")
elif operation51 < 12234.375:
    print("12150")
elif operation51 < 12276.5625:
    print("12234.375")
elif operation51 < 12487.5:
    print("12403.125")
elif operation51 < 12571.875:
    print("12487.5")
elif operation51 < 12614.0625:
    print("12571.875")
elif operation51 < 12825:
    print("12740.625")
elif operation51 < 12909.375:
    print("12825")
elif operation51 < 12951.5625:
    print("12909.375")
elif operation51 < 13162.5:
    print("13078.125")
elif operation51 < 13246.875:
    print("13162.5")
elif operation51 < 13289.0625:
    print("13246.875")
elif operation51 < 13500:
    print("13415.625")
elif operation51 < 13584.375:
    print("13500")
elif operation51 < 13626.5625:
    print("13584.375")
elif operation51 < 13837.5:
    print("13753.125")
elif operation51 < 13921.875:
    print("13837.5")
elif operation51 < 13964.0625:
    print("13921.875")
elif operation51 < 14175:
    print("14090.625")
elif operation51 < 14259.375:
    print("14175")
elif operation51 < 14301.5625:
    print("14259.375")
elif operation51 < 14512.5:
    print("14428.125")
elif operation51 < 14596.875:
    print("14512.5")
elif operation51 < 14639.0625:
    print("14596.875")
elif operation51 < 14850:
    print("14765.625")
elif operation51 < 14934.375:
    print("14850")
elif operation51 < 14976.5625:
    print("14934.375")
elif operation51 < 15187.5:
    print("15103.125")
elif operation51 < 15271.875:
    print("15187.5")
elif operation51 < 15314.0625:
    print("15271.875")
elif operation51 < 15525:
    print("15440.625")
elif operation51 < 15609.375:
    print("15525")
elif operation51 < 15651.5625:
    print("15609.375")
elif operation51 < 15862.5:
    print("15778.125")
elif operation51 < 15946.875:
    print("15862.5")
elif operation51 < 15989.0625:
    print("15946.875")
elif operation51 < 16200:
    print("16115.625")
elif operation51 < 16284.375:
    print("16200")
elif operation51 < 16326.5625:
    print("16284.375")
elif operation51 < 16537.5:
    print("16453.125")
elif operation51 < 16621.875:
    print("16537.5")
elif operation51 < 16664.0625:
    print("16621.875")
elif operation51 < 16875:
    print("16790.625")
elif operation51 < 16959.375:
    print("16875")
elif operation51 < 17001.5625:
    print("16959.375")
elif operation51 < 17212.5:
    print("17128.125")
elif operation51 < 17296.875:
    print("17212.5")
elif operation51 < 17339.0625:
    print("17296.875")
elif operation51 < 17550:
    print("17465.625")
elif operation51 < 17634.375:
    print("17550")
elif operation51 < 17676.5625:
    print("17634.375")
elif operation51 < 17887.5:
    print("17803.125")
elif operation51 < 17971.875:
    print("17887.5")
elif operation51 < 18014.0625:
    print("17971.875")
elif operation51 < 18225:
    print("18140.625")
elif operation51 < 18309.375:
    print("18225")
elif operation51 < 18351.5625:
    print("18309.375")
elif operation51 < 18562.5:
    print("18478.125")
elif operation51 < 18646.875:
    print("18562.5")
elif operation51 < 18689.0625:
    print("18646.875")
elif operation51 < 18900:
    print("18815.625")
elif operation51 < 18984.375:
    print("18900")
elif operation51 < 19026.5625:
    print("18984.375")
elif operation51 < 19237.5:
    print("19153.125")
elif operation51 < 19321.875:
    print("19237.5")
elif operation51 < 19364.0625:
    print("19321.875")
elif operation51 < 19575:
    print("19490.625")
elif operation51 < 19659.375:
    print("19575")
elif operation51 < 19701.5625:
    print("19659.375")
elif operation51 < 19912.5:
    print("19828.125")
elif operation51 < 19996.875:
    print("19912.5")
elif operation51 < 20039.0625:
    print("19996.875")
elif operation51 < 20250:
    print("20165.625")
elif operation51 < 20334.375:
    print("20250")
elif operation51 < 20376.5625:
    print("20334.375")
elif operation51 < 20587.5:
    print("20503.125")
elif operation51 < 20671.875:
    print("20587.5")
elif operation51 < 20714.0625:
    print("20671.875")
elif operation51 < 20925:
    print("20840.625")
elif operation51 < 21009.375:
    print("20925")
elif operation51 < 21051.5625:
    print("21009.375")
elif operation51 < 21262.5:
    print("21178.125")
elif operation51 < 21346.875:
    print("21262.5")
elif operation51 < 21389.0625:
    print("21346.875")
elif operation51 < 21600:
    print("21515.625")
elif operation51 < 21684.375:
    print("21600")
elif operation51 < 21726.5625:
    print("21684.375")
elif operation51 < 21937.5:
    print("21853.125")
elif operation51 < 22021.875:
    print("21937.5")
elif operation51 < 22064.0625:
    print("22021.875")
elif operation51 < 22275:
    print("22190.625")
elif operation51 < 22359.375:
    print("22275")
elif operation51 < 22401.5625:
    print("22359.375")
elif operation51 < 22612.5:
    print("22528.125")
elif operation51 < 22696.875:
    print("22612.5")
elif operation51 < 22739.0625:
    print("22696.875")
elif operation51 < 22950:
    print("22865.625")
elif operation51 < 23034.375:
    print("22950")
elif operation51 < 23076.5625:
    print("23034.375")
elif operation51 < 23287.5:
    print("23203.125")
elif operation51 < 23371.875:
    print("23287.5")
elif operation51 < 23414.0625:
    print("23371.875")
elif operation51 < 23625:
    print("23540.625")
elif operation51 < 23709.375:
    print("23625")
elif operation51 < 23751.5625:
    print("23709.375")
elif operation51 < 23962.5:
    print("23878.125")
elif operation51 < 24046.875:
    print("23962.5")
elif operation51 < 24089.0625:
    print("24046.875")
elif operation51 < 24300:
    print("24215.625")
elif operation51 < 24384.375:
    print("24300")
elif operation51 < 24426.5625:
    print("24384.375")
elif operation51 < 24637.5:
    print("24553.125")
elif operation51 < 24721.875:
    print("24637.5")
elif operation51 < 24764.0625:
    print("24721.875")
elif operation51 < 24975:
    print("24890.625")
elif operation51 < 25059.375:
    print("24975")
elif operation51 < 25101.5625:
    print("25059.375")
elif operation51 < 25312.5:
    print("25228.125")
elif operation51 < 25396.875:
    print("25312.5")
elif operation51 < 25439.0625:
    print("25396.875")
elif operation51 < 25650:
    print("25565.625")
elif operation51 < 25734.375:
    print("25650")
elif operation51 < 25776.5625:
    print("25734.375")
elif operation51 < 25987.5:
    print("25903.125")
elif operation51 < 26071.875:
    print("25987.5")
elif operation51 < 26114.0625:
    print("26071.875")
elif operation51 < 26325:
    print("26240.625")
elif operation51 < 26409.375:
    print("26325")
elif operation51 < 26451.5625:
    print("26409.375")
elif operation51 < 26662.5:
    print("26578.125")
elif operation51 < 26746.875:
    print("26662.5")
elif operation51 < 26789.0625:
    print("26746.875")
elif operation51 < 27000:
    print("26915.625")
elif operation51 < 27084.375:
    print("27000")
elif operation51 < 27126.5625:
    print("27084.375")
elif operation51 < 27337.5:
    print("27253.125")
elif operation51 < 27421.875:
    print("27337.5")
elif operation51 < 27464.0625:
    print("27421.875")
elif operation51 < 27675:
    print("27590.625")
elif operation51 < 27759.375:
    print("27675")
elif operation51 < 27801.5625:
    print("27759.375")
elif operation51 < 28012.5:
    print("27928.125")
elif operation51 < 28096.875:
    print("28012.5")
elif operation51 < 28139.0625:
    print("28096.875")
elif operation51 < 28350:
    print("28265.625")
elif operation51 < 28434.375:
    print("28350")
elif operation51 < 28476.5625:
    print("28434.375")
elif operation51 < 28687.5:
    print("28603.125")
elif operation51 < 28771.875:
    print("28687.5")
elif operation51 < 28814.0625:
    print("28771.875")
elif operation51 < 29025:
    print("28940.625")
elif operation51 < 29109.375:
    print("29025")
elif operation51 < 29151.5625:
    print("29109.375")
elif operation51 < 29362.5:
    print("29278.125")
elif operation51 < 29446.875:
    print("29362.5")
elif operation51 < 29489.0625:
    print("29446.875")
elif operation51 < 29700:
    print("29615.625")
elif operation51 < 29784.375:
    print("29700")
elif operation51 < 29826.5625:
    print("29784.375")
elif operation51 < 30037.5:
    print("29953.125")
elif operation51 < 30121.875:
    print("30037.5")
elif operation51 < 30164.0625:
    print("30121.875")
elif operation51 < 30375:
    print("30290.625")
elif operation51 < 30459.375:
    print("30375")
elif operation51 < 30501.5625:
    print("30459.375")
elif operation51 < 30712.5:
    print("30628.125")
elif operation51 < 30796.875:
    print("30712.5")
elif operation51 < 30839.0625:
    print("30796.875")
elif operation51 < 31050:
    print("30965.625")
elif operation51 < 31134.375:
    print("31050")
elif operation51 < 31176.5625:
    print("31134.375")
elif operation51 < 31387.5:
    print("31303.125")
elif operation51 < 31471.875:
    print("31387.5")
elif operation51 < 31514.0625:
    print("31471.875")
elif operation51 < 31725:
    print("31640.625")
elif operation51 < 31809.375:
    print("31725")
elif operation51 < 31851.5625:
    print("31809.375")
elif operation51 < 32062.5:
    print("31978.125")
elif operation51 < 32146.875:
    print("32062.5")
elif operation51 < 32189.0625:
    print("32146.875")
elif operation51 < 32400:
    print("32315.625")
elif operation51 < 32484.375:
    print("32400")
elif operation51 < 32526.5625:
    print("32484.375")
elif operation51 < 32737.5:
    print("32653.125")
elif operation51 < 32821.875:
    print("32737.5")
elif operation51 < 32864.0625:
    print("32821.875")
elif operation51 < 33075:
    print("32990.625")
elif operation51 < 33159.375:
    print("33075")
elif operation51 < 33201.5625:
    print("33159.375")
elif operation51 < 33412.5:
    print("33328.125")
elif operation51 < 33496.875:
    print("33412.5")
elif operation51 < 33539.0625:
    print("33496.875")
elif operation51 < 33750:
    print("33665.625")
elif operation51 < 33834.375:
    print("33750")
elif operation51 < 33876.5625:
    print("33834.375")
elif operation51 < 34087.5:
    print("34003.125")
elif operation51 < 34171.875:
    print("34087.5")
elif operation51 < 34214.0625:
    print("34171.875")
elif operation51 < 34425:
    print("34340.625")
elif operation51 < 34509.375:
    print("34425")
elif operation51 < 34551.5625:
    print("34509.375")
elif operation51 < 34762.5:
    print("34678.125")
elif operation51 < 34846.875:
    print("34762.5")
elif operation51 < 34889.0625:
    print("34846.875")
elif operation51 < 35100:
    print("35015.625")
elif operation51 < 35184.375:
    print("35100")
elif operation51 < 35226.5625:
    print("35184.375")
elif operation51 < 35437.5:
    print("35353.125")
elif operation51 < 35521.875:
    print("35437.5")
elif operation51 < 35564.0625:
    print("35521.875")
elif operation51 < 35775:
    print("35690.625")
elif operation51 < 35859.375:
    print("35775")
elif operation51 < 35901.5625:
    print("35859.375")
elif operation51 < 36112.5:
    print("36028.125")
elif operation51 < 36196.875:
    print("36112.5")
elif operation51 < 36239.0625:
    print("36196.875")
elif operation51 < 36450:
    print("36365.625")
elif operation51 < 36534.375:
    print("36450")
elif operation51 < 36576.5625:
    print("36534.375")
elif operation51 < 36787.5:
    print("36703.125")
elif operation51 < 36871.875:
    print("36787.5")
elif operation51 < 36914.0625:
    print("36871.875")
elif operation51 < 37125:
    print("37040.625")
elif operation51 < 37209.375:
    print("37125")
elif operation51 < 37251.5625:
    print("37209.375")
elif operation51 < 37462.5:
    print("37378.125")
elif operation51 < 37546.875:
    print("37462.5")
elif operation51 < 37589.0625:
    print("37546.875")
elif operation51 < 37800:
    print("37715.625")
elif operation51 < 37884.375:
    print("37800")
elif operation51 < 37926.5625:
    print("37884.375")
elif operation51 < 38137.5:
    print("38053.125")
elif operation51 < 38221.875:
    print("38137.5")
elif operation51 < 38264.0625:
    print("38221.875")
elif operation51 < 38475:
    print("38390.625")
elif operation51 < 38559.375:
    print("38475")
elif operation51 < 38601.5625:
    print("38559.375")
elif operation51 < 38812.5:
    print("38728.125")
elif operation51 < 38896.875:
    print("38812.5")
elif operation51 < 38939.0625:
    print("38896.875")
elif operation51 < 39150:
    print("39065.625")
elif operation51 < 39234.375:
    print("39150")
elif operation51 < 39276.5625:
    print("39234.375")
elif operation51 < 39487.5:
    print("39403.125")
elif operation51 < 39571.875:
    print("39487.5")
elif operation51 < 39614.0625:
    print("39571.875")
elif operation51 < 39825:
    print("39740.625")
elif operation51 < 39909.375:
    print("39825")
elif operation51 < 39951.5625:
    print("39909.375")
elif operation51 < 40162.5:
    print("40078.125")
elif operation51 < 40246.875:
    print("40162.5")
elif operation51 < 40289.0625:
    print("40246.875")
elif operation51 < 40500:
    print("40415.625")
elif operation51 < 40584.375:
    print("40500")
elif operation51 < 40626.5625:
    print("40584.375")
elif operation51 < 40837.5:
    print("40753.125")
elif operation51 < 40921.875:
    print("40837.5")
elif operation51 < 40964.0625:
    print("40921.875")
elif operation51 < 41175:
    print("41090.625")
elif operation51 < 41259.375:
    print("41175")
elif operation51 < 41301.5625:
    print("41259.375")
elif operation51 < 41512.5:
    print("41428.125")
elif operation51 < 41596.875:
    print("41512.5")
elif operation51 < 41639.0625:
    print("41596.875")
elif operation51 < 41850:
    print("41765.625")
elif operation51 < 41934.375:
    print("41850")
elif operation51 < 41976.5625:
    print("41934.375")
elif operation51 < 42187.5:
    print("42103.125")
elif operation51 < 42271.875:
    print("42187.5")
elif operation51 < 42314.0625:
    print("42271.875")
elif operation51 < 42525:
    print("42440.625")
elif operation51 < 42609.375:
    print("42525")
elif operation51 < 42651.5625:
    print("42609.375")
elif operation51 < 42862.5:
    print("42778.125")
elif operation51 < 42946.875:
    print("42862.5")
elif operation51 < 42989.0625:
    print("42946.875")
elif operation51 < 43200:
    print("43115.625")
else:
    print(operation51)

# Perform calculations to determine the probable high

if operation52 > 43115.6250:
    print("43200.0000")
elif operation52 > 42946.875 and operation52 < 43073.4375:
    print(operation52)
elif operation52 > 42609.375 and operation52 < 42735.9375:
    print(operation52)
elif operation52 > 42271.875 and operation52 < 42398.4375:
    print(operation52)
elif operation52 > 41934.375 and operation52 < 42060.9375:
    print(operation52)
elif operation52 > 41596.875 and operation52 < 41723.4375:
    print(operation52)
elif operation52 > 41259.375 and operation52 < 41385.9375:
    print(operation52)
elif operation52 > 40921.875 and operation52 < 41048.4375:
    print(operation52)
elif operation52 > 40584.375 and operation52 < 40710.9375:
    print(operation52)
elif operation52 > 40246.875 and operation52 < 40373.4375:
    print(operation52)
elif operation52 > 39909.375 and operation52 < 40035.9375:
    print(operation52)
elif operation52 > 39571.875 and operation52 < 39698.4375:
    print(operation52)
elif operation52 > 39234.375 and operation52 < 39360.9375:
    print(operation52)
elif operation52 > 38896.875 and operation52 < 39023.4375:
    print(operation52)
elif operation52 > 38559.375 and operation52 < 38685.9375:
    print(operation52)
elif operation52 > 38221.875 and operation52 < 38348.4375:
    print(operation52)
elif operation52 > 37884.375 and operation52 < 38010.9375:
    print(operation52)
elif operation52 > 37546.875 and operation52 < 37673.4375:
    print(operation52)
elif operation52 > 37209.375 and operation52 < 37335.9375:
    print(operation52)
elif operation52 > 36871.875 and operation52 < 36998.4375:
    print(operation52)
elif operation52 > 36534.375 and operation52 < 36660.9375:
    print(operation52)
elif operation52 > 36196.875 and operation52 < 36323.4375:
    print(operation52)
elif operation52 > 35859.375 and operation52 < 35985.9375:
    print(operation52)
elif operation52 > 35521.875 and operation52 < 35648.4375:
    print(operation52)
elif operation52 > 35184.375 and operation52 < 35310.9375:
    print(operation52)
elif operation52 > 34846.875 and operation52 < 34973.4375:
    print(operation52)
elif operation52 > 34509.375 and operation52 < 34635.9375:
    print(operation52)
elif operation52 > 34171.875 and operation52 < 34298.4375:
    print(operation52)
elif operation52 > 33834.375 and operation52 < 33960.9375:
    print(operation52)
elif operation52 > 33496.875 and operation52 < 33623.4375:
    print(operation52)
elif operation52 > 33159.375 and operation52 < 33285.9375:
    print(operation52)
elif operation52 > 32821.875 and operation52 < 32948.4375:
    print(operation52)
elif operation52 > 32484.375 and operation52 < 32610.9375:
    print(operation52)
elif operation52 > 32146.875 and operation52 < 32273.4375:
    print(operation52)
elif operation52 > 31809.375 and operation52 < 31935.9375:
    print(operation52)
elif operation52 > 31471.875 and operation52 < 31598.4375:
    print(operation52)
elif operation52 > 31134.375 and operation52 < 31260.9375:
    print(operation52)
elif operation52 > 30796.875 and operation52 < 30923.4375:
    print(operation52)
elif operation52 > 30459.375 and operation52 < 30585.9375:
    print(operation52)
elif operation52 > 30121.875 and operation52 < 30248.4375:
    print(operation52)
elif operation52 > 29784.375 and operation52 < 29910.9375:
    print(operation52)
elif operation52 > 29446.875 and operation52 < 29573.4375:
    print(operation52)
elif operation52 > 29109.375 and operation52 < 29235.9375:
    print(operation52)
elif operation52 > 28771.875 and operation52 < 28898.4375:
    print(operation52)
elif operation52 > 28434.375 and operation52 < 28560.9375:
    print(operation52)
elif operation52 > 28096.875 and operation52 < 28223.4375:
    print(operation52)
elif operation52 > 27759.375 and operation52 < 27885.9375:
    print(operation52)
elif operation52 > 27421.875 and operation52 < 27548.4375:
    print(operation52)
elif operation52 > 27084.375 and operation52 < 27210.9375:
    print(operation52)
elif operation52 > 26746.875 and operation52 < 26873.4375:
    print(operation52)
elif operation52 > 26409.375 and operation52 < 26535.9375:
    print(operation52)
elif operation52 > 26071.875 and operation52 < 26198.4375:
    print(operation52)
elif operation52 > 25734.375 and operation52 < 25860.9375:
    print(operation52)
elif operation52 > 25396.875 and operation52 < 25523.4375:
    print(operation52)
elif operation52 > 25059.375 and operation52 < 25185.9375:
    print(operation52)
elif operation52 > 24721.875 and operation52 < 24848.4375:
    print(operation52)
elif operation52 > 24384.375 and operation52 < 24510.9375:
    print(operation52)
elif operation52 > 24046.875 and operation52 < 24173.4375:
    print(operation52)
elif operation52 > 23709.375 and operation52 < 23835.9375:
    print(operation52)
elif operation52 > 23371.875 and operation52 < 23498.4375:
    print(operation52)
elif operation52 > 23034.375 and operation52 < 23160.9375:
    print(operation52)
elif operation52 > 22696.875 and operation52 < 22823.4375:
    print(operation52)
elif operation52 > 22359.375 and operation52 < 22485.9375:
    print(operation52)
elif operation52 > 22021.875 and operation52 < 22148.4375:
    print(operation52)
elif operation52 > 21684.375 and operation52 < 21810.9375:
    print(operation52)
elif operation52 > 21346.875 and operation52 < 21473.4375:
    print(operation52)
elif operation52 > 21009.375 and operation52 < 21135.9375:
    print(operation52)
elif operation52 > 20671.875 and operation52 < 20798.4375:
    print(operation52)
elif operation52 > 20334.375 and operation52 < 20460.9375:
    print(operation52)
elif operation52 > 19996.875 and operation52 < 20123.4375:
    print(operation52)
elif operation52 > 19659.375 and operation52 < 19785.9375:
    print(operation52)
elif operation52 > 19321.875 and operation52 < 19448.4375:
    print(operation52)
elif operation52 > 18984.375 and operation52 < 19110.9375:
    print(operation52)
elif operation52 > 18646.875 and operation52 < 18773.4375:
    print(operation52)
elif operation52 > 18309.375 and operation52 < 18435.9375:
    print(operation52)
elif operation52 > 17971.875 and operation52 < 18098.4375:
    print(operation52)
elif operation52 > 17634.375 and operation52 < 17760.9375:
    print(operation52)
elif operation52 > 17296.875 and operation52 < 17423.4375:
    print(operation52)
elif operation52 > 16959.375 and operation52 < 17085.9375:
    print(operation52)
elif operation52 > 16621.875 and operation52 < 16748.4375:
    print(operation52)
elif operation52 > 16284.375 and operation52 < 16410.9375:
    print(operation52)
elif operation52 > 15946.875 and operation52 < 16073.4375:
    print(operation52)
elif operation52 > 15609.375 and operation52 < 15735.9375:
    print(operation52)
elif operation52 > 15271.875 and operation52 < 15398.4375:
    print(operation52)
elif operation52 > 14934.375 and operation52 < 15060.9375:
    print(operation52)
elif operation52 > 14596.875 and operation52 < 14723.4375:
    print(operation52)
elif operation52 > 14259.375 and operation52 < 14385.9375:
    print(operation52)
elif operation52 > 13921.875 and operation52 < 14048.4375:
    print(operation52)
elif operation52 > 13584.375 and operation52 < 13710.9375:
    print(operation52)
elif operation52 > 13246.875 and operation52 < 13373.4375:
    print(operation52)
elif operation52 > 12909.375 and operation52 < 13035.9375:
    print(operation52)
elif operation52 > 12571.875 and operation52 < 12698.4375:
    print(operation52)
elif operation52 > 12234.375 and operation52 < 12360.9375:
    print(operation52)
elif operation52 > 11896.875 and operation52 < 12023.4375:
    print(operation52)
elif operation52 > 11559.375 and operation52 < 11685.9375:
    print(operation52)
elif operation52 > 11221.875 and operation52 < 11348.4375:
    print(operation52)
elif operation52 > 10884.375 and operation52 < 11010.9375:
    print(operation52)
elif operation52 > 10546.875 and operation52 < 10673.4375:
    print(operation52)
elif operation52 > 10209.375 and operation52 < 10335.9375:
    print(operation52)
elif operation52 > 9871.875 and operation52 < 9998.4375:
    print(operation52)
elif operation52 > 9534.375 and operation52 < 9660.9375:
    print(operation52)
elif operation52 > 9196.875 and operation52 < 9323.4375:
    print(operation52)
elif operation52 > 8859.375 and operation52 < 8985.9375:
    print(operation52)
elif operation52 > 8521.875 and operation52 < 8648.4375:
    print(operation52)
elif operation52 > 8184.375 and operation52 < 8310.9375:
    print(operation52)
elif operation52 > 7846.875 and operation52 < 7973.4375:
    print(operation52)
elif operation52 > 7509.375 and operation52 < 7635.9375:
    print(operation52)
elif operation52 > 7171.875 and operation52 < 7298.4375:
    print(operation52)
elif operation52 > 6834.375 and operation52 < 6960.9375:
    print(operation52)
elif operation52 > 6496.875 and operation52 < 6623.4375:
    print(operation52)
elif operation52 > 6159.375 and operation52 < 6285.9375:
    print(operation52)
elif operation52 > 5821.875 and operation52 < 5948.4375:
    print(operation52)
elif operation52 > 5484.375 and operation52 < 5610.9375:
    print(operation52)

# Perform additional calculations to determine probable high

elif operation52 > 43115.652:
    print("43200")
elif operation52 > 43073.4375:
    print("43115.625")
elif operation52 > 42862.5:
    print("42946.875")
elif operation52 > 42778.152:
    print("42862.5")
elif operation52 > 42735.9375:
    print("42778.125")
elif operation52 > 42525:
    print("42609.375")
elif operation52 > 42440.652:
    print("42525")
elif operation52 > 42398.4375:
    print("42440.625")
elif operation52 > 42187.5:
    print("42271.875")
elif operation52 > 42103.152:
    print("42187.5")
elif operation52 > 42060.9375:
    print("42103.125")
elif operation52 > 41850:
    print("41934.375")
elif operation52 > 41765.652:
    print("41850")
elif operation52 > 41723.4375:
    print("41765.625")
elif operation52 > 41512.5:
    print("41596.875")
elif operation52 > 41428.152:
    print("41512.5")
elif operation52 > 41385.9375:
    print("41428.125")
elif operation52 > 41175:
    print("41259.375")
elif operation52 > 41090.652:
    print("41175")
elif operation52 > 41048.4375:
    print("41090.625")
elif operation52 > 40837.5:
    print("40921.875")
elif operation52 > 40753.152:
    print("40837.5")
elif operation52 > 40710.9375:
    print("40753.125")
elif operation52 > 40500:
    print("40584.375")
elif operation52 > 40415.652:
    print("40500")
elif operation52 > 40373.4375:
    print("40415.625")
elif operation52 > 40162.5:
    print("40246.875")
elif operation52 > 40078.152:
    print("40162.5")
elif operation52 > 40035.9375:
    print("40078.125")
elif operation52 > 39825:
    print("39909.375")
elif operation52 > 39740.652:
    print("39825")
elif operation52 > 39698.4375:
    print("39740.625")
elif operation52 > 39487.5:
    print("39571.875")
elif operation52 > 39403.152:
    print("39487.5")
elif operation52 > 39360.9375:
    print("39403.125")
elif operation52 > 39150:
    print("39234.375")
elif operation52 > 39065.652:
    print("39150")
elif operation52 > 39023.4375:
    print("39065.625")
elif operation52 > 38812.5:
    print("38896.875")
elif operation52 > 38728.152:
    print("38812.5")
elif operation52 > 38685.9375:
    print("38728.125")
elif operation52 > 38475:
    print("38559.375")
elif operation52 > 38390.652:
    print("38475")
elif operation52 > 38348.4375:
    print("38390.625")
elif operation52 > 38137.5:
    print("38221.875")
elif operation52 > 38053.152:
    print("38137.5")
elif operation52 > 38010.9375:
    print("38053.125")
elif operation52 > 37800:
    print("37884.375")
elif operation52 > 37715.652:
    print("37800")
elif operation52 > 37673.4375:
    print("37715.625")
elif operation52 > 37462.5:
    print("37546.875")
elif operation52 > 37378.152:
    print("37462.5")
elif operation52 > 37335.9375:
    print("37378.125")
elif operation52 > 37125:
    print("37209.375")
elif operation52 > 37040.652:
    print("37125")
elif operation52 > 36998.4375:
    print("37040.625")
elif operation52 > 36787.5:
    print("36871.875")
elif operation52 > 36703.152:
    print("36787.5")
elif operation52 > 36660.9375:
    print("36703.125")
elif operation52 > 36450:
    print("36534.375")
elif operation52 > 36365.652:
    print("36450")
elif operation52 > 36323.4375:
    print("36365.625")
elif operation52 > 36112.5:
    print("36196.875")
elif operation52 > 36028.152:
    print("36112.5")
elif operation52 > 35985.9375:
    print("36028.125")
elif operation52 > 35775:
    print("35859.375")
elif operation52 > 35690.652:
    print("35775")
elif operation52 > 35648.4375:
    print("35690.625")
elif operation52 > 35437.5:
    print("35521.875")
elif operation52 > 35353.152:
    print("35437.5")
elif operation52 > 35310.9375:
    print("35353.125")
elif operation52 > 35100:
    print("35184.375")
elif operation52 > 35015.652:
    print("35100")
elif operation52 > 34973.4375:
    print("35015.625")
elif operation52 > 34762.5:
    print("34846.875")
elif operation52 > 34678.152:
    print("34762.5")
elif operation52 > 34635.9375:
    print("34678.125")
elif operation52 > 34425:
    print("34509.375")
elif operation52 > 34340.652:
    print("34425")
elif operation52 > 34298.4375:
    print("34340.625")
elif operation52 > 34087.5:
    print("34171.875")
elif operation52 > 34003.152:
    print("34087.5")
elif operation52 > 33960.9375:
    print("34003.125")
elif operation52 > 33750:
    print("33834.375")
elif operation52 > 33665.652:
    print("33750")
elif operation52 > 33623.4375:
    print("33665.625")
elif operation52 > 33412.5:
    print("33496.875")
elif operation52 > 33328.152:
    print("33412.5")
elif operation52 > 33285.9375:
    print("33328.125")
elif operation52 > 33075:
    print("33159.375")
elif operation52 > 32990.652:
    print("33075")
elif operation52 > 32948.4375:
    print("32990.625")
elif operation52 > 32737.5:
    print("32821.875")
elif operation52 > 32653.152:
    print("32737.5")
elif operation52 > 32610.9375:
    print("32653.125")
elif operation52 > 32400:
    print("32484.375")
elif operation52 > 32315.652:
    print("32400")
elif operation52 > 32273.4375:
    print("32315.625")
elif operation52 > 32062.5:
    print("32146.875")
elif operation52 > 31978.152:
    print("32062.5")
elif operation52 > 31935.9375:
    print("31978.125")
elif operation52 > 31725:
    print("31809.375")
elif operation52 > 31640.652:
    print("31725")
elif operation52 > 31598.4375:
    print("31640.625")
elif operation52 > 31387.5:
    print("31471.875")
elif operation52 > 31303.152:
    print("31387.5")
elif operation52 > 31260.9375:
    print("31303.125")
elif operation52 > 31050:
    print("31134.375")
elif operation52 > 30965.652:
    print("31050")
elif operation52 > 30923.4375:
    print("30965.625")
elif operation52 > 30712.5:
    print("30796.875")
elif operation52 > 30628.152:
    print("30712.5")
elif operation52 > 30585.9375:
    print("30628.125")
elif operation52 > 30375:
    print("30459.375")
elif operation52 > 30290.652:
    print("30375")
elif operation52 > 30248.4375:
    print("30290.625")
elif operation52 > 30037.5:
    print("30121.875")
elif operation52 > 29953.152:
    print("30037.5")
elif operation52 > 29910.9375:
    print("29953.125")
elif operation52 > 29700:
    print("29784.375")
elif operation52 > 29615.652:
    print("29700")
elif operation52 > 29573.4375:
    print("29615.625")
elif operation52 > 29362.5:
    print("29446.875")
elif operation52 > 29278.152:
    print("29362.5")
elif operation52 > 29235.9375:
    print("29278.125")
elif operation52 > 29025:
    print("29109.375")
elif operation52 > 28940.652:
    print("29025")
elif operation52 > 28898.4375:
    print("28940.625")
elif operation52 > 28687.5:
    print("28771.875")
elif operation52 > 28603.152:
    print("28687.5")
elif operation52 > 28560.9375:
    print("28603.125")
elif operation52 > 28350:
    print("28434.375")
elif operation52 > 28265.652:
    print("28350")
elif operation52 > 28223.4375:
    print("28265.625")
elif operation52 > 28012.5:
    print("28096.875")
elif operation52 > 27928.152:
    print("28012.5")
elif operation52 > 27885.9375:
    print("27928.125")
elif operation52 > 27675:
    print("27759.375")
elif operation52 > 27590.652:
    print("27675")
elif operation52 > 27548.4375:
    print("27590.625")
elif operation52 > 27337.5:
    print("27421.875")
elif operation52 > 27253.152:
    print("27337.5")
elif operation52 > 27210.9375:
    print("27253.125")
elif operation52 > 27000:
    print("27084.375")
elif operation52 > 26915.652:
    print("27000")
elif operation52 > 26873.4375:
    print("26915.625")
elif operation52 > 26662.5:
    print("26746.875")
elif operation52 > 26578.152:
    print("26662.5")
elif operation52 > 26535.9375:
    print("26578.125")
elif operation52 > 26325:
    print("26409.375")
elif operation52 > 26240.652:
    print("26325")
elif operation52 > 26198.4375:
    print("26240.625")
elif operation52 > 25987.5:
    print("26071.875")
elif operation52 > 25903.152:
    print("25987.5")
elif operation52 > 25860.9375:
    print("25903.125")
elif operation52 > 25650:
    print("25734.375")
elif operation52 > 25565.652:
    print("25650")
elif operation52 > 25523.4375:
    print("25565.625")
elif operation52 > 25312.5:
    print("25396.875")
elif operation52 > 25228.152:
    print("25312.5")
elif operation52 > 25185.9375:
    print("25228.125")
elif operation52 > 24975:
    print("25059.375")
elif operation52 > 24890.652:
    print("24975")
elif operation52 > 24848.4375:
    print("24890.625")
elif operation52 > 24637.5:
    print("24721.875")
elif operation52 > 24553.152:
    print("24637.5")
elif operation52 > 24510.9375:
    print("24553.125")
elif operation52 > 24300:
    print("24384.375")
elif operation52 > 24215.652:
    print("24300")
elif operation52 > 24173.4375:
    print("24215.625")
elif operation52 > 23962.5:
    print("24046.875")
elif operation52 > 23878.152:
    print("23962.5")
elif operation52 > 23835.9375:
    print("23878.125")
elif operation52 > 23625:
    print("23709.375")
elif operation52 > 23540.652:
    print("23625")
elif operation52 > 23498.4375:
    print("23540.625")
elif operation52 > 23287.5:
    print("23371.875")
elif operation52 > 23203.152:
    print("23287.5")
elif operation52 > 23160.9375:
    print("23203.125")
elif operation52 > 22950:
    print("23034.375")
elif operation52 > 22865.652:
    print("22950")
elif operation52 > 22823.4375:
    print("22865.625")
elif operation52 > 22612.5:
    print("22696.875")
elif operation52 > 22528.152:
    print("22612.5")
elif operation52 > 22485.9375:
    print("22528.125")
elif operation52 > 22275:
    print("22359.375")
elif operation52 > 22190.652:
    print("22275")
elif operation52 > 22148.4375:
    print("22190.625")
elif operation52 > 21937.5:
    print("22021.875")
elif operation52 > 21853.152:
    print("21937.5")
elif operation52 > 21810.9375:
    print("21853.125")
elif operation52 > 21600:
    print("21684.375")
elif operation52 > 21515.652:
    print("21600")
elif operation52 > 21473.4375:
    print("21515.625")
elif operation52 > 21262.5:
    print("21346.875")
elif operation52 > 21178.152:
    print("21262.5")
elif operation52 > 21135.9375:
    print("21178.125")
elif operation52 > 20925:
    print("21009.375")
elif operation52 > 20840.652:
    print("20925")
elif operation52 > 20798.4375:
    print("20840.625")
elif operation52 > 20587.5:
    print("20671.875")
elif operation52 > 20503.152:
    print("20587.5")
elif operation52 > 20460.9375:
    print("20503.125")
elif operation52 > 20250:
    print("20334.375")
elif operation52 > 20165.652:
    print("20250")
elif operation52 > 20123.4375:
    print("20165.625")
elif operation52 > 19912.5:
    print("19996.875")
elif operation52 > 19828.152:
    print("19912.5")
elif operation52 > 19785.9375:
    print("19828.125")
elif operation52 > 19575:
    print("19659.375")
elif operation52 > 19490.652:
    print("19575")
elif operation52 > 19448.4375:
    print("19490.625")
elif operation52 > 19237.5:
    print("19321.875")
elif operation52 > 19153.152:
    print("19237.5")
elif operation52 > 19110.9375:
    print("19153.125")
elif operation52 > 18900:
    print("18984.375")
elif operation52 > 18815.652:
    print("18900")
elif operation52 > 18773.4375:
    print("18815.625")
elif operation52 > 18562.5:
    print("18646.875")
elif operation52 > 18478.152:
    print("18562.5")
elif operation52 > 18435.9375:
    print("18478.125")
elif operation52 > 18225:
    print("18309.375")
elif operation52 > 18140.652:
    print("18225")
elif operation52 > 18098.4375:
    print("18140.625")
elif operation52 > 17887.5:
    print("17971.875")
elif operation52 > 17803.152:
    print("17887.5")
elif operation52 > 17760.9375:
    print("17803.125")
elif operation52 > 17550:
    print("17634.375")
elif operation52 > 17465.652:
    print("17550")
elif operation52 > 17423.4375:
    print("17465.625")
elif operation52 > 17212.5:
    print("17296.875")
elif operation52 > 17128.152:
    print("17212.5")
elif operation52 > 17085.9375:
    print("17128.125")
elif operation52 > 16875:
    print("16959.375")
elif operation52 > 16790.652:
    print("16875")
elif operation52 > 16748.4375:
    print("16790.625")
elif operation52 > 16537.5:
    print("16621.875")
elif operation52 > 16453.152:
    print("16537.5")
elif operation52 > 16410.9375:
    print("16453.125")
elif operation52 > 16200:
    print("16284.375")
elif operation52 > 16115.652:
    print("16200")
elif operation52 > 16073.4375:
    print("16115.625")
elif operation52 > 15862.5:
    print("15946.875")
elif operation52 > 15778.152:
    print("15862.5")
elif operation52 > 15735.9375:
    print("15778.125")
elif operation52 > 15525:
    print("15609.375")
elif operation52 > 15440.652:
    print("15525")
elif operation52 > 15398.4375:
    print("15440.625")
elif operation52 > 15187.5:
    print("15271.875")
elif operation52 > 15103.152:
    print("15187.5")
elif operation52 > 15060.9375:
    print("15103.125")
elif operation52 > 14850:
    print("14934.375")
elif operation52 > 14765.652:
    print("14850")
elif operation52 > 14723.4375:
    print("14765.625")
elif operation52 > 14512.5:
    print("14596.875")
elif operation52 > 14428.152:
    print("14512.5")
elif operation52 > 14385.9375:
    print("14428.125")
elif operation52 > 14175:
    print("14259.375")
elif operation52 > 14090.652:
    print("14175")
elif operation52 > 14048.4375:
    print("14090.625")
elif operation52 > 13837.5:
    print("13921.875")
elif operation52 > 13753.152:
    print("13837.5")
elif operation52 > 13710.9375:
    print("13753.125")
elif operation52 > 13500:
    print("13584.375")
elif operation52 > 13415.652:
    print("13500")
elif operation52 > 13373.4375:
    print("13415.625")
elif operation52 > 13162.5:
    print("13246.875")
elif operation52 > 13078.152:
    print("13162.5")
elif operation52 > 13035.9375:
    print("13078.125")
elif operation52 > 12825:
    print("12909.375")
elif operation52 > 12740.652:
    print("12825")
elif operation52 > 12698.4375:
    print("12740.625")
elif operation52 > 12487.5:
    print("12571.875")
elif operation52 > 12403.152:
    print("12487.5")
elif operation52 > 12360.9375:
    print("12403.125")
elif operation52 > 12150:
    print("12234.375")
elif operation52 > 12065.652:
    print("12150")
elif operation52 > 12023.4375:
    print("12065.625")
elif operation52 > 11812.5:
    print("11896.875")
elif operation52 > 11728.152:
    print("11812.5")
elif operation52 > 11685.9375:
    print("11728.125")
elif operation52 > 11475:
    print("11559.375")
elif operation52 > 11390.652:
    print("11475")
elif operation52 > 11348.4375:
    print("11390.625")
elif operation52 > 11137.5:
    print("11221.875")
elif operation52 > 11053.152:
    print("11137.5")
elif operation52 > 11010.9375:
    print("11053.125")
elif operation52 > 10800:
    print("10884.375")
elif operation52 > 10715.652:
    print("10800")
elif operation52 > 10673.4375:
    print("10715.625")
elif operation52 > 10462.5:
    print("10546.875")
elif operation52 > 10378.152:
    print("10462.5")
elif operation52 > 10335.9375:
    print("10378.125")
elif operation52 > 10125:
    print("10209.375")
elif operation52 > 10040.652:
    print("10125")
elif operation52 > 9998.4375:
    print("10040.625")
elif operation52 > 9787.5:
    print("9871.875")
elif operation52 > 9703.152:
    print("9787.5")
elif operation52 > 9660.9375:
    print("9703.125")
elif operation52 > 9450:
    print("9534.375")
elif operation52 > 9365.652:
    print("9450")
elif operation52 > 9323.4375:
    print("9365.625")
elif operation52 > 9112.5:
    print("9196.875")
elif operation52 > 9028.152:
    print("9112.5")
elif operation52 > 8985.9375:
    print("9028.125")
elif operation52 > 8775:
    print("8859.375")
elif operation52 > 8690.652:
    print("8775")
elif operation52 > 8648.4375:
    print("8690.625")
elif operation52 > 8437.5:
    print("8521.875")
elif operation52 > 8353.152:
    print("8437.5")
elif operation52 > 8310.9375:
    print("8353.125")
elif operation52 > 8100:
    print("8184.375")
elif operation52 > 8015.652:
    print("8100")
elif operation52 > 7973.4375:
    print("8015.625")
elif operation52 > 7762.5:
    print("7846.875")
elif operation52 > 7678.152:
    print("7762.5")
elif operation52 > 7635.9375:
    print("7678.125")
elif operation52 > 7425:
    print("7509.375")
elif operation52 > 7340.652:
    print("7425")
elif operation52 > 7298.4375:
    print("7340.625")
elif operation52 > 7087.5:
    print("7171.875")
elif operation52 > 7003.152:
    print("7087.5")
elif operation52 > 6960.9375:
    print("7003.125")
elif operation52 > 6750:
    print("6834.375")
elif operation52 > 6665.652:
    print("6750")
elif operation52 > 6623.4375:
    print("6665.625")
elif operation52 > 6412.5:
    print("6496.875")
elif operation52 > 6328.152:
    print("6412.5")
elif operation52 > 6285.9375:
    print("6328.125")
elif operation52 > 6075:
    print("6159.375")
elif operation52 > 5990.652:
    print("6075")
elif operation52 > 5948.4375:
    print("5990.625")
elif operation52 > 5737.5:
    print("5821.875")
elif operation52 > 5653.152:
    print("5737.5")
elif operation52 > 5610.9375:
    print("5653.125")
elif operation52 > 5400:
    print("5484.375")
else:
    print(operation52)

# Create template to to show previous day open, high, low and close values plus probable range for next trading day

tweet_template = "DJIA ({})\n\n{} Open\n{} High\n{} Low\n{} Close\n\nProbable range for ({}):\n{} - {}\n\nNot financial advice"

# Replace the placeholders in the tweet template with actual values

date = pd.Timestamp.today().strftime("%Y-%m-%d")
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")
previous_open = "{:,.2f}".format(exampledata[1][1])
previous_high = "{:,.2f}".format(exampledata[1][2])
previous_low = "{:,.2f}".format(exampledata[1][3])
previous_close = "{:,.2f}".format(exampledata[1][4])

# Calculate the probable high and low prices for the next trading day's close

next_business_day = (pd.Timestamp.today() + BDay(0)).strftime("%Y-%m-%d")
probable_low = "{:,.2f}".format(operation51)
probable_high = "{:,.2f}".format(operation52)


# Create the tweet using the tweet template

body = tweet_template.format(
    yesterday_str,
    previous_open,
    previous_high,
    previous_low,
    previous_close,
    next_business_day,
    probable_low,
    probable_high,
)

""" # Define the high and low values
high = probable_high
low = probable_low"""

# Convert high and low to floats if they are not already floats
# if  probable_high != float:
#     probable_high = float(probable_high)
# if  probable_low != float:
#     probable_low = float(probable_low)
# if type(high) != float:
#     high = float(high)
# if type(low) != float:
#     low = float(high)



# Define the Pine Script code with the probable high and low values
""" pine_script = '// This source code is subject to the terms of the Mozilla Public License 2.0'
pine_script += '// © terrykinder1'
pine_script += ''
pine_script += '//@version=5' """
pine_script = 'indicator("Probable High Low", overlay=true)'
pine_script += "probable_high = {}\n".format(probable_high.replace(",", ""))
pine_script += "probable_low = {}\n".format(probable_low.replace(",", ""))
# pine_script += '// Plot the high and low values as lines with unique names and fixed price levels'
pine_script += 'plot(probable_high, color=color.green, linewidth=2, title="Probable High", trackprice=true)\n'
pine_script += 'plot(probable_low, color=color.red, linewidth=2, title="Probable Low", trackprice=true)\n'
# pine_script += 'plot(probable_high, color=color.green, linewidth=2, overlay=true)\n'
# pine_script += 'plot(probable_low, color=color.red, linewidth=2, overlay=true)\n'

# Save the Pine Script code to a file
try:
    with open("high_low.pine", "w") as f:
        f.write(pine_script)
    print("Pine Script file saved successfully.")
except Exception as e:
    print("Error saving Pine Script file:", e)
# pine_script = 'high = {:,.2f}\n'.format(probable_high)
# pine_script = 'high = {:,.2f}\n'.format(probable_low)
# pine_script = 'high = {:,.2f}\n'.format((str)probable_high)
# pine_script += 'low = {:,.2f}\n'.format((str)probable_low)
# pine_script += 'plot(high, color=color.green)\n'
# pine_script += 'plot(low, color=color.red)\n'
# pine_script = 'high = {}\n'.format(probable_high)
# pine_script += 'low = {}\n'.format(probable_low)
# pine_script += 'plot(high, color=color.green)\n'
# pine_script += 'plot(low, color=color.red)\n'

# Save the Pine Script code to a file
# try:
#     with open('high_low.pine', 'w') as f:
#         f.write(pine_script)
#     print('Pine Script file saved successfully.')
# except Exception as e:
#     print('Error saving Pine Script file:', e)

""" # Format the probable high and low values
probable_high = round(float(probable_high.replace(",", "")), 2)
probable_low = round(float(probable_low.replace(",", "")), 2)

# Export the probable high and low values to a CSV file
try:
    with open("high_low.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["High", "Low"])
        writer.writerow([probable_high, probable_low])
except Exception as e:
    print(f"Error: {e}")
else:
    print("CSV file created successfully!")
    
# Create the Pine Script for the daily high and low

# Read the CSV file
data = csv("C:/Python311/djia_probable_range_blogger/high_low.csv") """

# Extract the high and low values
# probable_high = data.value[0]
# probable_low = data.value[1]


# # Export the high and low values to a CSV file
# try:
#     with open("high_low.csv", "w", newline="") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(["High", "Low"])
#         writer.writerow([probable_high, probable_low])
# except Exception as e:
#     print(f"Error: {e}")
# else:
#     print("CSV file created successfully!")

# Login to Trading View 

""" with open('C:\Python311\djia_probable_range_blogger\squirrel.json', 'r') as f:
    credentials = json.load(f)

username = credentials['username']
password = credentials['password']

tv.login(username, password)

# Open the chart you want to update
symbol = "DJI"
interval = "1h"

chart = tv.chart(symbol, interval)

# Open the Pine Script location of file to be published on Trading View

with open("C:/Python311/djia_probable_range_blogger/high_low.pine", "r") as f:
    pine_script = f.read()

# Publish the updated Pine Script
chart.publish('8gD08TvJ', pine_script) """

# Get the DJIA information
symbol = "DJI"
interval = Interval.INTERVAL_1_HOUR
exchange = "DJ"
screener = "cfd"
handler = TA_Handler(
    symbol=symbol,
    interval=interval,
    exchange = exchange,
    screener = screener
    )
# handler.set_symbol_as(symbol)
# handler.set_interval_as(interval)
djia_data = handler.get_dataframe()

# # Get the DJIA information
# symbol = "DJI"
# interval = Interval.INTERVAL_1_HOUR
# handler = TA_Handler()
# handler.set_symbol_as(symbol)
# handler.set_interval_as(interval)
# djia_data = handler.get_dataframe()

# Convert the DJIA data to a Pandas DataFrame
djia_df = pd.DataFrame(djia_data)

# Draw the chart with Plotly
fig = go.Figure(data=[go.Candlestick(x=djia_df.index,
                                      open=djia_df['open'],
                                      high=djia_df['high'],
                                      low=djia_df['low'],
                                      close=djia_df['close'])])

# Apply the Pine script to the DJIA data
with open("C:/Python311/djia_probable_range_blogger/high_low.pine", "r") as f:
    pine_script = f.read()
handler.apply_indicator(pine_script)

# Get the current date and time
now = datetime.datetime.now()

# Add the current date and time to the chart title
fig.update_layout(title="DJIA Probable Range - {}".format(now.strftime("%Y-%m-%d %H:%M:%S")))

# Create a variable to store the name of the chart image
chart_name = "chart_{}.jpg".format(now.strftime("%Y-%m-%d_%H-%M-%S"))

# Write the chart image to a file with the updated name
chart_name = "chart_{}.jpg".format(now.strftime("%Y-%m-%d_%H-%M-%S"))
fig.write_image("C:/Python311/djia_probable_range_blogger/images/{}".format(chart_name), format="jpeg", width=800, height=600, scale=1, responsive=True)

# Define the blog ID

blog_id = '4845598872127481481'
post_content = body

# Get the URL of the chart image
chart_url = "C:/Python311/djia_probable_range_blogger/images/{}".format(chart_name)

# Create the Blogger post content with the chart image
# post = {
#     'title': 'Probable range for' + " " + date,
#     'content': '<p>Date: ' + yesterday_str + '</p><p>Open: ' + str(previous_open) + '</p><p>High: ' + str(previous_high) + '</p><p>Low: ' + str(previous_low) + '</p><p>Close: ' + str(previous_close) + '</p><p>Next business day: ' + next_business_day + '</p><p>Probable low: ' + str(probable_low) + '</p><p>Probable high: ' + str(probable_high) + '</p><img src="{}">'.format(chart_url)
# }

# Create a new Blogger blog post with content and chart image and print error message if blog fails to post or URL of blog if post is successful

try:
    post = {
        'title': 'Probable range for' + " " + date,
        'content': '<p>Date: ' + yesterday_str + '</p><p>Open: ' + str(previous_open) + '</p><p>High: ' + str(previous_high) + '</p><p>Low: ' + str(previous_low) + '</p><p>Close: ' + str(previous_close) + '</p><p>Next business day: ' + next_business_day + '</p><p>Probable low: ' + str(probable_low) + '</p><p>Probable high: ' + str(probable_high) + '</p><img src="{}">'.format(chart_url)
        # 'content': '<p>Date: ' + yesterday_str + '</p><p>Open: ' + str(previous_open) + '</p><p>High: ' + str(previous_high) + '</p><p>Low: ' + str(previous_low) + '</p><p>Close: ' + str(previous_close) + '</p><p>Next business day: ' + next_business_day + '</p><p>Probable low: ' + str(probable_low) + '</p><p>Probable high: ' + str(probable_high) + '</p>'
    }
    request = service.posts().insert(blogId=blog_id, body=post, isDraft=False)
    response = request.execute()
    print('New post created: {}'.format(response['url']))
except HttpError as error:
    print('An error occurred: {}'.format(error))
