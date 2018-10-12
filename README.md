# Date Entity Extractor
## Text Analytics Homework 1

The following `hw1.py` will take a given input file and extract exact date and time entity using relative expressions. Specifically, it will pull [US national holidays](https://www.redcort.com/us-federal-bank-holidays/) and fixed dates (both numerical and written notations), but will not pull relative dates, like "two years ago" and "the day before yesterday".

To run the script, run the following with your own arguments or utilize the defaults below:

```
python hw1.py --input input.txt --output.txt
```