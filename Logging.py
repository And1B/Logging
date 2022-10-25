import random
import logging
import sys

from datetime import datetime

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('formatted.log')

formatter = logging.Formatter('%(asctime)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    
  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
      if pin != 1234:
        logger.error('Error! Invalid pin. Try again.')
      else:
        return None
 
  def deposit(self):
    try:
      amount=float(input("Enter amount to be deposited: "))
      if amount < 0:
        logger.warning('Warning! You entered a negative number to deposit.')
      self.balance += amount
      print("Amount Deposited: ${amount}".format(amount=amount))
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
    except ValueError:
      logger.error("Error! You entered a non-number value to deposit.")
      logger.error("Status: Failed")
      logger.error("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    
  def withdraw(self):
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      if self.balance >= amount:
        self.balance -= amount
        logger.info("You withdrew: ${amount}".format( amount=amount))
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      else:
        logger.error("Error! Insufficient balance to complete withdrawel.")
        logger.error("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.error("Error! You entered a non-number value to withdraw.")
      logger.error("Transaction #{number}".format(number=random.randint(10000, 1000000)))
 
  def display(self):
    print("Available Balance = ${balance}".format(balance=self.balance))
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()
