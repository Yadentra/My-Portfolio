## Decision Table Testing

Decision table for testing the discount application logic in the train ticket system:

1. Conditions:
   
        • C1: Senior Citizen (age 65 or older)
        • C2: Student
        • C3: Off-Peak Hours
        • C4: Frequent Traveler Card

3. Discount Percentages:

        • C1: 20%
        • C2: 15%
        • C3: 10%
        • C4: 5%



## Decision Table

  | Test Cases    | C1       | C2       | C3       | C4       | Total Discount |
  | ------------- | -------- | -------- | -------- | -------- | -------------  |
  | 1             | N        | N        | N        | N        |      20 %      |
  | 2             | Y        | N        | N        | N        |      20 %      |
  | 3             | N        | Y        | N        | N        |      15 %      |
  | 4             | N        | N        | N        | Y        |      10 %      |
  | 5             | N        | N        | N        | Y        |       5 %      |
  | 6             | Y        | Y        | N        | N        |      35 %      |
  | 7             | Y        | N        | Y        | N        |      30 %      |
  | 8             | Y        | N        | N        | Y        |      25 %      |
  | 9             | N        | Y        | Y        | N        |      25 %      |
  | 10            | N        | N        | Y        | Y        |      15 %      |
  | 11            | N        | N        | Y        | Y        |      15 %      |
  | 12            | Y        | Y        | Y        | N        |      45 %      |
  | 13            | Y        | Y        | N        | Y        |      40 %      |
  | 14            | Y        | N        | Y        | Y        |      35 %      |
  | 15            | N        | Y        | Y        | Y        |      30 %      |
  | 16            | Y        | Y        | Y        | Y        |      50 %      |


  3. Total Discount Calculation:

          • Test Case 1: No discounts apply, so the total discount is 0%.
  
          • Test Case 6:  Senior Citizen (20%) + Student (15%) = 35%
  
          • Test Case 16:  All discounts apply: 20% + 15% + 10% + 5% = 50%
  

## Benefits of Decision Table Testing:

          • Clear and Concise: Decision tables provide a structured and organized way to represent complex logic.

          • Comprehensive Coverage: They ensure that all possible combinations of conditions are tested.

          • Easy to Understand:  Even non-technical stakeholders can easily understand the decision logic.
          

## NOTE:  

We can use this decision table as a basis for creating automated tests for the discount logic within the train ticket system.


