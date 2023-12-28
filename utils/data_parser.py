from datetime import datetime
import xml.etree.ElementTree as ET


def parse_address(address):
    parts = address.split(', ')
    return {
        'region': parts[0] if parts and parts[0] else None,
        'city': parts[1] if len(parts) > 1 else None,
        'street': parts[2] if len(parts) > 2 else None,
        'building': parts[3] if len(parts) > 3 else None,
        'apartment': parts[4] if len(parts) > 4 else None
    }


def parse_debtor(debtor_xml):
    debtor_data = {
        'full_name': debtor_xml.find('Name').text,
        'inn': debtor_xml.find('Inn').text,
        'birth_date': datetime.strptime(debtor_xml.find('BirthDate').text, '%Y-%m-%dT%H:%M:%SZ').date(),
        'birth_place': debtor_xml.find('BirthPlace').text,
    }
    address_text = debtor_xml.find('Address').text if debtor_xml.find('Address') is not None else ''
    address_data = parse_address(address_text)
    debtor_data.update(address_data)
    return debtor_data


def parse_monetary_obligation(mo_xml):
    return {
        'creditor_name': mo_xml.find('CreditorName').text,
        'total_sum': mo_xml.find('TotalSum').text,
        'debt_sum': mo_xml.find('DebtSum').text,
        'content': mo_xml.find('Content').text,
        'basis': mo_xml.find('Basis').text,
    }


def parse_data(raw_data):
    tree = ET.ElementTree(ET.fromstring(raw_data))
    root = tree.getroot()

    bankruptcy_messages = root.findall('ExtrajudicialBankruptcyMessage')

    parsed_data = []
    for message in bankruptcy_messages:
        debtor_data = parse_debtor(message.find('Debtor'))

        mo_info = message.findall('CreditorsNonFromEntrepreneurship/MonetaryObligations/MonetaryObligation')

        for mo in mo_info:
            mo_data = parse_monetary_obligation(mo)
            parsed_data.append({'debtor_data': debtor_data, 'mo_data': mo_data})

    return parsed_data

