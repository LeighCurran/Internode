[![buy me a coffee](https://img.shields.io/badge/If%20you%20like%20it-Buy%20us%20a%20coffee-green.svg?style=for-the-badge)](https://www.buymeacoffee.com/leighcurran)
![Maintenance](https://img.shields.io/maintenance/yes/2021.svg?style=for-the-badge)

Internode is a package to pull data from https://customer-webtools-api.internode.on.net/api/v1.5. To use the Internode API you need a valid account with Internode.

## Requirements
- Install Python 3.9 (for all users)
- Pip install requests

## Usage

Connect to Internode API:

    import internode
    Internode = internode.api("user.name@outlook.com", "password")

To get service information use the following:

    Internode.getservice()

To get current usage information use the following:

    Internode.getusage()

To get the last day's history information use the following:

    Internode.gethistory()

Full example:

    Internode = internode.api("user.name@outlook.com", "password")
    if (not Internode.Error):
        Internode.getservice()
        print(Internode.service)
        
        Internode.getusage()
        print(Internode.usage)
        
        Internode.gethistory()
        print(Internode.history)
        
    else:
        print(Internode.Error)