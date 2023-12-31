# cat_breed_analysis_ml_tool
TensorFlow_Hub retrained machine learning model trained to classify a cats breed based on a given image.

Original dataset used to retrain the model: https://www.kaggle.com/datasets/doctrinek/catbreedsrefined-7k
(The Jupyter Notebook code used to retrain the model can be found in the root of the repo.  Only the files within "cat_breed_analysis_tool" are required to function.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.	Install Python 3.11
  a.	https://www.python.org/downloads/release/python-3110/
  b.	The Windows installer (64-bit) is recommended.
  c.	When running the installer, check the box at the bottom of the install shield to, “Add python.exe to PATH.
  d.	After installation, just close the installer.
2.	Open a command prompt (search “cmd” in Windows search)
  a.	Type: pip install TensorFlow
  b.	Type: pip install TensorFlow_Hub
  c.	Type: pip install numpy
  d.	Type: pip install streamlit
3.	Install PyCharm Community Edition
  a.	https://www.jetbrains.com/pycharm/download/?section=windows
  b.	You will find the community edition towards the lower portion of the page.
  c.	You should check the box in the top right to update the path variable.
  d.	After installing, perform a reboot of the operating system.
4.	Download the tensorflow_hub model
  a.	https://www.kaggle.com/datasets/cvsquiggz/sjones-cat-breed-model
  b.	Hit download in the top right corner.
  c.	Save this somewhere you can find it.
5.	Unzip the cat_breed_analysis_tool.zip file submitted with this assignment.
6.	Unzip the tensorflow_hub model file downloaded earlier and store the contents in ‘cat_breed_analysis_tool/tmp’.
  a.	Make sure the tmp folder now contains the cat_breed_model_efficientnetv2-xl-21k folder, and also check that directory contains variables, along with the fingerprint.pb and saved_model.pb.
    i.	If there’s an additional directory between these due to an error in extracting, then the application will not run correctly.
7.	Launch PyCharm and select to open a project then select the unzipped folder and click open.
  a.	Make sure the folder you open is the folder containing the images and the .py file directly. (By default, it may extract to a duplicated folder, i.e., “cat_breed_analysis_tool/cat_breed_analysis_tool/…”)
8.	Specifically open the streamlit_deployment.py file in the tree on the lefthand side of PyCharm by double clicking it.
9.	At the top, it may warn of an Invalid Python interpreter. If it does, do the following sub-steps.
  a.	Click the hyperlink to configure an interpreter.
  b.	Select Add new, and then add local interpreter.
  c.	Inherit global site-packages checkbox.
  d.	Click okay on the next window to create it.
10.	Click the green play button or hit Shift+F10 to execute the code.
11.	The console should pop up at the bottom once it is finished, with a line at the bottom like this:
  a.	Warning: to view this Streamlit app on a browser, run it with the following command: streamlit run E:\School\Final Project\cat_breeds_retrained\tensorLite_deployment.py 
  b.	Copy the command (not including the [ARGUMENTS] bit) to your clipboard.
12.	Click on the Terminal tab at the bottom of PyCharm.
13.	Paste the previously copied line into the terminal and hit enter to execute it.
  a.	It may require apostrophes around it if there are any spaces in any of your folder/file names like there are in the example above \Final Project\.
14.	This should open the Streamlit app in your default web browser.
15.	Type the names of the cat image files in the root project folder (Seen in PyCharm tree) and click classify to evaluate them one at a time.
  a.	The entire image name must be entered exactly, i.e., “siamese_1.jpg”.
  b.	New images can be saved to the root directory to make them available for evaluation by the model.
16.	The image along with its classification will show once the evaluation is complete.
17.	Steps 13 and 14 can be repeated as many times as necessary.
18.	Afterwards, close the browser as well as PyCharm to finish classifying images.
