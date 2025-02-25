Below is a **step-by-step** breakdown that organizes your requirements into a clear workflow. These steps refer to the three core sheets in your Excel (or database) setup—**Transaction Past**, **Accounts Present**, and **Freedom Future**—and include reconciliation and Discord integration.

---

## 1. **Core Sheets & Their Roles**

1. **Transaction Past**  
   - **Purpose**: Stores all *completed* transactions (historical record).  
   - **Data Fields** (typical): *Date, Description, Category, Amount (Debit/Credit), Related Account, Status (Reconciled/Unreconciled)*.  

2. **Accounts Present**  
   - **Purpose**: Holds *current* balances for all your bank accounts, credit cards, and any other financial instruments.  
   - **Data Fields**: *Account Name, Current Balance, Last Updated Date, etc.*  

3. **Freedom Future**  
   - **Purpose**: Lists *planned* or *budgeted* transactions (income or expenses) for upcoming dates.  
   - **Data Fields**: *Planned Date, Description, Category, Expected Amount, Frequency (if recurring), Payment Method*.

---

## 2. **Future Transactions: Creation & Execution**

1. **Add a Future Transaction**  
   1. In **Freedom Future**, enter details (e.g., *Rent, 1st of the month, ₹10,000*).  
   2. If it is recurring (e.g., monthly rent), mark the frequency (monthly).  

2. **Automated Reminder & Transfer to Past**  
   1. **On Due Date**: A Discord bot message prompts you: “*Transaction X is due today. Confirm payment?*”  
   2. If you react or reply **“Yes”** (thumbs-up):  
      - **Remove** that transaction from **Freedom Future**.  
      - **Add** it automatically to **Transaction Past** (with the actual payment date).  
      - **Update** the relevant account in **Accounts Present** (e.g., deducting ₹10,000 from *ICICI Savings*).  

3. **Overdue Transactions**  
   - If a transaction’s date is past, and you haven’t confirmed payment, the system flags it as **overdue**. You can manually mark it *paid / canceled / rescheduled*.

---

## 3. **Reconciliation Workflow**

1. **Collect Statements from All Sources**  
   - **Bank Accounts**: 
     - ICICI Savings  
     - ICICI Corporate  
     - SBI Savings  
   - **Credit Cards**:  
     - ICICI Coral  
     - ICICI Amazon Pay  
     - SBI Elite  
     - DBS Premium  

2. **Consolidate Transactions**  
   1. **Parse Bank Statements**: (CSV/Excel/PDF)  
      - For each transaction, identify *date, amount, reference number, partial description*.  
   2. **Parse Credit Card Statements**:  
      - Break down each credit card transaction for more detailed particulars (since the bank statement only shows bulk debit for credit card bills).  
   3. **Use UPI Apps** for Additional Details:  
      - Match the partial descriptions from bank statements (e.g., “UPI/1234/ABC Stores”) with the actual store names from UPI logs (e.g., “ABC Supermarket”).  

3. **Chronological Merge into Transaction Past**  
   1. **Check if Transaction Already Exists in Transaction Past** (from Freedom Future or manual entry).  
      - If **exists**: Mark it as **Reconciled**.  
      - If **not found**: Create a *new* entry in **Transaction Past** and mark as *Unreconciled* until you confirm details.  
   2. **Categorization**:  
      - If a transaction has appeared ≥3 times with the same store/description, **auto-suggest** category/store mapping.  
      - Confirm or adjust the suggested category to finalize reconciliation.

4. **Finalize Reconciliation**  
   - Once matched and categorized, set the **Status** to “Reconciled” in **Transaction Past**.  
   - Update the **Accounts Present** balance accordingly.

---

## 4. **Adding New/One-Off Transactions**

1. **Direct Entry to Transaction Past**  
   - For unplanned expenses or income, you can enter them *directly* into **Transaction Past**.  
   - Update the respective account in **Accounts Present**.  

2. **Automatic Recurring Index Update**  
   - If you enter a **similar transaction ≥3 times** manually (same store/payee/category), the system prompts:  
     - “Do you want to add this to *Freedom Future*’s Recurring Index?”  
   - If “Yes,” it becomes part of your recurring list in **Freedom Future**.

---

## 5. **Budget Projection & Recurring Index**

1. **Generate Next N Months’ Budget**  
   - From **Freedom Future**, select “Generate Budget for X months.”  
   - The system will:  
     1. **Duplicate** all known recurring transactions for the requested period (e.g., *Rent*, *Utilities*, *Subscriptions*).  
     2. **Summarize** total projected expenditures vs. income.  

2. **Adjust & Review**  
   - You can add or remove any anticipated one-time items (e.g., *holiday travel*).  
   - Finalize the budget to see your net balance forecast.

---

## 6. **Discord Integration & Queries**

1. **Real-Time Status Queries**  
   - Via Discord bot commands, you can ask:  
     - “**What is my current liquid balance?**”  
       - The bot checks **Accounts Present** and returns a sum of *available funds*.  
     - “**How much do I owe on credit cards?**”  
       - The bot calculates total outstanding from your credit cards in **Accounts Present**.  
     - “**What’s my next week’s/month’s projected cash flow?**”  
       - The bot references **Freedom Future** and any known incomes to show net *expected balance*.

2. **Confirming Transactions**  
   - The bot pings you about due transactions (from **Freedom Future**).  
   - On your confirmation, moves them to **Transaction Past** and updates **Accounts Present**.

---

## 7. **Income Allocation & Labeling**

1. **Pre-Allocation Strategy**  
   - Define *rules* for splitting incoming amounts:  
     - E.g., “Of every ₹1,000 I receive, allocate ₹500 to Rent, ₹300 to Savings, ₹200 to Fun.”  
   - If an unexpected lump sum arrives (e.g., gift from a relative), the system asks:  
     - “How do you want to allocate ₹5,500? Options: [Debt repayment], [Insurance premium], [Emergency fund], etc.”  
   - The system can *suggest* based on your current budget priorities (e.g., if you have unpaid debts, it might prioritize those).

2. **Automatic Categorization of Future Inflows**  
   - When an income transaction is detected (or manually entered), the system uses your rules to:  
     - Update **Accounts Present** (increase balance).  
     - Insert a corresponding entry in **Transaction Past** with a label (e.g., *Income → Salary*).  
     - Optionally, “reserve” portions of that income against future or overdue bills in **Freedom Future**.

---

## 8. **Edge Cases & Additional Notes**

1. **Unpaid Scheduled Transactions**  
   - If you **skip** paying or confirm you haven’t paid, that transaction remains in **Freedom Future** with a status like “Overdue” or “Missed.”  
   - You can *manually remove* or *reschedule* it if needed.

2. **Cancelled Transactions**  
   - Some future transactions might get cancelled (e.g., a service subscription).  
   - Update in **Freedom Future** to mark as cancelled, so it doesn’t show up again.

3. **Recurring vs. One-Time**  
   - Keep your **Recurring Index** updated. If it’s definitely *not recurring*, ensure it’s marked one-time in **Freedom Future** to avoid confusion in future budget projections.

4. **Statement Mismatches**  
   - If a statement shows a transaction that you never recorded, you’ll need to add it to **Transaction Past** (or dispute it if fraudulent).

---

## 9. **Putting It All Together**

1. **Enter & Maintain Future Transactions** in **Freedom Future** (recurring or one-time).  
2. **Sync & Reconcile** your bank and credit card statements, merging them into **Transaction Past**.  
3. **Use Discord** to confirm payments, check balances, and run budget commands.  
4. **Regularly Update** your allocations and recurring rules so your system auto-suggests how to use new income.  
5. **Monitor** the system’s “Overdue” or “Missed” transactions to keep your finances accurate.

---

### **Summary of the Workflow**

1. **Create/Update** recurring or one-off items in *Freedom Future*.  
2. **When due**, a Discord **prompt** confirms payment.  
3. **On confirmation**, transaction moves to *Transaction Past*, **Accounts Present** updates.  
4. **Reconcile** with statements from all **Bank Accounts** + **Credit Cards**. Use **UPI details** to enrich vendor info.  
5. **Identify** repeated transactions (≥3 times) for auto-suggestion of categories.  
6. **Generate Budgets** for 3/6 months from *Freedom Future*, adjusting as needed.  
7. **Query** balances and debts via Discord at any time.  
8. **Allocate** incoming money based on set rules or suggestions (debt, savings, etc.).  
9. **Repeat** to maintain a continuous, real-time overview of your finances.

---

With these steps, you have a **comprehensive blueprint** for your financial tracking and reconciliation system, leveraging the **Transaction Past**, **Accounts Present**, and **Freedom Future** sheets alongside **Discord** for real-time interaction.