# Language_Analytics_Assignment_2
## ------ SCRIPT DESCRIPTION ------
This repository contains a script that takes the dataset "fake_or_real_news.csv" and create a new dataset with either the Fake or Real news polarity and named entities. Furthermore, if the user wishes the script will print the top X named entities.

The script will:
- Create a new .csv file with either the Real or fake news.
- Append each articles polarity and named entities
- Print the top X* named entities in the terminal. 
  - * specified by the user

## ------ METHODS ------


## ------ DATA ------
The data is a .csv file containing around 6335 fake and real news articles divided into the columns "title", "text" and "label".

The data was obtained through the language analytics course.

## ------ REPO STRUCTURE ------
"src" FOLDER:
- This folder contains the .py script.

"in" FOLDER:
- This is where the data used in the scripts should be placed. Ie. where the "fake_or_real_news.csv" should be placed.

"out" FOLDER:
- This is where the new .csv files will be placed.

"utils" FOLDER:
- This folder should include all utility scripts used by the main script.

## ------ SCRIPT USAGE ------
**Required**
- The model_creation.py script requires you to give the arguments "-l" / "--label" (The name of the label you want to use the script on. Ie. "FAKE" or "REAL" )

**Optional**
- The poster_prediction.py script requires you to give the argument "-o" / "--output" (The filepath to the place you want to place the folders in (without the output filename). If none is given the file will be outputted to the "out" folder.
- The poster_prediction.py script requires you to give the argument "-t" / "--" (the name of the image plot file created by the script)

## ------ RESULTS ------
The model achieves what it sets out to do. However, we might quickly run into problems if the script is used to find similar images in the eyes of a human. That is because while the histograms (in other words the color concentrations and values) of the images might be similar, what the images actually depict might not be. That is why finding similar images is probably better achieved using something like feature extraction and the nearest_neighbor function from sklearn.
