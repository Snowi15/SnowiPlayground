Create a python script  for 
1. Read the "Date"from the freedom_future sheet in kaas.db and get today's transactions
2. Format each of today's transactions as separate message and  notify on telegram.  
3. If user replies yes to any of the messages, move it to transaction_past sheet in kaas.db
4. Update the 'balance' field in account_present sheet with the payment (match "PaymentMode" in freedom_future sheet with "AccountName" in account_present sheet) 

freedom_future sheet
TrNo	Date	Description	Amount	PaymentMode	AccID	Department	Comments	Category
1	24-Feb-25	Samosa Payment	₹ 50.00	ICICI_CA_1849		TradeMan	Subscription 	
2	24-Feb-25	Party 	₹ 100.00	ICICI_CA_1849		TradeMan	Subscription 	
3	28-Feb-25	Cursor	-₹ 2,000.00	ICICI70090		TradeMan	Subscription	
4	1-Mar-25	Claude API	-₹ 5,000.00	CC_DBS_209		TradeMan	Subscription	
5	1-Mar-25	Snowy	-₹ 12,500.00	ICICI70090		Dhoom	Salary	
6	1-Mar-25	Omkar	-₹ 10,500.00	ICICI70090		Serendipity	Salary	
7	2-Mar-25	Cred Main EMI	-₹ 10,540.00	SBI_SA_7049	EMI_005	Serendipity	Cred Main 8th Installment	EMI

accounts_present sheet
SLNo	AccountName	Type	AccID	Balance	IntRate	NextDueDate	Bank	Tenure	EMIAmt	Comments
1	ICICI Vimala Loan EMI	EMI	EMI - 007	-₹ 170,000.00	-0.15	5th of Each Month	ICICI	22	₹ 9,912.00	Exact value to be confirmed
2	Axios Loan EMI	EMI	EMI - 001	-₹ 107,000.00	-0.15	5th of Each Month	SBI-3479	30	-₹ 13,193.23	Need to check foreclosure condition and interest rate
3	ABFL Loan	EMI	EMI - 002	-₹ 57,365.00	-0.15	5th of Each Month	SBI-3479	24	₹ 14,977.00	Need to check foreclosure condition and interest rate
4	INDMoney Main	EMI	EMI - 003	-₹ 295,542.00	-1.75	2nd of Each Month	SBI-3479	36	₹ 10,840.00	Need to check foreclosure condition and interest rate
5	CredLoan Main	EMI	EMI - 005	-₹ 289,236.00	-1.42	2nd of Each Month	SBI-3479	48	₹ 10,540.00	Need to check foreclosure condition and interest rate
6	Cred Loan Freedom	EMI	EMI - 006	-₹ 108,583.00	-1.42	2nd of Each Month	ICICI -090	36	₹ 4,353.00	Better to Foreclose

transactions_past sheet
TrNo	Date	Description	Amount	PaymentMode	AccID	Department	Comments	Category
1	2-Jul-24	Ind Money Loan	-₹ 10,840.00	SBI	EMI - 003	Serendipity	Paid EMI for July Month	EMI
2	2-Jul-24	Cred Loan	-₹ 10,540.00	SBI	EMI - 005	Serendipity	Paid EMI for July Month	EMI
3	4-Jul-24	Max Life Insurance	-₹ 1,060.00	ICICI	MAT - 001	Serendipity	Personal Insurance Linked to ICICI	Maintenance
4	5-Jul-24	Axios Loan EMI	-₹ 13,194.00	SBI	EMI - 001	Serendipity	Paid EMI for July Month	EMI
5	5-Jul-24	Paytm Loan EMI	-₹ 14,977.00	SBI	EMI - 002	Serendipity	Paid EMI for July Month	EMI
6	6-Jul-24	Office Rent Online	-₹ 30,017.70	ICICI	MAT - 001	Serendipity	Paid June Rent for Dhanalakshmi	Maintenance

