#   Python Libraries
import datetime
from typing import List, Any

#   Third-party Libraries
import yagmail # type: ignore (Library lacks type stubs)

#   Internal Libraries
from .database_connection import MariaDB
from lib.config.env_config import settings

class Calculators:
    '''         Calculators     

        DateCountDown :
            Calculates how many years, months days left
    '''

    def __init__(self): pass

    def date_count_down(self, arg: datetime.date) -> int:
        today: datetime.date = datetime.date.today()
        total_days: int = (arg - today).days
        return total_days

class SendMail:
    def __init__(self): self.kalc = Calculators()

    def configuration(self) -> List[List[Any]]:
        maria_db = MariaDB()
        database: str = settings.DATABASE7
        dates: List[List[Any]] = []
        query = 'SELECT * FROM lib'
        data: List[List[Any]] = maria_db.select_from_table(database, query)
        if data:
            for row in data:
                dates.append(row)
        return dates
    
    def send_mail_outlook(self, SMPTMASTER: str, SMTPPASSWORD: str, RECIEVER: str):
        pass

    def send_mail_yahoo(self, SMPTMASTER: str, SMTPPASSWORD: str, RECIEVER: str):
        pass

    def send_mail_gmail(self, SMPTMASTER: str, SMTPPASSWORD: str, RECIEVER: str):
        '''
            Sends an email, different functions for different mail 
            services setups.
        '''
        records: List[List[Any]] = self.configuration()
        if not records: return

        for row in records:
            #   Calculating the return date and the overdue date, by using the date count down function
            return_date_days: int = self.kalc.date_count_down(row[7])
            over_due_date_days: int = self.kalc.date_count_down(row[8])

            if return_date_days == 7:
                msg = f'''   greetings, {row[9]}.
                This is reminder to return {row[2]}, by {row[3]} with-in {return_date_days} days.
                If the store is closed, please deliver the given book in a propper box outside the store. 
                If the book is not delivered by {row[7]} a fine may apply\n This is an automatic generated email, please do not respond.'''   

                #  Sending an e-mail 
                yagmail.SMTP(SMPTMASTER, SMTPPASSWORD).send(to=RECIEVER, subject="Book Return Reminder", contents=msg) # type: ignore (Library lacks type stubs)

            elif over_due_date_days == 0:
                msg = f'''   greetings {row[3]}.
                We can see in our database you've forgotten to deliver {row[2]}. 
                We would appreciate if you could deliver the book with-in the next few days.
                If the store is closed, please deliver the given book in a propper box outside the store. '''
                
                #  Sending an e-mail
                yagmail.SMTP(SMPTMASTER, SMTPPASSWORD).send(to=RECIEVER, subject="Overdue Book", contents=msg) # type: ignore (Library lacks type stubs)

        return

    def send_mail_server(self,SMPTMASTER:str, SMTPPASSWORD:str, RECIEVER:str):
        pass
