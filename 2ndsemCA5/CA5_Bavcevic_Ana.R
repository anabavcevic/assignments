##https://github.com/anabavcevic/assignments/blob/master/2ndsemCA5/CA5_Bavcevic_Ana.R
mydata <- read.csv("C:/Users/anaba/OneDrive/Desktop/DBS/programming for BD/CA5_R/CA1Ana_2.csv")
attach(mydata)
str(mydata)
summary(mydata)
library(ggplot2)

#######################ggp for population density on Cratian Islands########################
####################################################
otok<-(mydata$X)
Populacija<-(mydata$Population.Density)
ggplot(mydata, aes(x=otok, y=Populacija)) + geom_bar(stat="identity", fill = "#36D8BE") + 
  labs(title= "Population Density on Croatian Islands", x="islands", y="population density") + 
  theme(axis.text.x = element_text(angle = 90)) +
  theme(axis.text.y = element_blank())

################### HIghers point of Croatian islands#######################################
#####################################################
otok<-(mydata$X)
visina<-(mydata$Highest.Point)
ggplot(mydata, aes(x=otok, y=visina)) + geom_bar(stat="identity", fill = "#653484") + 
  labs(title= "Highest island peack in Croatia", x="islands", y="highest point") +
  theme(axis.text.x = element_text(angle = 90)) +
  theme(axis.text.y = element_blank())

##########################GGplot Croatian Islands by area################################
###############################################################

otok<-(mydata$X)
povrsina<-(mydata$Area)
ggplot(mydata, aes(x=otok, y=povrsina)) + geom_bar(stat="identity", fill = "#D866AE") + 
  labs(title= "Largest Island in Croatia ", x="islands", y="highest point") +
  theme(axis.text.x = element_text(angle = 90)) +
  theme(axis.text.y = element_blank())

########################## boxplot population by island#############################
##########################################################
boxplot(Population~X,data=mydata, main="Population by Island",
        xlab="Island", ylab="Population")


##########################basic plot population density on each Island #####################
###################################################################
attach(mydata)
plot(X, Population.Density)
abline(lm(Population.Density~X))
title("POpulation density on each Island")


#########################histogram of Island's Areas################################
######################################################
hist(mydata$Area, breaks=12, col="red", xlab="Area", main="Isliand's Areas")

###################################### Filled Density Plot####################
######################################################
d <- density(mydata$Population.Density)

plot(d, main="Population Density on Croatian Island")
polygon(d, col="#ECA6B9", border="#8D72DC")

                                                                                                                             size = 1)