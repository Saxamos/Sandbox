# VowPal Wabbit

## Overview of VowPal Wabbit
The Vowpal Wabbit (VW) project is a fast out-of-core learning system sponsored by Yahoo! Research and written by John Langford along with a number of contributors.

Via parallel learning, it can exceed the throughput of any single machine network interface when doing linear learning, a first amongst learning algorithms.

What does it do well? Online learning & scalable solutions

Its scalability is aided by several factors:
* Out-of-core learning (no need to load all data into memory)
* Exploiting multi-core CPUs (input and learning are done in separate threads)
* Compiled C++ Code

## Requirements 

* Python
* Vowpal Wabbit

## Titanic Predictive Model

We will use VowPal Wabbit (vw) to develop a model to predict whether a passenger would survive or die on the Titanic. This demo is based on a [code from MLwave] (http://mlwave.com/tutorial-titanic-machine-learning-from-distaster/)

### Data Input & Exploration 

The [Commandline](https://github.com/JohnLangford/vowpal_wabbit/wiki/Command-line-arguments) list on github provides useful commands in C++. We will use Python for some of the manipulations. 

VowPal Wabbit has a specific [input format](https://github.com/JohnLangford/vowpal_wabbit/wiki/Input-format). We will use the provided python code (convert_csv_to_vw.py) to convert the train.csv and test.csv files.

```
python convert_csv_to_vw_<your_data>.py
```
This should generate two new new files called train.vw and test.vw

### Generating a predictive model
Now that the data is in vw format, we can start training a model. 
```
vw train.vw -f model.vw --binary --passes 20 -c -q ff --adaptive --normalized --l1 0.00000001 --l2 0.0000001 -b 24
```
A explanation of each command is provided in vw_model_options_cheat_sheet.txt

### Predicting Survival using the Model

Now we want our model to predict whether the test.csv passengers will survive or not. 

```
vw -d test.vw -t -i model.vw -p preds_titanic.txt
```
This has saved the predictions into a text file. 

### Converting format

If you want to submit your vw model to the [Kaggle](http://www.kaggle.com) competition, use the provided python script to convert to the Kaggle format. 
```
python convert_vw_to_kaggle.py
```
Now you should have a new file called kaggle_preds.csv that you can submit to the Kaggle Titanic competition. 

## Resources
[VowPal Wabbit Tutorial for the Uninitiated](http://zinkov.com/posts/2013-08-13-vowpal-tutorial/)
This tutorial has fairly easy-to-understand explanations of many of the command line options. 

[Technical Tricks of VowPal Wabbit](http://www.slideshare.net/jakehofman/technical-tricks-of-vowpal-wabbit)
This is technical overview of how the program works (lots of math). 

http://hunch.net/~vw/validate.html