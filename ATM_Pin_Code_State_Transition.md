State Transition Testing for ATM Pin Code

1. States:
   
         • S0: Start Screen

         • S1: Wait for PIN Screen

         • S2: First PIN Attempt

         • S3: Second PIN Attempt

         • S4: Third PIN Attempt

         • S5: Access Account

         • S6: Card Eaten

2. Transitions:
   
         • T1:  Start Screen -> Wait for PIN Screen (Event: User presses "Start")

         • T2: Wait for PIN Screen -> First PIN Attempt (Event: User enters PIN)

         • T3: First PIN Attempt -> Second PIN Attempt (Event: Incorrect PIN)

         • T4: First PIN Attempt -> Access Account (Event: Correct PIN)

         • T5: Second PIN Attempt -> Third PIN Attempt (Event: Incorrect PIN)

         • T6: Second PIN Attempt -> Access Account (Event: Correct PIN)

         • T7: Third PIN Attempt -> Card Eaten (Event: Incorrect PIN)

         • T8: Third PIN Attempt -> Access Account (Event: Correct PIN)

3. Events:

   • User presses "Start"
   
   • User enters PIN
   
   • Correct PIN
   
   • Incorrect PIN

4. State Transition Table:

   | Current State  | Event               | Next State   |
   | -------------- | ------------------- | -----------  |
   | S0             | User presses "Start"| S1           |
   | S1             | User Enters PIN     | S2           |
   | S2             | Correct PIN         | S5           |
   | S2             | Incorrect PIN       | S3           |
   | S3             | Correct PIN         | S5           |
   | S3             | Incorrect PIN       | S4           |
   | S4             | Correct PIN         | S5           |
   | S4             | Incorrect PIN       | S6           |



