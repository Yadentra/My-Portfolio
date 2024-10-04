# State Transition for ATM Pin Code
## Objective
To validate the behavior of an ATM system based on various states of PIN entry.
## States and Transitions
- **State 1**: Waiting for PIN
  - Transition: User enters PIN → Move to State 2 (Valid PIN) or State 3 (Invalid PIN).
- **State 2**: Valid PIN Entered
  - Actions: Proceed to account selection.
- **State 3**: Invalid PIN Entered
  - Transition: Retry or lock account after max attempts.
