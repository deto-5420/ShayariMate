# ShayariMate

•Back-end for a platform where user can post their poetry along with the voice-overs.

•Multiple user can reply to the post with their own voice-overs.

•Applied the logic for re-share(re-tweet) post.

# Installation Guide
## System Configuration

* Ubuntu `20.04` **(Recommended)**
* *OR* WSL for Windows `10` \(Follow the guide below\) :  
    [Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* *OR* Windows `7/8/8.1/10`

## Software Requirements

* Python `3.8`
* Git

## How to get started

* on **Ubuntu**:

    ```sh
    // Install the required packages using the following command:
    
    sudo apt install python3-pip python3-dev python3-venv libpq-dev build-essential git
    sudo -H pip3 install --upgrade pip
    ```

* on **Windows**:

  * Get Python 3.8 from [here](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe) for AMD64/x64 or [here](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe) for x86
  * Git from [here](https://git-scm.com/download/win)
  * Install both using the downloaded `exe` files   
  **Important:** Make sure to check the box that says **Add Python 3.x to PATH** to ensure that the interpreter will be placed in your execution path

### Setting up environment

* Create a virtual environment  
  * on **Ubuntu**: `python3 -m venv env`  
  * on **Windows PowerShell**: `python -m venv env`
* Activate the *env*    
  * on **Ubuntu**: `source env/bin/activate`
  * on **Windows PowerShell**: `.\env\Scripts\Activate.ps1`     
  **Note** : On Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following command: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
* Install the requirements: `pip install -r requirements.txt`

### Running server

* Change directory to **ShayariMate** `cd ShayariMate`
* Run the server `python manage.py runserver`


# APIs
![Screenshot from 2021-06-16 11-16-04](https://user-images.githubusercontent.com/53571579/122177384-3179f780-cea3-11eb-94b1-b91be7fc01d0.png)


