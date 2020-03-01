

if (!require("ggplot2")) install.packages("ggplot2")
if (!require("ggthemes")) install.packages("ggthemes")
if (!require("scales")) install.packages("scales")
if (!require("dplyr")) install.packages("dplyr")
if (!require("mice")) install.packages("mice")
if (!require("randomForest")) install.packages("randomForest")

# Load packages
library('ggplot2') # visualization
library('ggthemes') # visualization
library('scales') # visualization
library('dplyr') # data manipulation
library('mice') # imputation
library('randomForest') # classification algorithm
install.packages("doBy")


getwd()
setwd("C:/Users/Ana/Documents/GitHub/assignments/CA2/data_out")
ca2_analiza <- read.csv('dataset_output.csv', stringsAsFactors = F)

str(ca2_analiza)
average_number_of_changes = mean(ca2_analiza$changes)
average_number_of_comment = mean(ca2_analiza$number.of.lines)
commits_per_developer <- ca2_analiza %>% group_by(name) %>% tally()

average_number_of_changes
average_number_of_comment

ca2_analiza$name[name == '/OU=Domain Control Validated/CN=svn.company.net'] = 'Ana'
name<-(ca2_analiza$name)
revision<-(ca2_analiza$revision)

ggplot(ca2_analiza, aes(x=name, y=revision)) + geom_bar(stat="Identity") + 
  labs(x="name", y="revision") +
  theme(axis.text.x = element_text(angle = 90)) +
  theme(axis.text.y = element_blank())


