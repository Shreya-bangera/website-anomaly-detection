Q7)Consider the Fish Prices dataset and perform the following using the 
JMP Pro tool.  
1. Use the DASL Fish Prices data to investigate whether there is evidence 
that overfishing occurred from 1970 to 1980.  
2. Perform a paired t-test for Fish price dataset. Interpret the results, and 
describe the change with confidence intervals.  
CODE: 
# Load necessary library 
library(readxl) 
# Read the Excel file 
data <- read_excel("C:/Users/hp/Desktop/Stats Lab Dataset/fishstory.xls") 
# Perform a paired t-test between 1970 and 1980 prices 
t_test_result <- t.test(data$`1980Price`, data$`1970Price`, paired = TRUE) 
# Print test result 
print(t_test_result) 
# Print mean difference 
mean_diff <- mean(data$`1980Price` - data$`1970Price`, na.rm = TRUE) 
cat("Mean difference in price (1980 - 1970):", mean_diff, "\n") 
# Print confidence interval 
cat("95% Confidence Interval:", t_test_result$conf.int, "\n") 
