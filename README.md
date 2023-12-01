# FlowSentry
Real time performance monitoring of LC-MS systems

# Functionality
This repository contains two scripts responisbile for monitoring and notifying the performance of LC-MS systems.
- ChromChek.py implements tesseract-OCR (https://github.com/tesseract-ocr/tesseract) to monitor the presence of any system errors reported by Xcalibur. These include, sample obstructions and increasing values in column pressure. Upon the apearence of any systematic error, a log is generated and shared to a divice connected to the internet.
- ErrorDispatch.py is used to constantly monitor the logs generated. Should an error be reported it uses slack_sdk to notify the user via slack about the presence of an error through a designated slack-channel.
