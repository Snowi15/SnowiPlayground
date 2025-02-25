import sqlite3
from telethon import TelegramClient, events
from datetime import datetime
import asyncio

# Telegram credentials
API_ID = '22941664'
API_HASH = '2ee02d39b9a6dae9434689d46e0863ca'
CHAT_ID = 830726191

class TransactionNotifier:
    def __init__(self):
        print("Initializing TransactionNotifier...")
        self.client = TelegramClient('session_name', API_ID, API_HASH)
        self.conn = sqlite3.connect('kaas.db')
        self.cursor = self.conn.cursor()
        print("Database connection established")

    def parse_freedom_future_date(self, date_str):
        """Parse date from freedom_future format (DD-MMM-YY) to YYYY-MM-DD"""
        try:
            date_obj = datetime.strptime(date_str, '%d-%b-%y')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError as e:
            print(f"Date parsing error: {e}")
            return None

    def format_date_for_past(self, date_str):
        """Format date for transactions_past (D-MMM-YY)"""
        try:
            date_obj = datetime.strptime(date_str, '%d-%b-%y')
            return date_obj.strftime('%-d-%b-%y')  # %-d removes leading zero
        except ValueError as e:
            print(f"Date formatting error: {e}")
            return None

    async def get_todays_transactions(self):
        # Format date as YYYY-MM-DD 00:00:00
        today = datetime.now().strftime('%Y-%m-%d 00:00:00')
        print(f"Searching for transactions on date: {today}")
        
        try:
            # First, let's see what dates are actually in the database
            self.cursor.execute('SELECT DISTINCT date FROM freedom_future')
            dates_in_db = self.cursor.fetchall()
            print(f"Available dates in database: {dates_in_db}")
            
            query = '''
                SELECT TrNo, Date, Description, Amount, PaymentMode, AccID, Department, Comments, Category
                FROM freedom_future 
                WHERE Date = ?
            '''
            print(f"Executing query: {query} with date: {today}")
            
            self.cursor.execute(query, (today,))
            transactions = self.cursor.fetchall()
            print(f"Found {len(transactions)} transactions for today")
            
            if transactions:
                for t in transactions:
                    print(f"Transaction details: {t}")
            else:
                print("No transactions found for today")
                
            return transactions
            
        except sqlite3.Error as e:
            print(f"Database error in get_todays_transactions: {e}")
            # Print the full traceback for debugging
            import traceback
            print(traceback.format_exc())
            raise

    async def format_transaction_message(self, transaction):
        trno, date, desc, amount, payment_mode, accid, dept, comments, category = transaction
        parsed_date = self.parse_freedom_future_date(date)
        
        message = (
            f"🔔 Transaction Alert!\n\n"
            f"Date: {parsed_date}\n"
            f"Description: {desc}\n"
            f"Amount: {amount}\n"
            f"Payment Mode: {payment_mode}\n"
            f"Department: {dept}\n"
            f"Category: {category}\n"
            f"Comments: {comments}\n\n"
            f"Reply 'yes' to confirm this transaction."
        )
        return message

    async def move_to_transaction_past(self, transaction):
        try:
            # Format date for transactions_past
            transaction_list = list(transaction)
            transaction_list[1] = self.format_date_for_past(transaction_list[1])
            
            self.cursor.execute('''
                INSERT INTO transactions_past 
                (Date, Description, Amount, PaymentMode, AccID, Department, Comments, Category)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', transaction_list[1:])
            
            self.cursor.execute('DELETE FROM freedom_future WHERE TrNo = ?', (transaction[0],))
            
            # Update account balance
            amount_str = transaction[3].replace('₹', '').replace(',', '').strip()
            amount_float = float(amount_str)
            
            self.cursor.execute('''
                UPDATE accounts_present 
                SET Balance = Balance - ?
                WHERE AccountName = ?
            ''', (amount_float, transaction[4]))  # transaction[4] is PaymentMode
            
            self.conn.commit()
            
        except (sqlite3.Error, ValueError) as e:
            print(f"Error processing transaction: {e}")
            self.conn.rollback()
            raise

    async def update_account_balance(self, payment_mode, amount):
        try:
            # Convert amount string to float
            amount_str = amount.replace('₹', '').replace(',', '').strip()
            amount_float = float(amount_str)
            
            # Update balance in accounts_present
            self.cursor.execute('''
                UPDATE accounts_present 
                SET Balance = Balance - ? 
                WHERE AccountName = ?
            ''', (amount_float, payment_mode))
            
            self.conn.commit()
            print(f"Updated balance for account {payment_mode}")
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            raise

    async def handle_response(self, event, transaction):
        if event.message.text.lower() == 'yes':
            await self.move_to_transaction_past(transaction)
            await event.reply("Transaction confirmed and processed! ✅")

    async def run(self):
        await self.client.start()
        print("Telegram client started")

        transactions = await self.get_todays_transactions()
        if not transactions:
            print("No transactions found for today")
            return

        for transaction in transactions:
            message = await self.format_transaction_message(transaction)
            sent_message = await self.client.send_message(CHAT_ID, message)
            
            try:
                # Wait for response for 1 hour
                response = await self.client.wait_event(
                    events.NewMessage(chats=CHAT_ID, pattern='(?i)^yes$'),
                    timeout=3600
                )
                await self.handle_response(response, transaction)
            except asyncio.TimeoutError:
                await self.client.send_message(CHAT_ID, "Transaction confirmation timed out ⏰")

async def main():
    notifier = TransactionNotifier()
    await notifier.run()

if __name__ == "__main__":
    asyncio.run(main())
