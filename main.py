from sqlalchemy.orm import session

from db.database_connection import engine, SessionLocal
from db.models import Base, Debtor, MonetaryObligation, Bank, ObligatoryPayment, ExtrajudicialBankruptcyMessage
from utils.file_processing import decompress_file
from utils.data_parser import parse_data, parse_debtor

Base.metadata.create_all(bind=engine)


def main(filename):
    raw_data = decompress_file(filename)

    data = parse_data(raw_data)
    db = SessionLocal()

    try:
        for item in data:
            if 'full_name' in item and 'inn' in item:
                debtor = Debtor(
                    full_name=item.get('full_name'),
                    inn=item.get('inn'),
                    index=item.get('region', None),
                    region=item.get('region', None),
                    birth_date=item.get('birth_date', None),
                    birth_place=item.get('birth_place', None),
                    city=item.get('city'),
                    street=item.get('street'),
                    building=item.get('building'),
                    apartment=item.get('apartment'),
                )

                db.add(debtor)

                db.commit()

                monetary_obligation = MonetaryObligation(
                    debtor_id=debtor.id,
                    total_sum=item.get('total_sum', None),
                    debt_sum=item.get('debt_sum', None),
                    creditor_name=item.get('creditor_name', None),
                    content=item.get('content', None),
                    basis=item.get('basis', None)
                )
                db.add(monetary_obligation)
                db.commit()

                extrajudicial_bankruptcy_message = ExtrajudicialBankruptcyMessage(
                    number=item['extrajudicial_bankruptcy_message']['number'],
                    type=item['extrajudicial_bankruptcy_message']['type'],
                    publish_date=item['extrajudicial_bankruptcy_message']['publish_date']
                )
                db.add(extrajudicial_bankruptcy_message)
                db.commit()

                obligatory_payment = ObligatoryPayment(
                    name=item['obligatory_payment']['name'],
                    sum=item['obligatory_payment']['sum']
                )
                db.add(obligatory_payment)
                db.commit()

                bank = Bank(
                    name=item['obligatory_payment']['bank']['name'],
                    bik=item['obligatory_payment']['bank']['bik']
                )
                db.add(bank)
                db.commit()

                monetary_obligation.extrajudicial_bankruptcy_message = extrajudicial_bankruptcy_message
                monetary_obligation.obligatory_payment = obligatory_payment
                obligatory_payment.bank = bank

                db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
    finally:
        db.close()


if __name__ == '__main__':
    input_filename = 'ExtrajudicialData.xml.gz'
    main(input_filename)
