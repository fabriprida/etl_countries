from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import Base, Country, Language, CountryLanguage, Continent, Currency, CountryCurrency

def create_database():
    engine = create_engine('sqlite:///countries.db')
    Base.metadata.create_all(engine)
    return engine

def store_data(engine, data):
    Session = sessionmaker(bind=engine)
    session = Session()

    language_id_map = {}
    continent_id_map = {}
    currency_id_map = {}

    for country_data in data:
        language_data = country_data.get('languages', {}).items()
        for lang_code, lang_name in language_data:
            if lang_name not in language_id_map:
                language = Language(name=lang_name)
                session.add(language)
                session.flush() 
                language_id_map[lang_name] = language.id

        currencies_data = country_data.get('currencies', {}).items()
        for currency_code, currency_info in currencies_data:
            currency_name = currency_info['name']
            if currency_name not in currency_id_map:
                currency = Currency(code = currency_code, name = currency_info['name'])
                session.add(currency)
                session.flush()
                currency_id_map[currency_name] = currency.id
        
        country_continent = country_data.get('region', 'Unknown')
        if country_continent not in continent_id_map:
            continent_for_db = Continent(name=country_continent)
            session.add(continent_for_db)
            session.flush()
            continent_id_map[country_continent] = continent_for_db.id

        country = Country(
            name=country_data.get('name', {}).get('common', 'Unknown'),
            capital = country_data.get('capital', 'Null')[0] if len(country_data.get('capital', 'Null')) > 0 else 'Null',
            continent_id = continent_id_map[country_continent],
            population=country_data.get('population', -1),
            flag=country_data.get('flags', {}).get('png', 'Unknown')
        )

        session.add(country)
        session.flush()
        for lang_code, lang_name in language_data:
            country_language = CountryLanguage(country_id=country.id, language_id=language_id_map[lang_name])
            session.add(country_language)

        for currency_code, currency_info in currencies_data:
            country_currency = CountryCurrency(country_id = country.id, currency_id = currency_id_map[currency_info['name']])
            session.add(country_currency)
        
    session.commit()