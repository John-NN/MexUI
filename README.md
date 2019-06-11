# BitMex-UI

A graphical UI for BitMex

# What it is. 

This is a trading script for Bitmex API with a very easy to use GUI. 
I have been using this script(s) to manage any number of accounts via API even when bitmex has System overload errors. 

Some explainations: 

Starting the GUI:

For safety reasons, at startup, the trading terminal has no buttons. First you have to select the instrument from the INSTRUMENT
tab and after that you have to choose the type of trade: Buy/Long or Sell/Short.
The instrument Tab is updated automatically and so is the last price for ease of use. 

Position on Balance Ratio = Position Size / Wallet Balance

PoB is used instead of contracts because the managed accounts do not have the same amount of bitcoin in balance so 4000 contracts on one account could be 10% of the balance’s value and on a different account could be 200% of it’s value so instead of contracts we use the ratio between the position size and the wallet balance. This way we ensure that all gains and losses weigh the same on all the accounts.This is also a very good way to keep a linear money management.

A trade with PoB = 0.1 has the position size equal to 10% of the wallet’s balance value.

Example:
– A has 10 BTC
– B has 1 BTC
– C has 0.1 BTC

We want to open a long with PoB = 1 and 1 BTC = 4000$ (at the time of opening the position), this means that every account will have a position size equal to it’s wallet’s balance value:
– A will have 40.000 contracts
– B will have 4000 contracts
– C will have 400 contracts

One input, different position sizes but the same PoB.
The Public version will show contract number updating as the PoB slider is moved.


Grids/Limits:

The script can place up to 25 orders in a grid stile in one call - I find this very usefull when volatility is high. 
The grid call will use it's PoB slider to spread out the wanted money management using the number of orders wanted. 


There are several progressions available.

Stops , limits and Take profit orders are self explainatory. One note : Stop Loss are Stop Market orders of 9'999'999 contracts. This is a specific matermark since Mex does not differentiate Stop reduce only and Stop entry orders. A Stop entry order will always have another value that 9'999'999 contracts and can be identified as a Stop entry easily. 


Automations : 

For now only the Break even Automation is available in the public script. 
A B/e Auth of 1% will wait for a price move of at least 1% in profit to place a break even stop loss and , if selected , clean all trade side orders found and/or , if selected , will isolate and force a close to break even liquidation to prevent high slippage in case of sharp market moves. 

What will be added : 

A complete acount percentage risk isolated call to make money management even easier. 

A Dinamic TP automation.

A weighted TP autoamtion.

Social trading posibility linking user terminals over the internet. 



# Install

(tested on Ubuntu 18LTS fresh install)

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install -y gcc g++ make libncurses5-dev libreadline6-dev libssl-dev libgdbm-dev libc6-dev libsqlite3-dev libbz2-dev xz-utils patch wget tar curl bzip2 zlib1g-dev python-bsddb3 git

sudo apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev python-dev python-pip python-dev build-essential python-wxtools

sudo pip install Pyro4==4.60 bitmex-ws future jsonref jsonrpclib-pelix websocket

sudo pip install -U requests

git clone https://github.com/John-NN/MexUI.git


# Run the script

cd into MexUI directory and start:

cd MexUI

start the script :

python MexBot API_KEY=<YOUR_API_KEY> API_SECRET=<YOUR_API_KEY_SECRET> LiveNET=True AccName=<NAME_OF_ACCOUNT> TAG=<TRADETERM_TAG>

API_KEY= Use your API key. No space, no quotes

API_SECRET= Use your API secret. No space, no quotes

LiveNET= Optional: Leave this out and script will start on testnet , use True for realnet ( after experimenting a little on Testnet )

AccName= Optional: Leave this out and it will default to "PublicAcc" else use whatever name you want to give to this account

TAG= Optional: The tag to listen to for the trading terminal

# example 
python MexBot.py API_KEY=O8hbNQfSwK79XbxmZw4x4s6V API_SECRET=ko1qdH3UbtR1Y-zA9-QhfvDk5wWQuW9R3nWjorSrVvtxqP1r  LiveNET=False AccName=Tester TAG=MyTag

# Run the trade terminal

Open a new terminal and run from the same folder:

python Terminal.py

N-joy :)
