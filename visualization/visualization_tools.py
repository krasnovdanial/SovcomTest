import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
from db.models import Debtor

engine = create_engine('postgresql://postgres:4ty1dmjh1@localhost:5432/PersonsData')

Session = sessionmaker(bind=engine)
session = Session()

data = session.query(Debtor).all()

df = pd.DataFrame([(debtor.city, debtor.street, debtor.building, debtor.apartment, (pd.to_datetime('today').year - debtor.birth_date.year)) for debtor in data], columns=['city', 'street', 'building', 'apartment', 'age'])

debt_by_region = df.groupby(['city', 'street', 'building', 'apartment']).size()
debt_by_region.plot(kind='bar')
plt.xlabel('Регион')
plt.ylabel('Сумма задолженностей')
plt.title('Суммы задолженностей по регионам')
plt.show()

df['age_group'] = pd.cut(df['age'], bins=[20, 30, 40, 50, 60, 70, 80, 90])

debt_by_age = df.groupby('age_group').size()
debt_by_age.plot(kind='bar')
plt.xlabel('Возрастная группа')
plt.ylabel('Сумма задолженностей')
plt.title('Суммы задолженностей по возрасту')
plt.show()