flowchart LR

  %% --- Subgraph: Freedom Future ---
  subgraph A[Freedom Future]
  direction TB
  A1["Create or Update <br> Future Transactions"]
  A2{"Due Date <br> Reached?"}
  A3["Discord Prompt: <br> 'Confirm Payment?'"]
  A4{"Payment <br> Confirmed?"}
  A5["Move to <br> Transaction Past"]
  end

  %% --- Subgraph: Transaction Past ---
  subgraph B[Transaction Past]
  direction TB
  B1["Stores Completed <br> Transactions"]
  B2["Reconcile with <br> Statements"]
  B3{"Already Exists <br> in Past?"}
  B4["Mark <br> Reconciled"]
  B5["Unknown or New <br> Transaction"]
  B6["Add Manually & <br> Update Accounts"]
  
  B7{"3 Similar <br> Entries?"}
  B8["Add to <br> Recurring Index"]
  end

  %% --- Subgraph: Accounts Present ---
  subgraph C[Accounts Present]
  C1["Updated Balances <br> (Banks/Cards/Others)"]
  end

  %% --- Subgraph: Statements & UPI Data ---
  subgraph D[Statements & UPI Data]
  direction TB
  D1["Bank Statements <br> (ICICI, SBI, etc.)"]
  D2["Credit Card Statements <br> (ICICI Coral, SBI Elite, etc.)"]
  D3["UPI Apps <br> (Detailed Merchant Info)"]
  end

  %% --- Subgraph: Additional Features ---
  subgraph E[Additional Features]
  direction TB
  E1["Generate 3/6 Month <br> Budget via Freedom Future"]
  E2["Discord Queries: <br> Check Balances, Owed Amounts, etc."]
  E3["Income Allocation <br> & Labeling"]
  end

  %% --- Flow within Freedom Future ---
  A1 --> A2
  A2 -- "Yes" --> A3
  A2 -- "No" --> A1
  A3 --> A4
  A4 -- "Yes" --> A5
  A4 -- "No" --> A1

  %% --- Moving Confirmed Transactions to Past ---
  A5 --> B1
  A5 --> C1

  %% --- Transaction Past Reconciliation ---
  B1 --> B2
  B2 --> D1
  B2 --> D2
  B2 --> D3
  D1 --> B3
  D2 --> B3
  D3 --> B3

  %% --- Check if Transaction Already Exists ---
  B3 -- "Yes" --> B4
  B4 --> C1

  B3 -- "No" --> B5
  B5 --> B6
  B6 --> C1
  B6 --> B7

  %% --- Recurring Index Prompt for Repeated Transactions ---
  B7 -- "Yes" --> B8
  B8 --> A1

  %% --- Additional Feature Hooks ---
  A1 --> E1
  C1 --> E2
  B1 --> E3
