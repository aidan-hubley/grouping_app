# [Inuaai Grouping Script](https://inuaai.com)
<<<<<<< HEAD

<br />

### 👉 Virtual Environment Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
```

<br />

### 👉 Virtual Environment Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```bash
$ python -m venv venv
$ .\venv\Scripts\activate
```

**Install dependencies** using pip

```bash
$ pip install -r requirements.txt
```

**Start the Grouping script**

```bash
$ python Grouping App.py
```

<br />
## Authors
=======
## What does it do?
This application is used to "group" a folder of images together
<br />"grouping" images together simply means to extend their filename to include a group identification number

_Example:_

| Before Grouping | After Grouping |
|-----------------|----------------|
| image0          | image0-1       |
| image1          | image1-1       |
| image2          | image2-2       |
| image3          | image3-2       |
| image4          | image4-3       |
| image5          | image5-4       |

This should allow for easy identification of grouping when editing images

## How to Use the Grouping App
### Step 1: Select Folder
Select a folder that contains .dng images
<br/>(jira card raw image folder)

### Step 2: Group Photos
Select images in the 'Raw Photos' column that belong grouped together
<br />Click the <button>Group Photos</button> button to group selected images
<br />_Note: All raw photos must be grouped, including groups of 1 image_

Select the <button>Review Groups ></button> button

### Step 3: Review Groups
Scroll through the 'Review Groups' column
<br /> Validate that all groups are accurate
<br /> If there is a mistake, select the <button>< Reselect Groups'</button> button
<br /> _Note: The column is scrollable both horizontally and vertically_

Select the <button>Save Groups ></button> button

### Step 4: Repeat?
You have successfully grouped a folder of images!
<br />If you wish to group another folder, select the <button>Select New Folder</button> button

## Authors
<<<<<<<< HEAD:README.md
👤 **Aidan Hubley**
========
>>>>>>> 92a89600bea2741ddf4f02d49faf416822502cff

👤 **Aidan Hubley**
👤 **Joshua Phillips**
👤 **Alex Karoki**
<<<<<<< HEAD
👤 **Timothy Muraya**
=======
👤 **Timothy Muraya**
>>>>>>>> 92a89600bea2741ddf4f02d49faf416822502cff:README(setup).md
>>>>>>> 92a89600bea2741ddf4f02d49faf416822502cff
