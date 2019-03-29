loan <- read.delim("F:/Imarticus learntron Final Projects/Python Project Material/XYZCorp_LendingData.txt",header = T)
View(loan)

nrow(loan)
ncol(loan)

str(loan)
colnames(loan)

#Check Null,blanks, zeros,NA's,?

col_name <- colnames(loan)[apply(loan,2, function(n) any(is.na(n)))]
if(length(col_name)>0)
{
  print("NA is present in columns : ")
  print(col_name)
}else
  print("No NA")

col_name <- colnames(loan) [apply(loan, 2, function(n) any(n == ""))]
if(length(col_name) >0)
{
  print("Blank is present in column : ")
  print(col_name)
}else
  print("No Blanks")

col_name <- colnames(loan) [apply(loan,2,function(n) any(n == 0))]
if(length(col_name) >0)
{
  print("0 present in column : ")
  print(col_name)
}else
  print("No zero's")

col_name <- colnames(loan) [apply(loan,2,function(n) any(n == "?"))]
if(length(col_name) >0)
{
  print("? present in column : ")
  print(col_name)
}else
  print("No ?")


#dividing dataset into train and test
train_loan <- loan[loan$issue_d]

