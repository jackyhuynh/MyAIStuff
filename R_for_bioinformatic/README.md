# R_for_Bioinformatic

<div class="LI-profile-badge"  data-version="v1" data-size="medium" data-locale="en_US" data-type="horizontal" data-theme="dark" data-vanity="trucdev"><a class="LI-simple-link" href='https://www.linkedin.com/in/trucdev?trk=profile-badge'>Truc Huynh</a></div>

## Introduction

Bioinformatics is a rapidly maturing field that is driving the collection, analysis, and interpretation of biological data using computational methods. This repo is designed to give readers a comprehensive entry-level introduction to bioinformatics. The contents will integrate both theoretical knowledge and hands-on experience using the  R programming language through small-scale projects. Emphasis will be placed on biological sequences (DNA, RNA, protein) analysis, and their applications...

Please refer to the Report.PDF in each folder solution for more details.

- More references can be found at [Computational Biology by Scott T. Kelley](https://www.barnesandnoble.com/w/computational-biology-scott-t-kelley/1133679834#:~:text=Computational%20Biology:%20A%20Hypertextbook,%20by%20Scott%20Kelley%20and,are%20integrated%20to%20form%20a%20complete%20educational%20resource.)

- [A Little Book of R For Bioinformatics](https://buildmedia.readthedocs.org/media/pdf/a-little-book-of-r-for-bioinformatics/latest/a-little-book-of-r-for-bioinformatics.pdf)

- fasta file can be download at [NCBI](https://www.ncbi.nlm.nih.gov/)

<img src="https://github.com/jackyhuynh/collection_of_data_science_and_data_visualization_exercise/blob/main/R_for_bioinformatic/images/bioinformatics.png" width="400" height="400" margin-left:auto margin-right:auto>

## What is DNA

"Deoxyribonucleic acid, other wise (thank fully) known as DNA, is life’s single most important  molecule.  DNA  underpins  virtually all of biology. With the exception of a few viuses,1 life encodes it self using the chemical nucleotides of the DNA dou-ble helix. Every living cell contains its molecular information in the form of DNA, in cluding the 1 trillion cells in the human body and every animal, plant, fungal, and bacterial cell on the planet. Placed end to end, the DNA from a single human cell could stretch an astonishing 3 meters. The amount of raw in formation contained in this 3-meter length of DNA is similarly remarkable. The unit of molecular infor-mation in DNA is the nucleotide. Thus, the human genome, the com plete set of all the DNA information contained in each cell, contains approximately 3 billion pieces of information.Theoretically, the ability to read and interpret this chemical code should allow us to learn a great deal about how cells and organisms function and interact."

Gene is the book contain everything about human body. have the ability to copy of itself 

DNA is a frame work it is not Protein.

## Central Dogma

![Img](https://github.com/jackyhuynh/collection_of_data_science_and_data_visualization_exercise/blob/main/R_for_bioinformatic/images/DNA_Replicate.PNG)

## Gene

A gene i sthe basic physicial and functional unit of heredity
Gene can vary in size from a few hundred DNA bases to more than 2 million bases
TheHuman Genome Projectes timated that humans have between 20,000 and 25,000 genes

![Img](https://github.com/jackyhuynh/collection_of_data_science_and_data_visualization_exercise/blob/main/R_for_bioinformatic/images/gene.PNG)

[**Exercise 1**]()

## Protein

Some genes act as instructionsto make molecules called proteins:
- Some proteins are structural and make up our tissueslike bones and muscles. 
- Proteins calledenzymesare involved in chemical reactions like breaking down the food we eat.
- Others are like little messengers that send signals around our body, these proteins are known ashormones.

Scientists giving genes  unique names /symbols (CFTR). Make everything in our body. Hair, nails , skin. How well our body produce Protein.


### Technology
* Bio-Informatic
* Machine Learning
* Data Visualization
* HTML
* CSS
* Artifical Intelligence
* Data Analysis
* Data Exploration: Explore min, max, mean, standard deviation, correlation, and else.
* Data Transformation
* Plotting Methods
* Principal Component Analysis (PCA)
* Eigen Vector
* Hopskin Statistic
* Confusion Matrix
* Clustering Methods
* Predictive Models


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Data
Each project will contatin each own data and readme file

### Prerequisites
What things you need to install the software and how to install them:
- R CRAN Project: R is a free software environment for statistical computing and graphics. It compiles and runs on a wide variety of UNIX platforms, Windows and macOS
- RStudio IDE: RStudio is an integrated development environment (IDE) for R. It includes a console, syntax-highlighting editor that supports direct code execution, as well as tools for plotting, history, debugging, and workspace management. Click here to see more RStudio features. RStudio is available in open source and commercial editions and runs on the desktop (Windows, Mac, and Linux) or in a browser connected to RStudio Server or RStudio Server Pro (Debian/Ubuntu, Red Hat/CentOS, and SUSE Linux)
- BioConductor Package: Design for using with BioInformatic packages.


### Installing

A step by step series of examples that tell you how to get a development environment running:
* [Install R](https://www.r-project.org/) - If you haven't downloaded and installed R, here's how to get started.
* [R Studio IDE](https://rstudio.com/products/rstudio/#:~:text=RStudio%20Take%20control%20of%20your%20R%20code%20RStudio,tools%20for%20plotting,%20history,%20debugging%20and%20workspace%20management.) - After that choose R Studio Desktop, and the free version (unless you have the Pro install). R free version is a pretty good IDE.
* [Install Bioconductor Packages](https://bioconductor.org/install/)

## Running the tests

### Data
Explain how to run the automated tests for this system:
- Start R Studio.
- Create new a project.
- Copy the src folder (source code) which include the markdown file (.rmd) into the source file. For example:
```
~/Fraud-TransactionsDetectionSystem/markdown.rmd
~/Fraud-TransactionsDetectionSystem/data.csv
```

- you can store the WholesaleCustomersData.csv in the same folder, but it is recommended to store in a data as below (coding standard):
```
~/Fraud-TransactionsDetectionSystem/data/data.csv
```

- Make sure to change the import code on top if you want to move your data anywhere. Depend on where you download the code. Your path will be different from mine. Please replace the path below with your  path:
```
# Import Data
Rdata <- read.csv("~/R/DataMining/FaultAnalyst.CreditCard/data/data.csv", header=TRUE)
# path:"~/R/DataMining/FaultAnalyst.CreditCard/data/data.csv"
```

- Please take a quick view of [import data in R](https://support.rstudio.com/hc/en-us/articles/218611977-Importing-Data-with-RStudio?mobile_site=true) if you fail to change the import code.
- Run the IDE by Choose the Knit option:
```
hit the "Knit" button
```
### Data Visualization:

There is chart and plot in each small exercises. Please refer to each of them for more details.

## Deployment
This research and its small application can be use for many bioinformatic application

More continuous attributes can just be added to the application, and it should work fine (with a bit of modification). Please refer to my research paper for a better understanding. [Full research paper can be found here](https://github.com/jackyhuynh/collection_of_data_science_and_data_visualization_exercise/tree/main/R_for_bioinformatic/bioinformatic_fomula_using_r).

I will not guarantee that this application will work "Big data set". If you are interested in a "Big(or Large) data set" please join here for [an argument](https://www.researchgate.net/post/How-much-data-is-considered-to-be-small-data-Large-data-in-data-mining) on what data set is considered a large data set in data mining.

## Built With

* [R Studio IDE](https://rstudio.com/products/rstudio/#:~:text=RStudio%20Take%20control%20of%20your%20R%20code%20RStudio,tools%20for%20plotting,%20history,%20debugging%20and%20workspace%20management.) 
* [R CRAN Project](https://www.r-project.org/)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Truc Huynh** - *Initial work* - [TrucDev](https://github.com/jackyhuynh)

## References

my README.md format was retrieved from
* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
* **Purdue University FortWayne** - where I represent this research in presentation and get improved feedback.

